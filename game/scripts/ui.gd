class_name UI
extends RefCounted

const FONT := preload("res://assets/fonts/ShantellHandBold.ttf")
const INK := Color("2b2b36")
const SOFT := Color("5d6b58")
const YELLOW := Color("f6c744")
const GREEN := Color("a8d08d")
const GREY := Color("cfc8b8")
const PAPER := Color("fffaf0")
const WOOD := Color("6e4524")
const DONE := Color("2e9e44")
const RED := Color("c8483e")
const BILINGUAL := false

static var _placeholders := {}


static func tex(path: String) -> Texture2D:
	if ResourceLoader.exists(path):
		return load(path)
	if not _placeholders.has(path):
		var img := Image.create(160, 160, false, Image.FORMAT_RGBA8)
		var c := Color.from_hsv(float(hash(path) % 360) / 360.0, 0.45, 0.85)
		for y in 160:
			for x in 160:
				if Vector2(x - 80, y - 80).length() < 76:
					img.set_pixel(x, y, c)
		_placeholders[path] = ImageTexture.create_from_image(img)
	return _placeholders[path]


static func box(c: Color, radius := 22, border := 5, border_col := WOOD) -> StyleBoxFlat:
	var sb := StyleBoxFlat.new()
	sb.bg_color = c
	sb.set_corner_radius_all(radius)
	sb.set_border_width_all(border)
	sb.border_color = border_col
	sb.content_margin_left = 28
	sb.content_margin_right = 28
	sb.content_margin_top = 10
	sb.content_margin_bottom = 14
	sb.shadow_color = Color(0, 0, 0, 0.2)
	sb.shadow_size = 6
	sb.shadow_offset = Vector2(0, 5)
	return sb


static func _style(b: Button, colour: Color) -> void:
	b.focus_mode = Control.FOCUS_NONE
	b.add_theme_color_override("font_color", INK)
	b.add_theme_color_override("font_hover_color", INK)
	b.add_theme_color_override("font_pressed_color", INK)
	b.add_theme_color_override("font_disabled_color", Color(INK, 0.55))
	b.add_theme_stylebox_override("normal", box(colour))
	b.add_theme_stylebox_override("hover", box(colour.lightened(0.25)))
	b.add_theme_stylebox_override("pressed", box(colour.darkened(0.1)))
	b.add_theme_stylebox_override("disabled", box(GREY))
	b.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
	b.pressed.connect(func(): Sound.play("pop"))


static func button(text: String, size := 56, colour := YELLOW) -> Button:
	var b := Button.new()
	b.text = text
	b.add_theme_font_size_override("font_size", size)
	_style(b, colour)
	return b


static func button2(primary: String, secondary: String, size := 56, colour := YELLOW) -> Button:
	if not BILINGUAL or secondary == "" or secondary == primary:
		return button(primary, size, colour)
	var b := Button.new()
	_style(b, colour)
	var v := bilabel(primary, secondary, size)
	v.mouse_filter = Control.MOUSE_FILTER_IGNORE
	for c in v.get_children():
		c.mouse_filter = Control.MOUSE_FILTER_IGNORE
	b.add_child(v)
	b.ready.connect(func(): _fit(b, v))
	b.resized.connect(func(): v.position = (b.size - v.size) / 2)
	return b


static func _fit(b: Button, v: Control) -> void:
	v.reset_size()
	var sb: StyleBox = b.get_theme_stylebox("normal")
	var pad := Vector2(sb.content_margin_left + sb.content_margin_right, sb.content_margin_top + sb.content_margin_bottom)
	b.custom_minimum_size = b.custom_minimum_size.max(v.size + pad)
	b.reset_size()
	v.position = (b.size - v.size) / 2


static func tbutton(key: String, size := 56, colour := YELLOW) -> Button:
	return button2(Text.t(key), Text.o(key), size, colour)


static func label(text: String, size := 48, colour := INK, outline := 0) -> Label:
	var l := Label.new()
	l.text = text
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", colour)
	if outline > 0:
		l.add_theme_constant_override("outline_size", outline)
		l.add_theme_color_override("font_outline_color", PAPER)
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	return l


static func bilabel(primary: String, secondary: String, size := 48, colour := INK, outline := 0) -> VBoxContainer:
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", -int(size * 0.18))
	v.add_child(label(primary, size, colour, outline))
	if BILINGUAL and secondary != "" and secondary != primary:
		v.add_child(label(secondary, int(size * 0.62), SOFT, outline))
	return v


static func tlabel(key: String, size := 48, colour := INK, outline := 0) -> VBoxContainer:
	return bilabel(Text.t(key), Text.o(key), size, colour, outline)


static func panel(colour := PAPER) -> PanelContainer:
	var p := PanelContainer.new()
	var sb := box(colour, 30, 6)
	sb.content_margin_left = 60
	sb.content_margin_right = 60
	sb.content_margin_top = 40
	sb.content_margin_bottom = 40
	p.add_theme_stylebox_override("panel", sb)
	return p


static func lang_switch(parent: Node, on_change: Callable, at := Vector2(960, 1040)) -> void:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 10)
	for l in Text.LANGS:
		var active: bool = l == Save.lang()
		var b := button(l.to_upper(), 40, YELLOW if active else GREY)
		b.custom_minimum_size = Vector2(110, 0)
		if not active:
			b.pressed.connect(func():
				Save.set_lang(l)
				on_change.call())
		h.add_child(b)
	parent.add_child(h)
	h.reset_size()
	h.position = Vector2(at.x - h.size.x / 2, at.y - h.size.y)


static func sprite(path: String, pos: Vector2, s := 1.0) -> Sprite2D:
	var sp := Sprite2D.new()
	sp.texture = tex(path)
	sp.position = pos
	sp.scale = Vector2(s, s)
	return sp


static func standing(path: String, feet: Vector2, s := 1.0) -> Sprite2D:
	var sp := sprite(path, feet, s)
	sp.centered = false
	sp.offset = Vector2(-sp.texture.get_width() / 2.0, -sp.texture.get_height())
	return sp


static func centered(parent: Node, c: Control, at := Vector2(960, 540)) -> void:
	parent.add_child(c)
	c.reset_size()
	c.position = at - c.size / 2


static func bob(node: CanvasItem, amp := 6.0, period := 1.6) -> void:
	var tw := node.create_tween().set_loops()
	var y: float = node.position.y
	tw.tween_property(node, "position:y", y - amp, period / 2).set_trans(Tween.TRANS_SINE)
	tw.tween_property(node, "position:y", y, period / 2).set_trans(Tween.TRANS_SINE)


static func pulse(n: CanvasItem, big := 1.4) -> void:
	if n is Control:
		n.pivot_offset = n.size / 2
	var base: Vector2 = n.scale
	var tw := n.create_tween()
	tw.tween_property(n, "scale", base * big, 0.12)
	tw.tween_property(n, "scale", base, 0.2)


static func backdrop(path: String) -> Node2D:
	var root := Node2D.new()
	var t := tex(path)
	var filler := ColorRect.new()
	filler.color = t.get_image().get_pixel(8, t.get_height() - 8) if t.get_image() else Color("6f8f4f")
	filler.position = Vector2(-200, 1070)
	filler.size = Vector2(2400, 1200)
	root.add_child(filler)
	var sp := Sprite2D.new()
	sp.texture = t
	sp.centered = false
	if t.get_width() != 1920:
		sp.scale = Vector2(1920.0 / t.get_width(), 1080.0 / t.get_height())
	root.add_child(sp)
	return root
