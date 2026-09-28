class_name Plaque
extends Node2D

const FONT := preload("res://assets/fonts/ShantellHandBold.ttf")
const DONE := Color("2e9e44")
const TODO := Color("2b2b36")
const BG := Color("fffaf0")
const EDGE := Color("6e4524")
const GLOW := Color("f6c744")

var text := ""
var progress := 0
var size := 56
var locked := false
var pad := Vector2(26, 12)
var edge := EDGE
var star := false


func set_state(t: String, p: int, is_locked: bool) -> void:
	text = t
	progress = p
	locked = is_locked
	queue_redraw()


func box() -> Rect2:
	var w := FONT.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x
	var h := FONT.get_height(size)
	return Rect2(-w / 2 - pad.x, -h / 2 - pad.y, w + pad.x * 2, h + pad.y * 2)


func _draw() -> void:
	if text.is_empty():
		return
	var r := box()
	if locked:
		draw_style(r.grow(8), GLOW, 22)
	draw_style(r.grow(6 if star else 3), edge, 18)
	draw_style(r, BG, 16)
	if star:
		draw_string(FONT, Vector2(r.position.x - 34, r.position.y + r.size.y * 0.7), "★", HORIZONTAL_ALIGNMENT_LEFT, -1, 60, Color("e0a31e"))
	var x := r.position.x + pad.x
	var base := r.position.y + pad.y + FONT.get_ascent(size)
	for i in text.length():
		var ch := text[i]
		var col := DONE if i < progress else TODO
		draw_string(FONT, Vector2(x, base), ch, HORIZONTAL_ALIGNMENT_LEFT, -1, size, col)
		if i == progress and locked:
			var cw := FONT.get_string_size(ch, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x
			draw_rect(Rect2(x, base + 8, cw, 5), GLOW)
		x += FONT.get_string_size(ch, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x


func draw_style(r: Rect2, c: Color, radius: int) -> void:
	var sb := StyleBoxFlat.new()
	sb.bg_color = c
	sb.set_corner_radius_all(radius)
	sb.anti_aliasing = true
	draw_style_box(sb, r)
