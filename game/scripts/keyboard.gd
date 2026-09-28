class_name OnScreenKeyboard
extends Node2D

signal typed(ch: String)

const ROWS := ["QWERTZUIOP", "ASDFGHJKL", "YXCVBNM"]
const KEY := 66.0
const GAP := 7.0

var keys := {}
var _lit := ""


func _ready() -> void:
	for r in ROWS.size():
		var row: String = ROWS[r]
		var w := row.length() * (KEY + GAP) - GAP
		for i in row.length():
			var ch := row[i]
			var b := Button.new()
			b.text = ch
			b.focus_mode = Control.FOCUS_NONE
			b.size = Vector2(KEY, KEY)
			b.position = Vector2(-w / 2 + i * (KEY + GAP) + r * 18.0, r * (KEY + GAP))
			b.add_theme_font_size_override("font_size", 40)
			b.add_theme_color_override("font_color", UI.INK)
			b.add_theme_color_override("font_hover_color", UI.INK)
			_style(b, false)
			b.pressed.connect(func(): typed.emit(ch))
			add_child(b)
			keys[ch] = b


func _style(b: Button, lit: bool) -> void:
	var c := UI.YELLOW if lit else UI.PAPER
	var sb := UI.box(c, 12, 6 if lit else 3, Color("e0473f") if lit else UI.WOOD)
	sb.content_margin_left = 0
	sb.content_margin_right = 0
	sb.content_margin_top = 0
	sb.content_margin_bottom = 4
	for s in ["normal", "hover", "pressed"]:
		b.add_theme_stylebox_override(s, sb)


func highlight(ch: String) -> void:
	var k := Typing.fold(ch)
	if k == _lit:
		return
	if keys.has(_lit):
		_style(keys[_lit], false)
		keys[_lit].scale = Vector2.ONE
	_lit = k
	if keys.has(k):
		var b: Button = keys[k]
		_style(b, true)
		b.pivot_offset = b.size / 2
		var tw := b.create_tween()
		tw.tween_property(b, "scale", Vector2(1.18, 1.18), 0.15)


func flash(ch: String) -> void:
	var k := Typing.fold(ch)
	if not keys.has(k):
		return
	var b: Button = keys[k]
	b.modulate = Color(1, 0.7, 0.7)
	b.create_tween().tween_property(b, "modulate", Color.WHITE, 0.3)
