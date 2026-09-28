class_name Critter
extends Node2D

signal completed(c: Critter)
signal hid(c: Critter)
signal missed(c: Critter)

enum State { RISING, SHOWN, SINKING, CAUGHT, GONE }

const LINE := -90.0
const COVER_TOP := -150.0
const SUNK := 50.0
const RISE := 0.6
const SINK := 0.9
const WARN := 0.7

var id := ""
var word := ""
var progress := 0
var peek_time := 12.0
var speed := 1.0
var rare := false
var spot := -1
var state := State.RISING
var t := 0.0

var clip := Control.new()
var pic := Sprite2D.new()
var plaque := Plaque.new()
var content := Rect2()
var _clock := randf() * 10.0
var _rise := 0.0

static var _used := {}


static func content_rect(tex: Texture2D) -> Rect2:
	var key := tex.resource_path if tex.resource_path != "" else str(tex.get_instance_id())
	if not _used.has(key):
		var img := tex.get_image()
		_used[key] = Rect2(img.get_used_rect()) if img else Rect2(Vector2.ZERO, tex.get_size())
	return _used[key]


func setup(entry_id: String, w: String, time: float, spot_i: int, is_rare := false) -> void:
	id = entry_id
	word = w
	peek_time = time
	spot = spot_i
	rare = is_rare


func _ready() -> void:
	clip.clip_contents = true
	clip.mouse_filter = Control.MOUSE_FILTER_IGNORE
	clip.position = Vector2(-200, -520)
	clip.size = Vector2(400, 520 + LINE)
	add_child(clip)
	pic.texture = UI.tex("res://assets/atlas/%s.png" % id)
	pic.centered = false
	content = content_rect(pic.texture)
	pic.offset = Vector2(-pic.texture.get_width() / 2.0, -content.end.y)
	pic.flip_h = randf() < 0.5
	clip.add_child(pic)
	plaque.z_as_relative = false
	plaque.z_index = 60
	if rare:
		plaque.star = true
		plaque.edge = Color("e0a31e")
		_add_glow()
	if word.length() == 1:
		plaque.size = 110
		plaque.pad = Vector2(30, 6)
	elif word.length() > 10:
		plaque.size = 44
	add_child(plaque)
	_place()
	on_progress()


func _add_glow() -> void:
	var g := GradientTexture2D.new()
	g.fill = GradientTexture2D.FILL_RADIAL
	g.fill_from = Vector2(0.5, 0.5)
	g.fill_to = Vector2(0.5, 0.0)
	g.width = 420
	g.height = 420
	var grad := Gradient.new()
	grad.set_color(0, Color(1.0, 0.86, 0.35, 0.75))
	grad.set_color(1, Color(1.0, 0.86, 0.35, 0.0))
	g.gradient = grad
	var glow := Sprite2D.new()
	glow.name = "Glow"
	glow.texture = g
	glow.position = Vector2(0, COVER_TOP - 40)
	add_child(glow)
	move_child(glow, 0)
	var tw := glow.create_tween().set_loops()
	tw.tween_property(glow, "scale", Vector2(1.15, 1.15), 0.7).set_trans(Tween.TRANS_SINE)
	tw.tween_property(glow, "scale", Vector2(0.9, 0.9), 0.7).set_trans(Tween.TRANS_SINE)


func _process(delta: float) -> void:
	_clock += delta
	match state:
		State.RISING:
			_rise = minf(1.0, _rise + delta / RISE)
			if _rise >= 1.0:
				state = State.SHOWN
		State.SHOWN:
			if progress == 0:
				t += delta / peek_time * speed
			if t >= 1.0:
				state = State.SINKING
		State.SINKING:
			_rise -= delta / SINK
			if _rise <= 0.0:
				state = State.GONE
				hid.emit(self)
				queue_free()
				return
	_place()


func _place() -> void:
	var height := content.size.y
	var shown_y := shown_bottom()
	var e := ease(clampf(_rise, 0.0, 1.0), -2.0)
	var y := lerpf(LINE + height, shown_y, e)
	if state == State.SHOWN and t > WARN and progress == 0:
		pic.rotation = sin(_clock * 18.0) * 0.05
	else:
		pic.rotation = 0.0
	pic.position = Vector2(200, 520 + y)
	var half := plaque.box().size.x / 2
	var gx := global_position.x
	plaque.position = Vector2(clampf(gx, half + 10, 1910 - half) - gx, shown_y - height - plaque.box().size.y / 2 - 8 - (spot % 2) * 90)
	plaque.visible = state in [State.RISING, State.SHOWN] or state == State.CAUGHT and progress < word.length()
	plaque.modulate.a = clampf(_rise * 2.0, 0.0, 1.0)
	if rare:
		get_node("Glow").modulate.a = clampf(_rise, 0.0, 1.0)


func shown_bottom() -> float:
	return COVER_TOP + minf(SUNK, content.size.y * 0.3)


func closeness() -> float:
	return t


func is_targetable() -> bool:
	return state in [State.RISING, State.SHOWN] and progress == 0


func picture_global() -> Vector2:
	return pic.global_position + Vector2(0, -content.size.y * 0.5)


func on_progress() -> void:
	plaque.set_state(word, progress, progress > 0 and progress < word.length())
	if progress > 0:
		Sound.play("pop")


func on_miss() -> void:
	missed.emit(self)
	var tw := create_tween()
	var x := plaque.position.x
	for i in 4:
		tw.tween_property(plaque, "position:x", x + (12.0 if i % 2 == 0 else -12.0), 0.04)
	tw.tween_property(plaque, "position:x", x, 0.04)


func on_complete() -> void:
	state = State.CAUGHT
	plaque.set_state(word, progress, false)
	plaque.visible = false
	completed.emit(self)


func take_picture() -> Sprite2D:
	var sp := Sprite2D.new()
	sp.texture = pic.texture
	sp.flip_h = pic.flip_h
	sp.offset = Vector2(0, pic.texture.get_height() / 2.0 - content.get_center().y)
	sp.global_position = picture_global()
	visible = false
	return sp


func vanish() -> void:
	state = State.GONE
	queue_free()


class Finale extends Node2D:
	signal completed(c)
	signal missed(c)

	var word := ""
	var progress := 0
	var plaque := Plaque.new()

	func _init(w: String) -> void:
		word = w

	func _ready() -> void:
		plaque.z_as_relative = false
		plaque.z_index = 60
		if word.length() == 1:
			plaque.size = 120
			plaque.pad = Vector2(34, 6)
		else:
			plaque.size = 64
		add_child(plaque)
		on_progress()

	func closeness() -> float:
		return 1.0

	func is_targetable() -> bool:
		return progress == 0

	func on_progress() -> void:
		plaque.set_state(word, progress, progress > 0 and progress < word.length())
		if progress > 0:
			Sound.play("pop")

	func on_miss() -> void:
		missed.emit(self)

	func on_complete() -> void:
		plaque.set_state(word, progress, false)
		completed.emit(self)
