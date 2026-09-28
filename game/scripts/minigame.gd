class_name MiniGame
extends Node2D

signal goto(screen: String, arg: String)

const SIZE := {"jezek": 1.5, "veverka": 1.0, "sova": 0.8}
const SPEED := {"jezek": 0.6, "veverka": 1.0, "sova": 1.3}
const COUNT := {"jezek": 0, "veverka": 1, "sova": 2}

var id := ""
var bg := ""
var prof := "veverka"
var big := 1.0
var speed := 1.0
var total := 10
var got := 0
var mistakes := 0
var elapsed := 0.0
var done := false
var play := Node2D.new()
var hud := Node2D.new()
var counter: Label
var ghost: Sprite2D
var _enter := Callable()


func _ready() -> void:
	prof = Save.profile_id()
	big = SIZE[prof]
	speed = SPEED[prof]
	add_child(UI.backdrop("res://assets/bg/%s.png" % bg))
	add_child(play)
	hud.z_index = 200
	add_child(hud)
	var title := UI.label(Text.t("game_" + id), 56, UI.INK, 14)
	title.position = Vector2(40, 18)
	hud.add_child(title)
	var how := UI.label(Text.t("how_" + id), 38, UI.INK, 12)
	how.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	how.custom_minimum_size = Vector2(1100, 0)
	hud.add_child(how)
	how.reset_size()
	how.position = Vector2(960 - how.size.x / 2, 100)
	counter = UI.label("0 / %d" % total, 52, UI.INK, 14)
	counter.position = Vector2(1640, 20)
	hud.add_child(counter)
	var back := UI.tbutton("back", 40, UI.GREEN)
	back.pressed.connect(func(): goto.emit("games", ""))
	back.position = Vector2(40, 950)
	hud.add_child(back)
	setup()
	counter.text = "%d / %d" % [got, total]
	Sound.say("intro_" + id)
	if prof == "jezek" or Save.game_cones(id) == 0:
		_demo.call_deferred()


func setup() -> void:
	pass


func demo_steps() -> Array:
	return []


func _process(delta: float) -> void:
	if not done:
		elapsed += delta
		tick(delta)


func tick(_delta: float) -> void:
	pass


func point(at := Vector2.ZERO) -> void:
	got += 1
	counter.text = "%d / %d" % [got, total]
	UI.pulse(counter)
	Sound.play("chime")
	if at != Vector2.ZERO:
		sparkle(at)
	if got >= total:
		finish.call_deferred()


func sparkle(at: Vector2) -> void:
	for i in 6:
		var s := UI.label("✦", 44, Color("f6c744"), 8)
		s.position = at + Vector2(randf_range(-80, 80), randf_range(-60, 40))
		s.z_index = 150
		add_child(s)
		var tw := s.create_tween()
		tw.tween_property(s, "modulate:a", 0.0, 0.9).set_delay(randf_range(0.1, 0.4))
		tw.tween_callback(s.queue_free)


func name_card(entry_id: String, at: Vector2) -> void:
	var l := UI.label(Atlas.name_of(entry_id), 48, UI.DONE, 14)
	l.z_index = 160
	add_child(l)
	l.reset_size()
	l.position = Vector2(clampf(at.x - l.size.x / 2, 10, 1910 - l.size.x), at.y - l.size.y)
	var tw := l.create_tween()
	tw.tween_property(l, "position:y", l.position.y - 60, 1.8)
	tw.parallel().tween_property(l, "modulate:a", 0.0, 0.6).set_delay(1.2)
	tw.tween_callback(l.queue_free)
	Sound.say("name_" + entry_id)


func stars() -> int:
	return Config.cones_for(total - mistakes, total)


func finish() -> void:
	if done:
		return
	done = true
	var cones := stars()
	Save.set_game(id, cones)
	Sound.play("fanfare")
	Sound.say("ui_game_done")
	_enter = func(): goto.emit("games", "")
	var o := Node2D.new()
	o.z_index = 400
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.35)
	dim.size = Vector2(1920, 1080)
	o.add_child(dim)
	add_child(o)
	var p := UI.panel()
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 20)
	p.add_child(v)
	v.add_child(UI.label(Text.t("game_done"), 72))
	var row := HBoxContainer.new()
	row.alignment = BoxContainer.ALIGNMENT_CENTER
	for i in 3:
		var r := TextureRect.new()
		r.texture = UI.tex("res://assets/ui/%s.png" % ("cone_icon" if i < cones else "cone_empty"))
		r.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		r.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		r.custom_minimum_size = Vector2(100, 100)
		row.add_child(r)
	v.add_child(row)
	var h := HBoxContainer.new()
	h.alignment = BoxContainer.ALIGNMENT_CENTER
	h.add_theme_constant_override("separation", 30)
	var games := UI.tbutton("games", 48)
	games.pressed.connect(func(): goto.emit("games", ""))
	var again := UI.tbutton("again", 48, UI.GREEN)
	again.pressed.connect(func(): goto.emit("game", id))
	h.add_child(games)
	h.add_child(again)
	v.add_child(h)
	UI.centered(o, p)


func _unhandled_key_input(event: InputEvent) -> void:
	if done and event.pressed and event.keycode in [KEY_ENTER, KEY_KP_ENTER] and _enter.is_valid():
		_enter.call()
	elif event.pressed and event.keycode == KEY_ESCAPE:
		goto.emit("games", "")


func _demo() -> void:
	var steps := demo_steps()
	if steps.is_empty():
		return
	ghost = UI.sprite("res://assets/ui/cursor_hand.png", steps[0].to, 2.4)
	ghost.centered = false
	ghost.offset = -Vector2(14, 6)
	ghost.modulate.a = 0.0
	ghost.z_index = 300
	add_child(ghost)
	var tw := ghost.create_tween()
	tw.tween_property(ghost, "modulate:a", 0.85, 0.3)
	for loop in 2:
		ghost.position = steps[0].to
		for s in steps:
			tw.tween_property(ghost, "position", s.to, s.get("time", 0.6)).set_trans(Tween.TRANS_SINE)
			for k in s.get("clicks", 0):
				tw.tween_property(ghost, "scale", Vector2(2.0, 2.0), 0.08)
				tw.tween_property(ghost, "scale", Vector2(2.4, 2.4), 0.08)
		tw.tween_interval(0.4)
		tw.tween_callback(func(): ghost.position = steps[0].to)
	tw.tween_property(ghost, "modulate:a", 0.0, 0.4)
	tw.tween_callback(ghost.queue_free)


static func mouse_pressed(event: InputEvent) -> bool:
	return event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT


static func mouse_released(event: InputEvent) -> bool:
	return event is InputEventMouseButton and not event.pressed and event.button_index == MOUSE_BUTTON_LEFT
