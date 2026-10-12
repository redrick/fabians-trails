class_name KeyGames
extends RefCounted

const ORDER := ["copy", "cut", "undo", "rake", "drill"]
const ICON := {
	"copy": "atlas/smrk", "cut": "atlas/zajic", "undo": "atlas/sojka", "rake": "atlas/buk", "drill": "chars/fabian_wave",
}
const HINT_AFTER := 4.0
const MODS := [KEY_CTRL, KEY_ALT, KEY_SHIFT, KEY_META]

# One entry per shortcut: [keys, picture]. Text keys are "key_<id>" (label) and "act_<id>" (voice).
const SHORTCUTS := {
	"copy": [[KEY_CTRL, KEY_C], "atlas/hrib"],
	"paste": [[KEY_CTRL, KEY_V], "ui/basket"],
	"cut": [[KEY_CTRL, KEY_X], "atlas/zajic"],
	"undo": [[KEY_CTRL, KEY_Z], "atlas/sojka"],
	"selectall": [[KEY_CTRL, KEY_A], "atlas/javor"],
	"save": [[KEY_CTRL, KEY_S], "ui/atlas"],
	"find": [[KEY_CTRL, KEY_F], "chars/joey_sniff"],
	"print": [[KEY_CTRL, KEY_P], "ui/herbarium"],
	"rename": [[KEY_F2], "ui/house"],
	"delete": [[KEY_DELETE], "atlas/buk"],
	"closetab": [[KEY_CTRL, KEY_W], "ui/lock"],
	"newtab": [[KEY_CTRL, KEY_T], "ui/cone_icon"],
	"newwindow": [[KEY_CTRL, KEY_N], "ui/question"],
	"switch": [[KEY_ALT, KEY_TAB], "chars/joey_stand"],
	"close": [[KEY_ALT, KEY_F4], "ui/sun"],
}
const EASY := ["copy", "paste", "undo", "selectall", "save", "delete"]
const SAFE := ["copy", "paste", "cut", "undo", "selectall", "save", "find", "print", "rename", "delete"]
# Browsers keep these for themselves (Ctrl+W closes the tab), so they only exist in the downloaded game.
const DESKTOP := ["closetab", "newtab", "newwindow", "switch", "close"]


static func make(id: String) -> MiniGame:
	match id:
		"cut":
			return Cut.new()
		"undo":
			return Undo.new()
		"rake":
			return Rake.new()
		"drill":
			return Drill.new()
	return Copy.new()


static func key_name(code: int) -> String:
	match code:
		KEY_CTRL:
			return "Ctrl"
		KEY_ALT:
			return "Alt"
		KEY_DELETE:
			return "Delete"
	return OS.get_keycode_string(code)


# Matched by keycode or key label (what is printed on the key), never by position: a Czech QWERTZ
# keyboard has Z and Y swapped.
static func hit(event: InputEvent, keys: Array) -> bool:
	if not (event is InputEventKey and event.pressed and not event.echo):
		return false
	var e := event as InputEventKey
	var ctrl := e.ctrl_pressed or (OS.has_feature("macos") and e.meta_pressed)
	var code: int = keys[-1]
	return ctrl == (KEY_CTRL in keys) and e.alt_pressed == (KEY_ALT in keys) and (e.keycode == code or e.key_label == code)


static func is_shortcut_try(event: InputEvent) -> bool:
	if not (event is InputEventKey and event.pressed and not event.echo):
		return false
	var e := event as InputEventKey
	if e.keycode in MODS:
		return false
	return e.ctrl_pressed or e.alt_pressed or e.keycode in [KEY_DELETE, KEY_F2, KEY_TAB, KEY_F4, KEY_BACKSPACE]


static func sprite_fit(path: String, at: Vector2, h: float) -> Sprite2D:
	var s := UI.sprite("res://assets/%s.png" % path, at)
	s.scale = Vector2.ONE * h / maxf(s.texture.get_height(), 1.0)
	return s


class Cap extends Node2D:
	const H := 92.0
	const SIZE := 50
	var text := ""
	var code := KEY_NONE
	var lit := false
	var w := 0.0

	func _init(c: int) -> void:
		code = c
		text = KeyGames.key_name(c)
		w = maxf(H, UI.FONT.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, SIZE).x + 46)

	func set_lit(v: bool) -> void:
		if v == lit:
			return
		lit = v
		scale = Vector2.ONE * (1.12 if v else 1.0)
		queue_redraw()

	func _draw() -> void:
		var sb := UI.box(UI.YELLOW if lit else UI.PAPER, 14, 6 if lit else 4, Color("e0473f") if lit else UI.WOOD)
		draw_style_box(sb, Rect2(-w / 2, -H / 2, w, H))
		var s := UI.FONT.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, SIZE)
		var base := (UI.FONT.get_ascent(SIZE) - UI.FONT.get_descent(SIZE)) / 2.0
		draw_string(UI.FONT, Vector2(-s.x / 2, base - 4), text, HORIZONTAL_ALIGNMENT_LEFT, -1, SIZE, UI.INK)


# The file-manager look of a selection: yellow glow and a dashed edge. Holes (empty spots) always show a
# faint dashed ring.
class Frame extends Node2D:
	var size := Vector2(200, 200)
	var round := false
	var lit := false
	var idle_visible := false

	func _init(s: Vector2, is_round := false, show_idle := false) -> void:
		size = s
		round = is_round
		idle_visible = show_idle
		z_index = 40

	func set_lit(v: bool) -> void:
		lit = v
		queue_redraw()

	func _draw() -> void:
		if not lit and not idle_visible:
			return
		var ink := UI.INK if lit else Color(UI.INK, 0.6)
		if round:
			var r := size.x / 2
			if not lit:
				draw_circle(Vector2.ZERO, r, Color(1, 1, 1, 0.35))
			if lit:
				draw_circle(Vector2.ZERO, r, Color(1, 0.85, 0.3, 0.3))
				draw_arc(Vector2.ZERO, r, 0, TAU, 64, Color(UI.YELLOW, 0.9), 10.0)
			for i in 24:
				draw_arc(Vector2.ZERO, r, i * TAU / 24, (i + 0.55) * TAU / 24, 6, ink, 5.0)
			return
		var rc := Rect2(-size / 2, size)
		var pts := [rc.position, Vector2(rc.end.x, rc.position.y), rc.end, Vector2(rc.position.x, rc.end.y), rc.position]
		if lit:
			draw_rect(rc, Color(1, 0.85, 0.3, 0.3))
			draw_rect(rc, Color(UI.YELLOW, 0.9), false, 10.0)
		for i in 4:
			draw_dashed_line(pts[i], pts[i + 1], ink, 5.0, 18.0)


class KeyGame extends MiniGame:
	var caps := Node2D.new()
	var cap_nodes: Array[Cap] = []
	var idle := 0.0
	var clip_box := Node2D.new()

	func _ready() -> void:
		menu = "keys"
		caps.z_index = 220
		caps.position = Vector2(960, 975)
		super._ready()
		add_child(caps)
		clip_box.z_index = 210
		clip_box.position = Vector2(1760, 210)
		clip_box.visible = false
		add_child(clip_box)

	# combos: [[text key, [keycodes]], ...], shown side by side with the action word above.
	func set_hint(combos: Array) -> void:
		for c in caps.get_children():
			c.queue_free()
		cap_nodes.clear()
		var parts := []
		var total_w := 0.0
		for combo in combos:
			var row := Node2D.new()
			var x := 0.0
			var keys: Array = combo[1]
			for i in keys.size():
				if i > 0:
					var plus := UI.label("+", 50, UI.INK, 10)
					plus.position = Vector2(x + 8, -42)
					row.add_child(plus)
					x += 52
				var cap := Cap.new(keys[i])
				cap.position = Vector2(x + cap.w / 2, 0)
				row.add_child(cap)
				cap_nodes.append(cap)
				x += cap.w
			var word := UI.label(Text.t(combo[0]), 34, UI.INK, 10)
			word.position = Vector2(0, -102)
			row.add_child(word)
			parts.append([row, x])
			total_w += x
		total_w += 90.0 * maxi(parts.size() - 1, 0)
		var at := -total_w / 2
		for p in parts:
			p[0].position = Vector2(at, 0)
			caps.add_child(p[0])
			at += p[1] + 90.0

	func show_hint_now() -> void:
		idle = HINT_AFTER

	func step_done() -> void:
		idle = 0.0

	func _process(delta: float) -> void:
		super._process(delta)
		idle += delta
		caps.visible = not done and (prof == "jezek" or idle >= HINT_AFTER)
		for c in cap_nodes:
			c.set_lit(Input.is_key_pressed(c.code) or Input.is_key_label_pressed(c.code))

	func _demo() -> void:
		super._demo()
		show_hint_now()

	func show_clip(path: String) -> void:
		for c in clip_box.get_children():
			c.queue_free()
		var p := UI.panel()
		p.mouse_filter = Control.MOUSE_FILTER_IGNORE
		p.custom_minimum_size = Vector2(230, 230)
		clip_box.add_child(p)
		p.position = Vector2(-115, -115)
		var l := UI.label(Text.t("clipboard"), 30, UI.INK)
		l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		l.custom_minimum_size = Vector2(230, 0)
		l.position = Vector2(-115, -110)
		clip_box.add_child(l)
		clip_box.add_child(KeyGames.sprite_fit(path, Vector2(0, 25), 140))
		clip_box.visible = true
		UI.pulse(clip_box, 1.15)

	func clear_clip() -> void:
		clip_box.visible = false

	func wrong() -> void:
		Sound.play("boing")
		show_hint_now()

	func near(list: Array, at: Vector2, r: float) -> Node2D:
		for n in list:
			if n.position.distance_to(at) < r * big:
				return n
		return null

	func _unhandled_input(event: InputEvent) -> void:
		if done:
			return
		if event is InputEventKey:
			on_key(event)
		elif MiniGame.mouse_pressed(event):
			on_click(get_global_mouse_position())

	func on_key(_e: InputEvent) -> void:
		pass

	func on_click(_at: Vector2) -> void:
		pass


# Plant a forest: copy a tree, click an empty spot, paste. The clipboard keeps the tree, so one copy
# can be pasted again and again.
class Copy extends KeyGame:
	var sources: Array[Sprite2D] = []
	var holes: Array[Sprite2D] = []
	var sel: Sprite2D
	var clip := ""

	func _init() -> void:
		id = "copy"
		bg = "pole"

	func setup() -> void:
		total = {"jezek": 4, "veverka": 6, "sova": 8}[prof]
		var kinds: Array = {"jezek": ["smrk"], "veverka": ["smrk", "buk"], "sova": ["smrk", "buk", "jedle"]}[prof]
		var shelf := UI.panel()
		shelf.mouse_filter = Control.MOUSE_FILTER_IGNORE
		var ys := []
		for i in kinds.size():
			ys.append(420 + i * 200 if kinds.size() > 1 else 600)
		shelf.custom_minimum_size = Vector2(300, ys[-1] - ys[0] + 230)
		shelf.position = Vector2(100, ys[0] - 115)
		play.add_child(shelf)
		for i in kinds.size():
			var s := _tree(kinds[i], Vector2(250, ys[i]))
			sources.append(s)
		var spots := Games.ground_spots(total, Rect2(620, 470, 1150, 380), 185.0 * big)
		for i in spots.size():
			var kind: String = kinds[i % kinds.size()]
			var ghost := UI.sprite("res://assets/atlas/%s.png" % kind, spots[i], 0.55 * big)
			ghost.modulate = Color(0.25, 0.2, 0.1, 0.35)
			ghost.set_meta("kind", kind)
			var f := Frame.new(Vector2(170, 170) * big, true, true)
			ghost.set_meta("frame", f)
			f.position = spots[i]
			play.add_child(ghost)
			play.add_child(f)
			holes.append(ghost)
		total = holes.size()
		set_hint([["key_copy", [KEY_CTRL, KEY_C]], ["key_paste", [KEY_CTRL, KEY_V]]])

	func _tree(kind: String, at: Vector2) -> Sprite2D:
		var s := UI.sprite("res://assets/atlas/%s.png" % kind, at, 0.7 * big)
		s.set_meta("kind", kind)
		var f := Frame.new(Vector2(200, 200) * big)
		f.position = at
		s.set_meta("frame", f)
		play.add_child(s)
		play.add_child(f)
		return s

	func demo_steps() -> Array:
		return [{"to": sources[0].position, "clicks": 1}, {"to": holes[0].position, "time": 1.2, "clicks": 1}]

	func select(s: Sprite2D) -> void:
		if sel:
			sel.get_meta("frame").set_lit(false)
		sel = s
		if s:
			s.get_meta("frame").set_lit(true)
			Sound.play("pop")

	func on_click(at: Vector2) -> void:
		var s := near(sources, at, 110.0)
		if not s:
			s = near(holes, at, 100.0)
		select(s)

	func on_key(e: InputEvent) -> void:
		if KeyGames.hit(e, [KEY_CTRL, KEY_C]):
			copy()
		elif KeyGames.hit(e, [KEY_CTRL, KEY_V]):
			paste()
		elif KeyGames.is_shortcut_try(e):
			wrong()

	func copy() -> void:
		if not sel or sel in holes:
			wrong()
			return
		clip = sel.get_meta("kind")
		show_clip("atlas/" + clip)
		Sound.play("chime")
		step_done()

	func paste() -> void:
		if clip == "" or not sel or not sel in holes:
			wrong()
			return
		var hole := sel
		if hole.get_meta("kind") != clip:
			mistakes += 1
			wrong()
			Sound.say("ui_wrong_place")
			UI.pulse(hole, 1.2)
			return
		select(null)
		holes.erase(hole)
		hole.get_meta("frame").queue_free()
		hole.queue_free()
		var t := _tree(clip, hole.position)
		sources.append(t)
		t.scale = Vector2.ZERO
		t.create_tween().tween_property(t, "scale", Vector2.ONE * 0.55 * big, 0.3).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
		Sound.play("plop")
		step_done()
		point(hole.position)

	func stars() -> int:
		return 3 if mistakes == 0 else (2 if mistakes <= 2 else 1)


# Animals sit in the wrong places. Cut one out, click its shadow at home, paste it there.
class Cut extends KeyGame:
	const POOL := ["zajic", "jezek", "veverka", "liska", "srna", "zaba", "kachna", "jezevec"]
	var animals: Array[Sprite2D] = []
	var homes: Array[Sprite2D] = []
	var sel: Sprite2D
	var clip: Sprite2D

	func _init() -> void:
		id = "cut"
		bg = "chumava"

	func setup() -> void:
		total = {"jezek": 3, "veverka": 4, "sova": 6}[prof]
		var ids := POOL.duplicate()
		ids.shuffle()
		var left := Games.ground_spots(total, Rect2(220, 380, 560, 470), 190.0 * big)
		var right := Games.ground_spots(total, Rect2(980, 380, 760, 470), 210.0 * big)
		total = mini(left.size(), right.size())
		for i in total:
			var home := UI.sprite("res://assets/atlas/%s.png" % ids[i], right[i], 0.6 * big)
			home.modulate = Color(0.1, 0.1, 0.12, 0.4)
			home.set_meta("id", ids[i])
			_frame(home, Vector2(190, 190))
			homes.append(home)
			var a := UI.sprite("res://assets/atlas/%s.png" % ids[i], left[i], 0.6 * big)
			a.set_meta("id", ids[i])
			a.set_meta("start", left[i])
			_frame(a, Vector2(190, 190))
			animals.append(a)
		set_hint([["key_cut", [KEY_CTRL, KEY_X]], ["key_paste", [KEY_CTRL, KEY_V]]])

	func _frame(s: Sprite2D, sz: Vector2) -> void:
		var f := Frame.new(sz * big)
		f.position = s.position
		s.set_meta("frame", f)
		play.add_child(s)
		play.add_child(f)

	func demo_steps() -> Array:
		return [{"to": animals[0].position, "clicks": 1}, {"to": homes[0].position, "time": 1.4, "clicks": 1}]

	func select(s: Sprite2D) -> void:
		if sel:
			sel.get_meta("frame").set_lit(false)
		sel = s
		if s:
			s.get_meta("frame").set_lit(true)
			Sound.play("pop")

	func on_click(at: Vector2) -> void:
		var s := near(animals.filter(func(a): return a.visible), at, 100.0)
		if not s:
			s = near(homes, at, 100.0)
		select(s)

	func on_key(e: InputEvent) -> void:
		if KeyGames.hit(e, [KEY_CTRL, KEY_X]):
			cut()
		elif KeyGames.hit(e, [KEY_CTRL, KEY_V]):
			paste()
		elif KeyGames.is_shortcut_try(e):
			wrong()

	func cut() -> void:
		if not sel or not sel in animals:
			wrong()
			return
		if clip:
			_back_home(clip)
		clip = sel
		select(null)
		clip.visible = false
		show_clip("atlas/" + str(clip.get_meta("id")))
		Sound.play("whoosh")
		step_done()

	func _back_home(a: Sprite2D) -> void:
		a.position = a.get_meta("start")
		a.visible = true
		UI.pulse(a, 1.2)

	func paste() -> void:
		if not clip or not sel or not sel in homes:
			wrong()
			return
		var home := sel
		if home.get_meta("id") != clip.get_meta("id"):
			mistakes += 1
			wrong()
			Sound.say("ui_wrong_place")
			return
		select(null)
		homes.erase(home)
		animals.erase(clip)
		home.get_meta("frame").queue_free()
		clip.get_meta("frame").queue_free()
		home.modulate = Color.WHITE
		home.scale = Vector2.ZERO
		home.create_tween().tween_property(home, "scale", Vector2.ONE * 0.6 * big, 0.3).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
		clip.queue_free()
		clip = null
		clear_clip()
		Sound.play("plop")
		name_card(home.get_meta("id"), home.position + Vector2(0, -100))
		step_done()
		point()

	func stars() -> int:
		return 3 if mistakes == 0 else (2 if mistakes <= 1 else 1)


# A jay knocks the tidy row over; Ctrl+Z puts things back, newest mess first.
class Undo extends KeyGame:
	const THINGS := ["jablko", "hrib", "siska", "orech", "zalud", "kastan"]
	var items: Array[Sprite2D] = []
	var history: Array = []
	var messed := 0
	var cooldown := 2.0
	var flying := false
	var jay: Sprite2D
	var since := 0.0

	func _init() -> void:
		id = "undo"
		bg = "ves"

	func setup() -> void:
		total = {"jezek": 5, "veverka": 8, "sova": 12}[prof]
		var n := 4 if prof == "jezek" else 6
		for i in n:
			var s := UI.sprite("res://assets/atlas/%s.png" % THINGS[i], Vector2(960 + (i - (n - 1) / 2.0) * 220, 780), 0.6 * big)
			s.set_meta("home", s.position)
			play.add_child(s)
			items.append(s)
		jay = UI.sprite("res://assets/atlas/sojka.png", Vector2(-200, 300), 0.7)
		jay.z_index = 60
		play.add_child(jay)
		set_hint([["key_undo", [KEY_CTRL, KEY_Z]]])

	func tick(delta: float) -> void:
		since += delta
		if flying or not history.is_empty() or messed >= total:
			return
		cooldown -= delta
		if cooldown <= 0.0:
			var wave := 1 if prof == "jezek" else randi_range(1, 2 if prof == "veverka" else 3)
			_fly(mini(wave, total - messed))

	func _fly(count: int) -> void:
		flying = true
		var targets := items.duplicate()
		targets.shuffle()
		targets = targets.slice(0, count)
		var tw := jay.create_tween()
		jay.position = Vector2(-150, randf_range(250, 380))
		jay.flip_h = false
		for t in targets:
			tw.tween_property(jay, "position", t.position + Vector2(0, -90), 0.7 / speed).set_trans(Tween.TRANS_SINE)
			tw.tween_callback(func(): mess(t))
		tw.tween_property(jay, "position", Vector2(2100, 260), 0.8 / speed).set_trans(Tween.TRANS_SINE)
		tw.tween_callback(func():
			flying = false
			cooldown = 1.2 / speed)

	func mess(t: Sprite2D, instant := false) -> void:
		history.append([t, t.position, t.rotation])
		messed += 1
		since = 0.0
		var to := Vector2(clampf(t.position.x + randf_range(-260, 260), 200, 1720), randf_range(400, 900))
		var rot := randf_range(-2.4, 2.4)
		Sound.play("press")
		if instant:
			t.position = to
			t.rotation = rot
			return
		_retween(t)
		var tw := t.create_tween()
		t.set_meta("tween", tw)
		tw.tween_property(t, "position", to, 0.4).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_OUT)
		tw.parallel().tween_property(t, "rotation", rot, 0.4)

	# An undo right after a kick must stop the kick's tween, or it finishes last and drags the thing away again.
	func _retween(t: Sprite2D) -> void:
		if t.has_meta("tween"):
			var old: Tween = t.get_meta("tween")
			if old.is_valid():
				old.kill()

	func on_key(e: InputEvent) -> void:
		if KeyGames.hit(e, [KEY_CTRL, KEY_Z]):
			undo()
		elif KeyGames.is_shortcut_try(e):
			wrong()

	func undo() -> void:
		if history.is_empty():
			wrong()
			return
		var h: Array = history.pop_back()
		var t: Sprite2D = h[0]
		if since > 8.0 / speed:
			mistakes += 1
		_retween(t)
		var tw := t.create_tween()
		t.set_meta("tween", tw)
		tw.tween_property(t, "position", h[1], 0.3).set_trans(Tween.TRANS_BACK)
		tw.parallel().tween_property(t, "rotation", h[2], 0.3)
		step_done()
		point(h[1])

	func stars() -> int:
		return 3 if mistakes == 0 else (2 if mistakes <= 2 else 1)


# Leaves cover the path. Ctrl+A selects them all, Delete blows them away and shows who hid underneath.
class Rake extends KeyGame:
	const KINDS := ["javor", "buk", "dub", "briza"]
	const HIDERS := ["jezek", "jesterka", "zaba", "mravenec", "slepys", "zajic"]
	var leaves: Array[Sprite2D] = []
	var hider: Sprite2D
	var round_n := 0

	func _init() -> void:
		id = "rake"
		bg = "lsten"

	func setup() -> void:
		total = {"jezek": 3, "veverka": 4, "sova": 5}[prof]
		new_round()
		set_hint([["key_selectall", [KEY_CTRL, KEY_A]], ["key_delete", [KEY_DELETE]]])

	func new_round() -> void:
		if done or not leaves.is_empty():
			return
		if hider:
			hider.queue_free()
		var who: String = HIDERS[round_n % HIDERS.size()]
		round_n += 1
		var c := Vector2(randf_range(600, 1300), randf_range(700, 760))
		hider = UI.sprite("res://assets/atlas/%s.png" % who, c, 0.6 * big)
		hider.set_meta("id", who)
		play.add_child(hider)
		var n: int = {"jezek": 12, "veverka": 18, "sova": 24}[prof]
		for i in n:
			var at := c + Vector2(randf_range(-90, 90), randf_range(-70, 70)) if i < 10 else Vector2(randf_range(250, 1670), randf_range(650, 830))
			var l := UI.sprite("res://assets/atlas/%s.png" % KINDS.pick_random(), at, 0.5 * big)
			l.rotation = randf_range(-PI, PI)
			l.z_index = 10
			var f := Frame.new(Vector2(105, 105) * big)
			f.z_index = 0
			l.add_child(f)
			f.scale = Vector2.ONE / l.scale
			f.rotation = 0
			l.set_meta("frame", f)
			l.set_meta("sel", false)
			play.add_child(l)
			leaves.append(l)
			l.scale = Vector2.ZERO
			l.create_tween().tween_property(l, "scale", Vector2.ONE * 0.5 * big, 0.25).set_delay(i * 0.03)

	func demo_steps() -> Array:
		return []

	func _mark(l: Sprite2D, v: bool) -> void:
		l.set_meta("sel", v)
		l.get_meta("frame").set_lit(v)

	func on_click(at: Vector2) -> void:
		for l in leaves:
			_mark(l, false)
		var hitl := near(leaves, at, 70.0)
		if hitl:
			_mark(hitl, true)
			Sound.play("pop")

	func on_key(e: InputEvent) -> void:
		if KeyGames.hit(e, [KEY_CTRL, KEY_A]):
			select_all()
		elif KeyGames.hit(e, [KEY_DELETE]):
			delete()
		elif KeyGames.is_shortcut_try(e):
			wrong()

	func select_all() -> void:
		if leaves.is_empty():
			return
		for l in leaves:
			_mark(l, true)
		Sound.play("chime")
		step_done()

	func delete() -> void:
		var picked := leaves.filter(func(l): return l.get_meta("sel"))
		if picked.is_empty():
			mistakes += 1
			wrong()
			return
		Sound.play("whoosh")
		for l in picked:
			leaves.erase(l)
			var tw: Tween = l.create_tween()
			tw.tween_property(l, "position", l.position + Vector2(randf_range(400, 900), randf_range(-500, -200)), 0.6).set_trans(Tween.TRANS_SINE)
			tw.parallel().tween_property(l, "modulate:a", 0.0, 0.6)
			tw.tween_callback(l.queue_free)
		step_done()
		if leaves.is_empty():
			UI.pulse(hider, 1.3)
			name_card(hider.get_meta("id"), hider.position + Vector2(0, -110))
			point(hider.position)
			if got < total:
				var tw := create_tween()
				tw.tween_interval(1.6)
				tw.tween_callback(new_round)

	func stars() -> int:
		return 3 if mistakes == 0 else (2 if mistakes <= 2 else 1)


# A card shows what should happen; press the shortcut. The downloaded game also asks for the
# shortcuts a browser would keep for itself.
class Drill extends KeyGame:
	var deck: Array = []
	var current := ""
	var card := Node2D.new()
	var away := false

	func _init() -> void:
		id = "drill"
		bg = "vrch"

	static func pool(p: String, web: bool) -> Array:
		if p == "jezek":
			return EASY.duplicate()
		return SAFE + ([] if web else DESKTOP)

	func setup() -> void:
		total = {"jezek": 6, "veverka": 10, "sova": 14}[prof]
		card.position = Vector2(960, 520)
		play.add_child(card)
		if not OS.has_feature("web"):
			get_tree().auto_accept_quit = false
		next_card()

	func _exit_tree() -> void:
		get_tree().auto_accept_quit = true

	func next_card() -> void:
		if deck.is_empty():
			deck = pool(prof, OS.has_feature("web"))
			deck.shuffle()
			if deck[0] == current and deck.size() > 1:
				deck.push_back(deck.pop_front())
		current = deck.pop_front()
		away = false
		for c in card.get_children():
			c.queue_free()
		var p := UI.panel()
		p.custom_minimum_size = Vector2(620, 460)
		p.position = Vector2(-310, -250)
		card.add_child(p)
		card.add_child(KeyGames.sprite_fit(SHORTCUTS[current][1], Vector2(0, -80), 230))
		var w := UI.label(Text.t("key_" + current), 76, UI.INK, 12)
		w.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		w.custom_minimum_size = Vector2(620, 0)
		w.position = Vector2(-310, 70)
		card.add_child(w)
		if current in ["switch", "close"]:
			var note := UI.label(Text.t("note_" + current), 30, UI.SOFT)
			note.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
			note.custom_minimum_size = Vector2(900, 0)
			note.position = Vector2(-450, 230)
			card.add_child(note)
			var skip := UI.tbutton("skip", 34, UI.GREEN)
			skip.pressed.connect(func():
				current = ""
				next_card())
			skip.position = Vector2(340, 150)
			card.add_child(skip)
		set_hint([["key_" + current, SHORTCUTS[current][0]]])
		card.scale = Vector2(0.6, 0.6)
		card.create_tween().tween_property(card, "scale", Vector2.ONE, 0.25).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
		Sound.say("act_" + current)

	func on_key(e: InputEvent) -> void:
		if KeyGames.hit(e, SHORTCUTS[current][0]):
			right()
		elif KeyGames.is_shortcut_try(e):
			mistakes += 1
			wrong()
			var tw := card.create_tween()
			for i in 4:
				tw.tween_property(card, "position:x", 960.0 + (18.0 if i % 2 == 0 else -18.0), 0.05)
			tw.tween_property(card, "position:x", 960.0, 0.05)

	func right() -> void:
		step_done()
		point(Vector2(960, 300))
		if got < total:
			next_card()

	func _notification(what: int) -> void:
		if done or current == "":
			if what == NOTIFICATION_WM_CLOSE_REQUEST:
				get_tree().quit()
			return
		match what:
			NOTIFICATION_APPLICATION_FOCUS_OUT:
				away = current == "switch"
			NOTIFICATION_APPLICATION_FOCUS_IN:
				if away and current == "switch":
					right()
			NOTIFICATION_WM_CLOSE_REQUEST:
				if current == "close":
					right()
				else:
					get_tree().quit()

	func stars() -> int:
		return 3 if mistakes <= 1 else (2 if mistakes <= 4 else 1)
