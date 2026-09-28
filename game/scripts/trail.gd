class_name Trail
extends Node2D

signal goto(screen: String, arg: String)

const RANGER := Vector2(170, 1062)
const JOEY := Vector2(390, 1064)
const FABIAN := Vector2(1300, 1025)
const FABIAN_KEYBOARD := Vector2(1650, 1025)
const HUD := {"photo": Vector2(1520, 70), "basket": Vector2(1670, 70), "herbarium": Vector2(1820, 70)}
const HUD_ICON := {"photo": "camera", "basket": "basket", "herbarium": "herbarium"}
const WALK_TIME := 2.4
const LINE_TIME := 4.5

var n := 1
var data := {}
var profile_id := ""
var profile := {}
var typing := Typing.new()
var station := 0
var wave: Wave
var stage: Node2D
var critters: Node2D
var hud := Node2D.new()
var fx := Node2D.new()
var ranger := Sprite2D.new()
var joey := Sprite2D.new()
var sun := Sprite2D.new()
var keyboard: OnScreenKeyboard
var station_label: Control
var counters := {}
var paws: Array[Sprite2D] = []
var spots: Array = []
var busy := {}
var cooldown := 1.2
var flying := 0
var phase := "station"
var appeared := 0
var caught := 0
var new_ids: Array = []
var finale: Critter.Finale
var fabian: Sprite2D
var sun_p := 0.0
var fabian_at := FABIAN
var _missed := {}
var _rare_seen := []
var _enter_action := Callable()
var _dialog: Control
var _lines := []
var _line_time := 0.0
var _after_lines := Callable()
var _ranger_timer := 0.0
var _joey_busy := false
var _lit_paws := 0


func _init(trail_no := 1) -> void:
	n = trail_no


func _ready() -> void:
	data = Atlas.trail(n)
	profile_id = Save.profile_id()
	profile = Config.PROFILES[profile_id]
	typing.lenient = profile.lenient
	Atlas.reset()
	spots = Config.SPOTS_KEYBOARD if profile.keyboard else Config.SPOTS
	fabian_at = FABIAN_KEYBOARD if profile.keyboard else FABIAN
	sun.texture = UI.tex("res://assets/ui/sun.png")
	sun.z_index = 5
	sun.scale = Vector2(1.1, 1.1)
	add_child(sun)
	fx.z_index = 100
	add_child(fx)
	ranger.texture = _ranger_tex("happy")
	ranger.z_index = 30
	add_child(ranger)
	_place_standing(ranger, RANGER, 0.95)
	joey.texture = UI.tex("res://assets/chars/joey_stand.png")
	joey.z_index = 31
	add_child(joey)
	_place_standing(joey, JOEY, 0.8)
	if profile.keyboard:
		keyboard = OnScreenKeyboard.new()
		keyboard.position = Vector2(960, 836)
		keyboard.z_index = 150
		keyboard.typed.connect(_on_char)
		add_child(keyboard)
	_build_hud()
	wave = Wave.new(profile)
	_start_station(0, true)
	Sound.start_ambience()


func _ranger_tex(mood: String) -> Texture2D:
	return UI.tex("res://assets/chars/%s_%s.png" % [Save.look(), mood])


func _place_standing(sp: Sprite2D, feet: Vector2, s: float) -> void:
	sp.centered = false
	sp.scale = Vector2(s, s)
	sp.offset = Vector2(-sp.texture.get_width() / 2.0, -sp.texture.get_height())
	sp.position = feet


func _set_ranger(mood: String, hold := 1.2) -> void:
	ranger.texture = _ranger_tex(mood)
	_place_standing(ranger, RANGER, 0.95)
	_ranger_timer = hold


func _build_hud() -> void:
	hud.z_index = 200
	add_child(hud)
	for tab in Config.TABS:
		var icon := UI.sprite("res://assets/ui/%s.png" % HUD_ICON[tab], HUD[tab], 0.6)
		hud.add_child(icon)
		var l := UI.label("0", 44, UI.INK, 12)
		l.position = HUD[tab] + Vector2(22, 10)
		hud.add_child(l)
		counters[tab] = l
	var map_b := UI.tbutton("map", 34, UI.GREEN)
	map_b.pressed.connect(func(): goto.emit("map", ""))
	map_b.position = Vector2(1180, 24)
	hud.add_child(map_b)
	var tray := Panel.new()
	tray.add_theme_stylebox_override("panel", UI.box(Color(UI.PAPER, 0.85), 18, 4))
	tray.position = Vector2(30, 138)
	tray.size = Vector2(Config.PAWS_FOR_RARE * 64 + 70, 76)
	hud.add_child(tray)
	var head := UI.sprite("res://assets/chars/joey_stand.png", Vector2(62, 176), 0.22)
	hud.add_child(head)
	for i in Config.PAWS_FOR_RARE:
		var p := UI.sprite("res://assets/ui/paw.png", Vector2(128 + i * 64, 176), 0.5)
		p.modulate = Color(1, 1, 1, 0.22)
		hud.add_child(p)
		paws.append(p)


func _show_station_name(primary: String, secondary: String) -> void:
	if station_label:
		station_label.queue_free()
	var v := UI.bilabel(primary, secondary, 60, UI.INK, 14)
	for c in v.get_children():
		c.horizontal_alignment = HORIZONTAL_ALIGNMENT_LEFT
	hud.add_child(v)
	v.reset_size()
	v.position = Vector2(40, 18)
	station_label = v


func _make_stage(bg: String, cover_kinds: Array) -> Node2D:
	var s := Node2D.new()
	s.add_child(UI.backdrop("res://assets/bg/%s.png" % bg))
	var cr := Node2D.new()
	cr.z_index = 10
	s.add_child(cr)
	for i in cover_kinds.size():
		if i >= spots.size():
			break
		var c := UI.standing("res://assets/covers/%s.png" % cover_kinds[i], spots[i], 0.75)
		c.z_index = 20
		c.flip_h = i % 2 == 1
		s.add_child(c)
	return s


func _start_station(i: int, first := false) -> void:
	station = i
	var st: Dictionary = data.stations[i]
	var paws_left := wave.paws
	wave = Wave.new(profile)
	wave.paws = paws_left
	busy.clear()
	if first:
		stage = _make_stage(st.id, Config.covers_for(st.id))
		add_child(stage)
		move_child(stage, 0)
		critters = stage.get_child(1)
	_show_station_name("%s" % st[Save.lang()], st[Text.other_lang()])
	cooldown = 1.5
	phase = "station"


func active() -> Array:
	var out := []
	if critters == null:
		return out
	for c in critters.get_children():
		if c is Critter and c.state in [Critter.State.RISING, Critter.State.SHOWN]:
			out.append(c)
	return out


func _process(delta: float) -> void:
	_update_sun(delta)
	if _ranger_timer > 0.0:
		_ranger_timer -= delta
		if _ranger_timer <= 0.0 and phase != "walk":
			ranger.texture = _ranger_tex("happy")
			_place_standing(ranger, RANGER, 0.95)
	if _dialog:
		_line_time += delta
		if _line_time > LINE_TIME and not Sound.speaking():
			_next_line()
	if phase == "station":
		cooldown -= delta
		if wave.done() and active().is_empty() and flying == 0 and busy.is_empty():
			_leave_station()
		elif wave.rare_due and not _joey_busy:
			_joey_fetch()
		elif cooldown <= 0.0 and wave.wants_spawn(active().size()) and not wave.rare_due:
			spawn()
	if keyboard:
		keyboard.highlight(_hint_letter())


func _update_sun(delta: float) -> void:
	var stations: int = data.stations.size()
	var target := 1.0
	if phase in ["station", "walk"]:
		target = (station + wave.progress()) / float(stations + 1)
	sun_p = move_toward(sun_p, target, delta * 0.08)
	sun.position = Vector2(lerpf(280.0, 1640.0, sun_p), 330.0 - sin(PI * lerpf(0.08, 0.92, sun_p)) * 230.0)
	var tint := Color(1, 1, 1).lerp(Color(1.0, 0.82, 0.68), smoothstep(0.6, 1.0, sun_p))
	for c in get_children():
		if c is Node2D and c.z_index <= 10 and c != sun and c != fx:
			c.modulate = tint
	sun.modulate = Color(1, 1, 1).lerp(Color(1.0, 0.6, 0.35), smoothstep(0.65, 1.0, sun_p))


func _free_spots() -> Array:
	var free := []
	for i in spots.size():
		if not busy.has(i):
			free.append(i)
	return free


func spawn(rare_id := "", forced_spot := -1) -> Critter:
	var free := _free_spots()
	if forced_spot >= 0:
		free = [forced_spot]
	if free.is_empty():
		return null
	var avoid := []
	var on_screen := []
	for c in active():
		avoid.append(Typing.fold(c.word[0]))
		on_screen.append(c.id)
	var rare := rare_id != ""
	var id := rare_id
	if not rare:
		id = Atlas.pick(n, station, profile_id, avoid)
		if id in on_screen:
			id = Atlas.pick(n, station, profile_id, avoid)
	if id == "":
		return null
	var word := Atlas.word_for(id, profile_id)
	var spot_i: int = free.pick_random()
	var time: float = profile.peek_time * (1.0 + 0.05 * maxi(0, word.length() - 6)) * (1.4 if rare else 1.0)
	var c := Critter.new()
	c.setup(id, word, time, spot_i, rare)
	c.position = spots[spot_i]
	c.speed = Save.speed()
	c.completed.connect(_on_completed)
	c.hid.connect(_on_hid)
	c.missed.connect(func(x): _missed[x] = true)
	critters.add_child(c)
	typing.add(c)
	busy[spot_i] = c
	wave.on_spawn(rare)
	appeared += 1
	cooldown = 1.7
	Sound.play("sniff")
	if rare:
		_sparkle(c.position + Vector2(0, -260))
	if profile.speak:
		Sound.say("name_" + id)
		Sound.say_after(Sound.letter_key(word[0]), Save.lang(), 1.3)
	return c


func _hint_letter() -> String:
	if typing.locked:
		return typing.locked.word[typing.locked.progress]
	if finale and finale.progress == 0 and finale in typing.targets:
		return finale.word[0]
	var best: Critter = null
	for c in active():
		if c.is_targetable() and (best == null or c.t > best.t):
			best = c
	return best.word[0] if best else ""


func _unhandled_input(event: InputEvent) -> void:
	var click: bool = event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT
	if _dialog and (click or event is InputEventKey and event.pressed and event.keycode in [KEY_ENTER, KEY_KP_ENTER, KEY_SPACE]):
		get_viewport().set_input_as_handled()
		if _line_time > 0.4:
			_next_line()
		return
	if not (event is InputEventKey) or not event.pressed:
		return
	get_viewport().set_input_as_handled()
	if phase == "over":
		if event.keycode in [KEY_ENTER, KEY_KP_ENTER] and _enter_action.is_valid():
			_enter_action.call()
		return
	if event.keycode in [KEY_ESCAPE, KEY_BACKSPACE]:
		typing.release()
		return
	_on_char(Typing.char_from_event(event))


func _on_char(ch: String) -> void:
	if ch.is_empty() or phase in ["over", "walk"] or _dialog:
		return
	match typing.handle(ch):
		Typing.Result.MISS:
			Sound.play("boing")
			if keyboard:
				keyboard.flash(ch)
		Typing.Result.LOCKED:
			Sound.play("lock")
			_speak_next()
		Typing.Result.ADVANCED:
			_speak_next()


func _speak_next() -> void:
	if profile.speak and typing.locked:
		Sound.say(Sound.letter_key(typing.locked.word[typing.locked.progress]))


func _on_completed(c: Critter) -> void:
	var clean := not _missed.has(c)
	_missed.erase(c)
	busy.erase(c.spot)
	wave.on_resolved(true)
	caught += 1
	Save.set_speed(wave.speed_after(Save.speed(), true, clean))
	_set_ranger("cheer")
	var e := Atlas.entry(c.id)
	var fresh := Save.add_found(c.id)
	if fresh:
		new_ids.append(c.id)
	_show_translation(c, fresh)
	Sound.say_after("name_" + c.id, Save.lang(), 0.3)
	var tab: String = Config.TAB_OF[e.cat]
	match e.cat:
		"animal", "poison":
			_fly_photo(c, e.cat == "poison")
		"plant":
			_fly_press(c)
		_:
			_fly_basket(c)
	if c.rare:
		_joey_home()
	elif wave.paws_after(true, clean) and not _joey_busy and not wave.rare_due and Atlas.pick_rare(n, _rare_seen) != "":
		wave.add_rare()
	_update_paws()


func _on_hid(c: Critter) -> void:
	typing.remove(c)
	_missed.erase(c)
	busy.erase(c.spot)
	wave.on_resolved(false)
	wave.paws_after(false, false)
	Save.set_speed(wave.speed_after(Save.speed(), false, false))
	if c.rare:
		_joey_home()
	_update_paws()


func _update_paws() -> void:
	var lit := Config.PAWS_FOR_RARE if wave.rare_due or _joey_busy else wave.paws
	for i in paws.size():
		var on := i < lit
		paws[i].modulate = Color(1, 1, 1, 1.0) if on else Color(1, 1, 1, 0.22)
		if on and i >= _lit_paws:
			UI.pulse(paws[i], 1.5)
			Sound.play("pop")
	_lit_paws = lit


func _joey_walk(to: Vector2, s: float, dur: float) -> Tween:
	joey.flip_h = to.x < joey.position.x
	var tw := create_tween()
	tw.tween_property(joey, "position", to, dur).set_trans(Tween.TRANS_SINE)
	tw.parallel().tween_property(joey, "scale", Vector2(s, s), dur)
	var hop := create_tween().set_loops(int(dur / 0.16))
	hop.tween_property(joey, "offset:y", joey.offset.y - 14, 0.08)
	hop.tween_property(joey, "offset:y", joey.offset.y, 0.08)
	return tw


func _joey_fetch() -> void:
	var free := _free_spots()
	var id := Atlas.pick_rare(n, _rare_seen)
	if free.is_empty() or id == "":
		if id == "":
			wave.rare_due = false
			wave.total -= 1
		return
	_joey_busy = true
	_rare_seen.append(id)
	var spot: int = free.pick_random()
	busy[spot] = true
	var at: Vector2 = spots[spot]
	for p in paws:
		UI.pulse(p, 1.6)
	Sound.play("chime")
	Sound.play("bark")
	joey.texture = UI.tex("res://assets/chars/joey_bark.png")
	var tw := _joey_walk(at + Vector2(-190 if at.x > 700 else 190, 25), 0.7, 1.0)
	tw.tween_callback(func():
		joey.flip_h = at.x < joey.position.x
		joey.texture = UI.tex("res://assets/chars/joey_sniff.png")
		Sound.play("sniff"))
	tw.tween_interval(0.9)
	tw.tween_callback(func():
		joey.texture = UI.tex("res://assets/chars/joey_bark.png")
		Sound.play("bark")
		busy.erase(spot)
		if phase == "station":
			spawn(id, spot))


func _joey_home() -> void:
	if not _joey_busy:
		return
	joey.texture = UI.tex("res://assets/chars/joey_stand.png")
	var tw := _joey_walk(JOEY, 0.8, 0.9)
	tw.tween_callback(func():
		joey.flip_h = false
		_joey_busy = false
		_update_paws())


func _land(tab: String, sp: Node2D) -> void:
	sp.queue_free()
	flying -= 1
	var l: Label = counters[tab]
	l.text = str(int(l.text) + 1)
	UI.pulse(l)


func _fly_to(sp: Node2D, tab: String, dur := 0.8, delay := 0.0) -> void:
	fx.add_child(sp)
	var tw := sp.create_tween()
	if delay > 0.0:
		tw.tween_interval(delay)
	tw.tween_property(sp, "position", HUD[tab], dur).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN)
	tw.parallel().tween_property(sp, "scale", sp.scale * 0.3, dur)
	tw.tween_callback(func(): _land(tab, sp))


func _fly_photo(c: Critter, poison: bool) -> void:
	flying += 1
	Sound.play("shutter")
	var flash := ColorRect.new()
	flash.color = Color(1, 1, 1, 0.8)
	flash.size = Vector2(1920, 1080)
	flash.mouse_filter = Control.MOUSE_FILTER_IGNORE
	fx.add_child(flash)
	flash.create_tween().tween_property(flash, "color:a", 0.0, 0.35)
	flash.create_tween().tween_callback(flash.queue_free).set_delay(0.4)
	var card := Node2D.new()
	var frame := Panel.new()
	var sb := UI.box(UI.PAPER, 8, 8, UI.RED if poison else Color("d8cfbd"))
	frame.add_theme_stylebox_override("panel", sb)
	frame.size = Vector2(230, 260)
	frame.position = Vector2(-115, -130)
	card.add_child(frame)
	card.position = c.picture_global()
	var pic := c.take_picture()
	pic.position = Vector2(0, -18)
	pic.scale = Vector2(0.8, 0.8)
	card.add_child(pic)
	if poison:
		Sound.say("ui_dont_touch")
		_float_text(Text.t("dont_touch"), Text.o("dont_touch"), c.position + Vector2(0, -330), UI.RED)
	_fly_to(card, "photo", 0.9, 1.0 if poison else 0.45)
	c.vanish()


func _fly_basket(c: Critter) -> void:
	flying += 1
	var sp := c.take_picture()
	Sound.play("plop")
	_fly_to(sp, "basket", 0.8, 0.25)
	c.vanish()


func _fly_press(c: Critter) -> void:
	flying += 1
	var sp := c.take_picture()
	fx.add_child(sp)
	Sound.play("press")
	var tw := sp.create_tween()
	tw.tween_property(sp, "scale", Vector2(1.15, 0.2), 0.25)
	tw.tween_property(sp, "scale", Vector2(0.9, 0.9), 0.2)
	tw.tween_callback(func():
		fx.remove_child(sp)
		_fly_to(sp, "herbarium", 0.7))
	c.vanish()


func _sparkle(at: Vector2) -> void:
	for i in 8:
		var s := UI.label("✦", 48, Color("f6c744"), 8)
		s.position = at + Vector2(randf_range(-110, 110), randf_range(-60, 60))
		fx.add_child(s)
		var tw := s.create_tween()
		tw.tween_property(s, "modulate:a", 0.0, 1.2).set_delay(randf_range(0.2, 0.6))
		tw.tween_callback(s.queue_free)
	Sound.play("chime")


func _float_text(primary: String, secondary: String, at: Vector2, colour: Color, rise := 70.0, hold := 2.2) -> Node2D:
	var card := Node2D.new()
	card.z_index = 300
	var v := UI.bilabel(primary, secondary, 46, colour, 12)
	add_child(card)
	UI.centered(card, v, Vector2.ZERO)
	var half := v.size.x / 2 + 20
	card.position = Vector2(clampf(at.x, half, 1920 - half), maxf(at.y, v.size.y / 2 + 10))
	var tw := card.create_tween()
	tw.tween_property(card, "position:y", card.position.y - rise, hold + 0.6).set_trans(Tween.TRANS_SINE)
	tw.parallel().tween_property(card, "modulate:a", 0.0, 0.7).set_delay(hold)
	tw.tween_callback(card.queue_free)
	return card


func _show_translation(c: Critter, fresh: bool) -> void:
	var names := Atlas.translation_pair(c.id, profile_id)
	var card := Node2D.new()
	card.z_index = 300
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", -6)
	if fresh:
		v.add_child(UI.bilabel(Text.t("new"), Text.o("new"), 40, Color("e08a1e"), 10))
	v.add_child(UI.label(names[0], 52, UI.DONE, 14))
	add_child(card)
	UI.centered(card, v, Vector2.ZERO)
	var at := c.position + Vector2(0, -360 - (c.spot % 2) * 90)
	var half := v.size.x / 2 + 20
	card.position = Vector2(clampf(at.x, half, 1920 - half), maxf(at.y, v.size.y / 2 + 10))
	if fresh:
		Sound.play("chime")
	var tw := card.create_tween()
	tw.tween_property(card, "position:y", card.position.y - 60, 2.8).set_trans(Tween.TRANS_SINE)
	tw.parallel().tween_property(card, "modulate:a", 0.0, 0.8).set_delay(2.0)
	tw.tween_callback(card.queue_free)


func _leave_station() -> void:
	typing.locked = null
	typing.targets.clear()
	if station + 1 < data.stations.size():
		var next: Dictionary = data.stations[station + 1]
		_walk(next.id, Config.covers_for(next.id), func(): _start_station(station + 1))
	else:
		_walk(data.finale.id, [], _start_finale)


func _walk(bg: String, cover_kinds: Array, then: Callable) -> void:
	phase = "walk"
	station_label.visible = false
	ranger.texture = _ranger_tex("walk")
	_place_standing(ranger, RANGER, 0.95)
	var next := _make_stage(bg, cover_kinds)
	next.position.x = 1920
	add_child(next)
	move_child(next, 0)
	var old := stage
	stage = next
	critters = next.get_child(1)
	var tw := create_tween().set_parallel()
	tw.tween_property(old, "position:x", -1920.0, WALK_TIME).set_trans(Tween.TRANS_SINE)
	tw.tween_property(next, "position:x", 0.0, WALK_TIME).set_trans(Tween.TRANS_SINE)
	var hop := create_tween().set_loops(6)
	hop.tween_property(ranger, "position:y", RANGER.y - 14, WALK_TIME / 12)
	hop.tween_property(ranger, "position:y", RANGER.y, WALK_TIME / 12)
	var hop2 := create_tween().set_loops(8)
	hop2.tween_property(joey, "position:y", JOEY.y - 10, WALK_TIME / 16)
	hop2.tween_property(joey, "position:y", JOEY.y, WALK_TIME / 16)
	Sound.play("whoosh")
	tw.chain().tween_callback(func():
		old.queue_free()
		ranger.texture = _ranger_tex("happy")
		_place_standing(ranger, RANGER, 0.95)
		station_label.visible = true
		then.call())


func _start_finale() -> void:
	phase = "finale"
	var f: Dictionary = data.finale
	_show_station_name(f[Save.lang()], f[Text.other_lang()])
	fabian = UI.standing("res://assets/chars/fabian_stand.png", fabian_at, 1.0)
	fabian.z_index = 30
	fabian.modulate.a = 0.0
	add_child(fabian)
	var tw := fabian.create_tween()
	tw.tween_property(fabian, "modulate:a", 1.0, 0.8)
	_sparkle(fabian_at + Vector2(0, -300))
	var lines := []
	for i in data.fabian.size():
		lines.append({"pair": data.fabian[i], "voice": "fabian_%d_%d" % [n, i]})
	_say_lines(lines, _show_finale_target)


func _say_lines(lines: Array, then: Callable) -> void:
	_lines = lines.duplicate()
	_after_lines = then
	_next_line()


func _next_line() -> void:
	if _dialog:
		_dialog.queue_free()
		_dialog = null
	if _lines.is_empty():
		var then := _after_lines
		_after_lines = Callable()
		if then.is_valid():
			then.call()
		return
	var line: Dictionary = _lines.pop_front()
	var pair: Dictionary = line.pair
	_line_time = 0.0
	if fabian:
		fabian.texture = UI.tex("res://assets/chars/fabian_talk.png")
	var p := UI.panel()
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 6)
	var a := UI.label(pair[Save.lang()], 46)
	var lines := [a]
	if UI.BILINGUAL:
		lines.append(UI.label(pair[Text.other_lang()], 32, UI.SOFT))
	for l in lines:
		l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		l.custom_minimum_size = Vector2(760, 0)
		v.add_child(l)
	p.add_child(v)
	p.z_index = 250
	p.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(p)
	p.reset_size()
	p.position = Vector2(fabian_at.x - p.size.x - 150, 360 - p.size.y / 2)
	_dialog = p
	Sound.say(line.voice)


func _show_finale_target() -> void:
	if fabian:
		fabian.texture = UI.tex("res://assets/chars/fabian_stand.png")
	var word := Atlas.target_for(n, profile_id)
	finale = Critter.Finale.new(word)
	finale.completed.connect(_on_finale_done)
	add_child(finale)
	var half := finale.plaque.box().size.x / 2
	finale.position = Vector2(clampf(fabian_at.x, half + 20, 1900 - half), fabian_at.y - fabian.texture.get_height() - 110)
	typing.add(finale)
	var key := "press_letter" if profile.letters else "type_sign"
	var hint := UI.label(Text.t(key), 44, UI.INK, 14)
	finale.add_child(hint)
	hint.reset_size()
	hint.position = Vector2(-hint.size.x / 2, -finale.plaque.box().size.y / 2 - hint.size.y - 10)
	hint.position.x = clampf(hint.position.x, 10 - finale.position.x, 1910 - finale.position.x - hint.size.x)
	var tw := finale.create_tween().set_loops()
	tw.tween_property(finale, "scale", Vector2(1.08, 1.08), 0.5).set_trans(Tween.TRANS_SINE)
	tw.tween_property(finale, "scale", Vector2.ONE, 0.5).set_trans(Tween.TRANS_SINE)
	Sound.say("ui_" + key)
	if profile.speak:
		Sound.say_after(Sound.letter_key(word[0]), Save.lang(), 2.2)


func _on_finale_done(_f) -> void:
	Sound.play("fanfare")
	_set_ranger("cheer", 999.0)
	fabian.texture = UI.tex("res://assets/chars/fabian_wave.png")
	var other := Atlas.target_for(n, profile_id, Text.other_lang())
	var names := [finale.word, other]
	if profile.letters:
		names = [data.target[Save.lang()], data.target[Text.other_lang()]]
	_float_text(names[0], "", finale.position + Vector2(0, -40), UI.DONE, 60, 2.6)
	finale.queue_free()
	finale = null
	_say_lines([{"pair": data.thanks, "voice": "thanks_%d" % n}], _give_keepsake)


func _give_keepsake() -> void:
	fabian.texture = UI.tex("res://assets/chars/fabian_wave.png")
	var k := UI.sprite("res://assets/keepsakes/%s.png" % data.keepsake.id, fabian_at + Vector2(-60, -200), 0.6)
	k.z_index = 320
	add_child(k)
	Sound.play("jingle")
	var tw := k.create_tween()
	tw.tween_property(k, "position", Vector2(960, 420), 0.9).set_trans(Tween.TRANS_BACK)
	tw.parallel().tween_property(k, "scale", Vector2(1.6, 1.6), 0.9)
	tw.tween_interval(0.6)
	tw.tween_callback(func():
		k.queue_free()
		_summary())


func _overlay() -> Node2D:
	phase = "over"
	typing.locked = null
	typing.targets.clear()
	var o := Node2D.new()
	o.z_index = 400
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.35)
	dim.size = Vector2(4000, 3000)
	dim.position = Vector2(-1000, -1000)
	o.add_child(dim)
	add_child(o)
	return o


func _texrect(path: String, px: float) -> TextureRect:
	var r := TextureRect.new()
	r.texture = UI.tex(path)
	r.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	r.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	r.custom_minimum_size = Vector2(px, px)
	return r


func _summary() -> void:
	var cones := Config.cones_for(caught, appeared)
	var keepsake: Dictionary = data.keepsake
	var next := Save.finish_trail(n, cones, keepsake.id)
	Sound.say("ui_done")
	_enter_action = func(): goto.emit("map", "")
	var o := _overlay()
	var p := UI.panel()
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 14)
	p.add_child(v)
	v.add_child(UI.tlabel("trail_done", 72))
	v.add_child(UI.bilabel(Text.t("found") % [caught, appeared], Text.o("found") % [caught, appeared], 44))
	var cone_row := HBoxContainer.new()
	cone_row.alignment = BoxContainer.ALIGNMENT_CENTER
	for i in 3:
		cone_row.add_child(_texrect("res://assets/ui/%s.png" % ("cone_icon" if i < cones else "cone_empty"), 90))
	v.add_child(cone_row)
	if not new_ids.is_empty():
		v.add_child(UI.bilabel(Text.t("new_count") % new_ids.size(), Text.o("new_count") % new_ids.size(), 38, Color("e08a1e")))
		var row := HBoxContainer.new()
		row.alignment = BoxContainer.ALIGNMENT_CENTER
		for id in new_ids.slice(0, 9):
			row.add_child(_texrect("res://assets/atlas/%s.png" % id, 90))
		v.add_child(row)
	var gift := HBoxContainer.new()
	gift.alignment = BoxContainer.ALIGNMENT_CENTER
	gift.add_child(_texrect("res://assets/keepsakes/%s.png" % keepsake.id, 100))
	gift.add_child(UI.bilabel(Text.t("gift") % keepsake[Save.lang()], Text.o("gift") % keepsake[Text.other_lang()], 40))
	v.add_child(gift)
	if next > 0:
		var nt: Dictionary = Atlas.trail(next).name
		v.add_child(UI.bilabel(Text.t("next_trail") % nt[Save.lang()], Text.o("next_trail") % nt[Text.other_lang()], 38, UI.DONE))
	else:
		v.add_child(UI.tlabel("all_done", 40, UI.DONE))
	var h := HBoxContainer.new()
	h.alignment = BoxContainer.ALIGNMENT_CENTER
	h.add_theme_constant_override("separation", 30)
	var map_b := UI.tbutton("map", 52)
	map_b.pressed.connect(func(): goto.emit("map", ""))
	var atlas_b := UI.tbutton("atlas", 44, UI.GREEN)
	atlas_b.pressed.connect(func(): goto.emit("atlas", ""))
	var again := UI.tbutton("again", 44, UI.GREEN)
	again.pressed.connect(func(): goto.emit("trail", str(n)))
	h.add_child(map_b)
	h.add_child(atlas_b)
	h.add_child(again)
	v.add_child(h)
	UI.centered(o, p)
