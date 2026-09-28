class_name Games
extends RefCounted

const ORDER := ["joey", "leaves", "sort", "fog", "orchard", "photo"]
const ICON := {
	"joey": "chars/joey_stand", "leaves": "atlas/javor", "sort": "ui/basket",
	"fog": "atlas/jesterka", "orchard": "atlas/jablko", "photo": "ui/camera",
}


static func make(id: String) -> MiniGame:
	match id:
		"leaves":
			return Leaves.new()
		"sort":
			return Sort.new()
		"fog":
			return Fog.new()
		"orchard":
			return Orchard.new()
		"photo":
			return Photo.new()
	return JoeyTrail.new()


static func ground_spots(n: int, area: Rect2, gap: float) -> Array:
	var out := []
	var tries := 0
	while out.size() < n and tries < 2000:
		tries += 1
		var p := Vector2(randf_range(area.position.x, area.end.x), randf_range(area.position.y, area.end.y))
		if out.all(func(q): return q.distance_to(p) > gap):
			out.append(p)
	return out


class JoeyTrail extends MiniGame:
	var joey := Sprite2D.new()
	var cones: Array[Sprite2D] = []

	func _init() -> void:
		id = "joey"
		bg = "brdlavka"

	func setup() -> void:
		total = {"jezek": 6, "veverka": 8, "sova": 10}[prof]
		for p in Games.ground_spots(total, Rect2(220, 560, 1500, 400), 170.0):
			var c := UI.sprite("res://assets/ui/cone_icon.png", p, 0.9 * big)
			play.add_child(c)
			UI.bob(c, 6, 1.4)
			cones.append(c)
		joey.texture = UI.tex("res://assets/chars/joey_stand.png")
		joey.scale = Vector2(0.7, 0.7)
		joey.position = Vector2(160, 900)
		play.add_child(joey)

	func demo_steps() -> Array:
		return [{"to": Vector2(220, 860)}, {"to": cones[0].position, "time": 1.4}]

	func tick(delta: float) -> void:
		var target := get_global_mouse_position()
		var d := target - joey.position
		if d.length() > 8.0:
			joey.flip_h = d.x < 0
			joey.position += d.limit_length(620.0 * speed * delta)
		for c in cones.duplicate():
			if c.position.distance_to(joey.position) < 110.0 * big:
				collect(c)

	func collect(c: Sprite2D) -> void:
		cones.erase(c)
		Sound.play("bark")
		var tw: Tween = c.create_tween()
		tw.tween_property(c, "scale", c.scale * 1.6, 0.15)
		tw.tween_property(c, "modulate:a", 0.0, 0.2)
		tw.tween_callback(c.queue_free)
		point(c.position)

	func stars() -> int:
		var t := elapsed * speed
		return 3 if t < 30.0 else (2 if t < 55.0 else 1)


class Leaves extends MiniGame:
	const KINDS := ["javor", "buk", "briza", "dub", "modrin"]
	var spawned := 0
	var cooldown := 1.0
	var leaves: Array[Sprite2D] = []

	func _init() -> void:
		id = "leaves"
		bg = "chlumec"

	func setup() -> void:
		total = {"jezek": 10, "veverka": 14, "sova": 18}[prof]

	func demo_steps() -> Array:
		return [{"to": Vector2(900, 420)}, {"to": Vector2(960, 520), "time": 0.8, "clicks": 1}]

	func tick(delta: float) -> void:
		cooldown -= delta
		if cooldown <= 0.0 and spawned < total:
			spawn()
		for l in leaves.duplicate():
			var t: float = l.get_meta("t") + delta
			l.set_meta("t", t)
			l.position.y += 120.0 * speed * delta
			l.position.x = l.get_meta("x") + sin(t * 1.6) * 90.0
			l.rotation = sin(t * 2.1) * 0.6
			if l.position.y > 1000:
				leaves.erase(l)
				mistakes += 1
				var tw: Tween = l.create_tween()
				tw.tween_property(l, "modulate:a", 0.0, 0.4)
				tw.tween_callback(l.queue_free)
				_check_end()

	func spawn() -> Sprite2D:
		spawned += 1
		cooldown = 1.6 / speed
		var l := UI.sprite("res://assets/atlas/%s.png" % KINDS.pick_random(), Vector2(randf_range(250, 1650), 170), 0.55 * big)
		l.set_meta("x", l.position.x)
		l.set_meta("t", randf() * 3.0)
		play.add_child(l)
		leaves.append(l)
		return l

	func _unhandled_input(event: InputEvent) -> void:
		if done or not MiniGame.mouse_pressed(event):
			return
		for l in leaves:
			if l.position.distance_to(get_global_mouse_position()) < 90.0 * big:
				catch(l)
				return
		Sound.play("boing")

	func catch(l: Sprite2D) -> void:
		leaves.erase(l)
		var tw: Tween = l.create_tween()
		tw.tween_property(l, "position", Vector2(1720, 60), 0.5).set_trans(Tween.TRANS_SINE)
		tw.parallel().tween_property(l, "scale", Vector2(0.15, 0.15), 0.5)
		tw.tween_callback(l.queue_free)
		got += 1
		counter.text = "%d / %d" % [got, total]
		UI.pulse(counter)
		Sound.play("pop")
		_check_end()

	func _check_end() -> void:
		if spawned >= total and leaves.is_empty():
			finish.call_deferred()


class Sort extends MiniGame:
	var basket: Sprite2D
	var camera: Sprite2D
	var items: Array[Sprite2D] = []
	var held: Sprite2D
	var grab := Vector2.ZERO

	func _init() -> void:
		id = "sort"
		bg = "provazec"

	func setup() -> void:
		total = {"jezek": 5, "veverka": 7, "sova": 9}[prof]
		basket = UI.sprite("res://assets/ui/basket.png", Vector2(330, 860), 2.2)
		camera = UI.sprite("res://assets/ui/camera.png", Vector2(1590, 860), 2.2)
		play.add_child(basket)
		play.add_child(camera)
		var good: Array = Atlas.ids_in_tab("basket").filter(func(i): return not Atlas.entry(i).rare)
		var bad: Array = Atlas.ids_in_tab("photo").filter(func(i): return Atlas.entry(i).cat == "poison")
		good.shuffle()
		var ids: Array = good.slice(0, total - 2) + [bad[0], bad[1]]
		ids.shuffle()
		var spots := Games.ground_spots(total, Rect2(560, 420, 800, 420), 170.0)
		for i in ids.size():
			var s := UI.sprite("res://assets/atlas/%s.png" % ids[i], spots[i], 0.6 * big)
			s.set_meta("id", ids[i])
			s.set_meta("home", spots[i])
			play.add_child(s)
			items.append(s)
			var name_l := UI.label(Atlas.name_of(ids[i]), 26, UI.INK, 8)
			s.add_child(name_l)
			name_l.reset_size()
			name_l.scale = Vector2.ONE / s.scale
			name_l.position = Vector2(-name_l.size.x / 2, 115) / s.scale

	func demo_steps() -> Array:
		var s := items[0]
		var target := camera.position if _poison(s) else basket.position
		return [{"to": s.position, "clicks": 1}, {"to": target, "time": 1.2}]

	func _poison(s: Sprite2D) -> bool:
		return Atlas.entry(s.get_meta("id")).cat == "poison"

	func _unhandled_input(event: InputEvent) -> void:
		if done:
			return
		if MiniGame.mouse_pressed(event):
			for s in items:
				if s.position.distance_to(get_global_mouse_position()) < 100.0 * big:
					held = s
					grab = s.position - get_global_mouse_position()
					s.z_index = 50
					UI.pulse(s, 1.15)
					Sound.play("pop")
					return
		elif event is InputEventMouseMotion and held:
			held.position = get_global_mouse_position() + grab
		elif MiniGame.mouse_released(event) and held:
			drop(held, get_global_mouse_position())
			held = null

	func drop(s: Sprite2D, at: Vector2) -> void:
		s.z_index = 0
		var right := camera if _poison(s) else basket
		var wrong := basket if right == camera else camera
		if at.distance_to(right.position) < 190.0 * big:
			items.erase(s)
			if right == camera:
				Sound.play("shutter")
			else:
				Sound.play("plop")
			var tw: Tween = s.create_tween()
			tw.tween_property(s, "position", right.position, 0.25)
			tw.parallel().tween_property(s, "scale", s.scale * 0.3, 0.25)
			tw.tween_callback(s.queue_free)
			name_card(s.get_meta("id"), right.position + Vector2(0, -160))
			point()
			return
		if at.distance_to(wrong.position) < 190.0 * big:
			mistakes += 1
			Sound.play("boing")
			Sound.say("ui_wrong_place")
			if _poison(s):
				Sound.say_after("ui_dont_touch", Save.lang(), 1.6)
		var tw: Tween = s.create_tween()
		tw.tween_property(s, "position", s.get_meta("home"), 0.35).set_trans(Tween.TRANS_BACK)

	func stars() -> int:
		return 3 if mistakes == 0 else (2 if mistakes <= 2 else 1)


class Fog extends MiniGame:
	const W := 192
	const H := 108
	const CELL := 10.0
	var fog := Image.create(W, H, false, Image.FORMAT_RGBA8)
	var fog_tex: ImageTexture
	var buried: Array[Sprite2D] = []
	var rubbing := false
	var _dirty := false
	var _idle := 0.0

	func _init() -> void:
		id = "fog"
		bg = "plesivec"

	func setup() -> void:
		total = {"jezek": 2, "veverka": 3, "sova": 4}[prof]
		var pool := ["jesterka", "slepys", "vazka", "zaba", "vres", "materidouska", "borovice", "boruvka", "kane", "kos"]
		pool.shuffle()
		var spots := Games.ground_spots(total, Rect2(300, 380, 1320, 520), 330.0)
		for i in total:
			var s := UI.sprite("res://assets/atlas/%s.png" % pool[i], spots[i], 0.9 * big)
			s.set_meta("id", pool[i])
			play.add_child(s)
			buried.append(s)
		for y in H:
			for x in W:
				fog.set_pixel(x, y, Color(0.93, 0.95, 0.97, 0.96 - 0.1 * sin(x * 0.15) * sin(y * 0.2)))
		fog_tex = ImageTexture.create_from_image(fog)
		var sp := Sprite2D.new()
		sp.texture = fog_tex
		sp.centered = false
		sp.scale = Vector2(CELL, CELL)
		sp.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
		sp.z_index = 100
		add_child(sp)

	func demo_steps() -> Array:
		var c := Vector2(960, 620)
		return [{"to": c + Vector2(-160, -60)}, {"to": c + Vector2(160, -20), "time": 0.5}, {"to": c + Vector2(-160, 40), "time": 0.5}, {"to": c + Vector2(160, 80), "time": 0.5}]

	func _unhandled_input(event: InputEvent) -> void:
		if done:
			return
		if MiniGame.mouse_pressed(event):
			rubbing = true
			rub(get_global_mouse_position())
		elif MiniGame.mouse_released(event):
			rubbing = false
		elif event is InputEventMouseMotion and rubbing:
			rub(get_global_mouse_position())

	func rub(at: Vector2, r := 0.0) -> void:
		var radius := r if r > 0.0 else 5.5 * big
		var c := at / CELL
		for y in range(int(c.y - radius) - 1, int(c.y + radius) + 2):
			for x in range(int(c.x - radius) - 1, int(c.x + radius) + 2):
				if x < 0 or y < 0 or x >= W or y >= H:
					continue
				var d := Vector2(x, y).distance_to(c) / radius
				if d < 1.0:
					var px := fog.get_pixel(x, y)
					px.a = minf(px.a, smoothstep(0.55, 1.0, d) * px.a)
					fog.set_pixel(x, y, px)
		_dirty = true
		_idle = 0.0

	func cleared(s: Sprite2D) -> float:
		var c := s.position / CELL
		var n := 0
		var clear := 0
		for y in range(int(c.y) - 6, int(c.y) + 7, 2):
			for x in range(int(c.x) - 6, int(c.x) + 7, 2):
				if x < 0 or y < 0 or x >= W or y >= H:
					continue
				n += 1
				if fog.get_pixel(x, y).a < 0.35:
					clear += 1
		return float(clear) / maxi(n, 1)

	func tick(delta: float) -> void:
		_idle += delta
		if _dirty:
			_dirty = false
			fog_tex.update(fog)
			for s in buried.duplicate():
				if cleared(s) > 0.5:
					reveal(s)
		if _idle > 12.0 and not buried.is_empty():
			_idle = 0.0
			sparkle(buried[0].position)

	func reveal(s: Sprite2D) -> void:
		buried.erase(s)
		rub(s.position, 11.0 * big)
		UI.pulse(s, 1.3)
		name_card(s.get_meta("id"), s.position + Vector2(0, -110))
		point(s.position)

	func stars() -> int:
		var t := elapsed * speed
		return 3 if t < 40.0 else (2 if t < 75.0 else 1)


class Orchard extends MiniGame:
	var targets: Array[Sprite2D] = []
	var basket: Sprite2D
	var last_click := -10.0
	var last_pos := Vector2.ZERO
	var window := 0.6

	func _init() -> void:
		id = "orchard"
		bg = "sady"

	func setup() -> void:
		total = {"jezek": 6, "veverka": 8, "sova": 10}[prof]
		window = {"jezek": 0.9, "veverka": 0.6, "sova": 0.5}[prof]
		var tree := UI.standing("res://assets/props/apple_tree.png", Vector2(760, 1020), 1.0)
		play.add_child(tree)
		basket = UI.sprite("res://assets/ui/basket.png", Vector2(1500, 900), 2.2)
		play.add_child(basket)
		var nuts := total / 3
		var apples := total - nuts
		var crown := Games.ground_spots(apples, Rect2(460, 380, 600, 200), 120.0)
		for p in crown:
			_add("jablko", p, 0.42)
		for p in Games.ground_spots(nuts, Rect2(1050, 900, 250, 80), 110.0):
			_add("orech", p, 0.42)

	func _add(kind: String, at: Vector2, s: float) -> void:
		var sp := UI.sprite("res://assets/atlas/%s.png" % kind, at, s * big)
		sp.set_meta("id", kind)
		play.add_child(sp)
		targets.append(sp)

	func demo_steps() -> Array:
		return [{"to": targets[0].position + Vector2(-60, 80)}, {"to": targets[0].position, "time": 0.6, "clicks": 2}]

	func _unhandled_input(event: InputEvent) -> void:
		if done or not MiniGame.mouse_pressed(event):
			return
		var now := Time.get_ticks_msec() / 1000.0
		var double := now - last_click < window and get_global_mouse_position().distance_to(last_pos) < 40.0 * big
		last_click = -10.0 if double else now
		last_pos = get_global_mouse_position()
		for t in targets:
			if t.position.distance_to(get_global_mouse_position()) < 70.0 * big:
				if double:
					pick(t)
				else:
					wiggle(t)
				return

	func wiggle(t: Sprite2D) -> void:
		var tw: Tween = t.create_tween()
		for i in 4:
			tw.tween_property(t, "rotation", 0.25 if i % 2 == 0 else -0.25, 0.06)
		tw.tween_property(t, "rotation", 0.0, 0.06)
		Sound.play("pop")

	func pick(t: Sprite2D) -> void:
		targets.erase(t)
		var tw: Tween = t.create_tween()
		if t.get_meta("id") == "jablko":
			tw.tween_property(t, "position:y", 960.0, 0.5).set_trans(Tween.TRANS_BOUNCE).set_ease(Tween.EASE_OUT)
		else:
			tw.tween_property(t, "position:y", t.position.y - 90, 0.2)
		tw.tween_property(t, "position", basket.position + Vector2(0, -30), 0.5).set_trans(Tween.TRANS_SINE)
		tw.parallel().tween_property(t, "scale", t.scale * 0.6, 0.5)
		tw.tween_callback(t.queue_free)
		Sound.play("plop")
		point(basket.position + Vector2(0, -80))

	func stars() -> int:
		var t := elapsed * speed
		return 3 if t < 30.0 else (2 if t < 55.0 else 1)


class Photo extends MiniGame:
	const BIRDS := ["sojka", "kos", "sykora", "kane", "datel", "kulisek", "volavka", "kachna"]
	var frame := Line2D.new()
	var box := Vector2(300, 220)
	var birds: Array[Sprite2D] = []
	var spawned := 0
	var cooldown := 1.0

	func _init() -> void:
		id = "photo"
		bg = "valy"

	func setup() -> void:
		total = {"jezek": 8, "veverka": 10, "sova": 12}[prof]
		box = Vector2(300, 220) * big
		frame.width = 6
		frame.default_color = Color(1, 1, 1, 0.95)
		frame.z_index = 120
		var hx := box.x / 2
		var hy := box.y / 2
		frame.points = PackedVector2Array([Vector2(-hx, -hy), Vector2(hx, -hy), Vector2(hx, hy), Vector2(-hx, hy), Vector2(-hx, -hy)])
		add_child(frame)
		var dot := UI.label("+", 48, Color.WHITE, 8)
		dot.position = Vector2(-14, -34)
		frame.add_child(dot)

	func demo_steps() -> Array:
		return [{"to": Vector2(600, 400)}, {"to": Vector2(900, 380), "time": 1.0, "clicks": 1}]

	func tick(delta: float) -> void:
		frame.position = get_global_mouse_position()
		cooldown -= delta
		var max_on := 1 if prof == "jezek" else 2
		if cooldown <= 0.0 and spawned < total and birds.size() < max_on:
			spawn()
		for b in birds.duplicate():
			var t: float = b.get_meta("t") + delta
			b.set_meta("t", t)
			b.position.x += b.get_meta("dir") * 230.0 * speed * delta
			b.position.y = b.get_meta("y") + sin(t * 2.4) * 40.0
			if b.position.x < -150 or b.position.x > 2070:
				birds.erase(b)
				b.queue_free()
				mistakes += 1
				_check_end()

	func spawn() -> Sprite2D:
		spawned += 1
		cooldown = 1.5 / speed
		var dir := 1.0 if randf() < 0.5 else -1.0
		var bird: String = BIRDS.pick_random()
		var b := UI.sprite("res://assets/atlas/%s.png" % bird, Vector2(-120.0 if dir > 0 else 2040.0, 0), 0.6 * big)
		b.set_meta("id", bird)
		b.flip_h = dir < 0
		b.set_meta("dir", dir)
		b.set_meta("y", randf_range(280, 620))
		b.set_meta("t", 0.0)
		play.add_child(b)
		birds.append(b)
		return b

	func _unhandled_input(event: InputEvent) -> void:
		if done or not MiniGame.mouse_pressed(event):
			return
		Sound.play("shutter")
		var r := Rect2(get_global_mouse_position() - box / 2, box)
		for b in birds:
			if r.has_point(b.position):
				snap(b)
				return

	func snap(b: Sprite2D) -> void:
		birds.erase(b)
		var flash := ColorRect.new()
		flash.color = Color(1, 1, 1, 0.7)
		flash.size = Vector2(1920, 1080)
		flash.mouse_filter = Control.MOUSE_FILTER_IGNORE
		flash.z_index = 150
		add_child(flash)
		var fl: Tween = flash.create_tween()
		fl.tween_property(flash, "color:a", 0.0, 0.3)
		fl.tween_callback(flash.queue_free)
		name_card(b.get_meta("id"), b.position + Vector2(0, -90))
		var tw: Tween = b.create_tween()
		tw.tween_property(b, "position", Vector2(1720, 60), 0.6).set_trans(Tween.TRANS_SINE)
		tw.parallel().tween_property(b, "scale", b.scale * 0.3, 0.6)
		tw.tween_callback(b.queue_free)
		got += 1
		counter.text = "%d / %d" % [got, total]
		UI.pulse(counter)
		Sound.play("chime")
		_check_end()

	func _check_end() -> void:
		if spawned >= total and birds.is_empty():
			finish.call_deferred()
