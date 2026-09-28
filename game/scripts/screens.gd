class_name Screens
extends RefCounted


static func back_button(parent: Node, target: String) -> Button:
	var back := UI.tbutton("back", 40, UI.GREEN)
	back.pressed.connect(func(): parent.goto.emit(target, ""))
	back.position = Vector2(40, 950)
	parent.add_child(back)
	return back


class Title extends Node2D:
	signal goto(screen: String, arg: String)

	func _ready() -> void:
		add_child(UI.backdrop("res://assets/bg/title.png"))
		var fabian := UI.standing("res://assets/chars/fabian_wave.png", Vector2(1560, 1030), 1.05)
		add_child(fabian)
		var joey := UI.standing("res://assets/chars/joey_stand.png", Vector2(1260, 1040), 0.85)
		add_child(joey)
		UI.centered(self, UI.bilabel(Text.t("title"), Text.o("title"), 140, Color("7a3e1d"), 26), Vector2(860, 230))
		var play := UI.tbutton("play", 100)
		play.pressed.connect(_go)
		UI.centered(self, play, Vector2(860, 640))
		UI.lang_switch(self, func(): goto.emit("title", ""), Vector2(860, 1040))
		var music := UI.button("♪", 44, UI.YELLOW if Save.setting("music") else UI.GREY)
		music.tooltip_text = Text.t("music")
		music.custom_minimum_size = Vector2(90, 0)
		music.pressed.connect(func():
			Sound.set_music(not Save.setting("music"))
			goto.emit("title", ""))
		music.position = Vector2(1080, 1040 - 78)
		add_child(music)
		var credit := UI.label(Text.t("music_credit"), 22, UI.SOFT)
		credit.position = Vector2(20, 1045)
		add_child(credit)

	func _go() -> void:
		Sound.start_ambience()
		goto.emit("players", "")

	func _unhandled_input(event: InputEvent) -> void:
		var key: bool = event is InputEventKey and event.pressed and event.keycode in [KEY_ENTER, KEY_SPACE, KEY_KP_ENTER]
		var click: bool = event is InputEventMouseButton and event.pressed and event.position.y < 900
		if key or click:
			get_viewport().set_input_as_handled()
			_go()


class Players extends Node2D:
	signal goto(screen: String, arg: String)

	func _ready() -> void:
		add_child(UI.backdrop("res://assets/bg/zator.png"))
		UI.centered(self, UI.tlabel("who", 72, UI.INK, 18), Vector2(960, 110))
		Sound.say("ui_who")
		var ids := ["alica", "hanka", "host"]
		for i in ids.size():
			_card(ids[i], Vector2(420 + i * 540, 590))
		Screens.back_button(self, "title").position = Vector2(40, 30)
		UI.lang_switch(self, func(): goto.emit("players", ""))

	func _unhandled_input(event: InputEvent) -> void:
		if event is InputEventKey and event.pressed and event.keycode == KEY_ESCAPE:
			get_viewport().set_input_as_handled()
			goto.emit("title", "")

	func _card(id: String, at: Vector2) -> void:
		var p: Dictionary = Save.data.players[id]
		var bg := UI.panel()
		bg.custom_minimum_size = Vector2(460, 760)
		UI.centered(self, bg, at)
		var pic := UI.standing("res://assets/chars/%s_happy.png" % p.look, at + Vector2(0, 90), 0.95)
		add_child(pic)
		var look := UI.button("⟳", 40, UI.GREEN)
		look.tooltip_text = Text.t("look")
		look.pressed.connect(func():
			var i := Config.LOOKS.find(p.look)
			Save.set_look(id, Config.LOOKS[(i + 1) % Config.LOOKS.size()])
			goto.emit("players", ""))
		look.position = at + Vector2(130, -330)
		add_child(look)
		var pick := UI.button(Text.player_name(id), 64)
		pick.custom_minimum_size = Vector2(340, 0)
		pick.pressed.connect(func():
			Save.current = id
			goto.emit("map", ""))
		UI.centered(self, pick, at + Vector2(0, 170))
		var rank := UI.button2(Text.rank(p.profile), Text.rank(p.profile, Text.other_lang()), 42, UI.GREEN)
		rank.custom_minimum_size.x = 340
		rank.pressed.connect(func():
			var i := Config.PROFILE_ORDER.find(p.profile)
			Save.set_profile(id, Config.PROFILE_ORDER[(i + 1) % Config.PROFILE_ORDER.size()])
			goto.emit("players", ""))
		UI.centered(self, rank, at + Vector2(0, 290))


class Map extends Node2D:
	signal goto(screen: String, arg: String)

	func _ready() -> void:
		add_child(UI.backdrop("res://assets/rooms/map.png"))
		var p := Save.player()
		var head := UI.bilabel("%s · %s" % [Text.player_name(Save.current), Text.rank(p.profile)], Text.rank(p.profile, Text.other_lang()), 52, UI.INK, 16)
		UI.centered(self, head, Vector2(960, 70))
		Sound.say("ui_map")
		var home := UI.sprite("res://assets/ui/house.png", Config.MAP_HOME, 0.9)
		add_child(home)
		UI.centered(self, UI.bilabel("Hostomice", "", 34, UI.INK, 10), Config.MAP_HOME + Vector2(0, 80))
		for n in Config.MAP:
			_trail_marker(n)
		if Save.is_done(2):
			for at in Config.MAP_FOG:
				add_child(UI.sprite("res://assets/ui/question.png", at, 0.8))
				UI.centered(self, UI.tlabel("soon", 30, UI.INK, 10), at + Vector2(0, 80))
		var atlas := UI.button2("%s (%d)" % [Text.t("atlas"), Save.distinct_found()], "", 44)
		atlas.pressed.connect(func(): goto.emit("atlas", ""))
		atlas.position = Vector2(40, 30)
		add_child(atlas)
		var games := UI.button(Text.t("games"), 44, UI.GREEN)
		games.pressed.connect(func(): goto.emit("games", ""))
		games.position = Vector2(40, 130)
		add_child(games)
		Screens.back_button(self, "players")
		UI.lang_switch(self, func(): goto.emit("map", ""), Vector2(1790, 110))

	func _trail_marker(n: int) -> void:
		var at: Vector2 = Config.MAP[n]
		var t := Atlas.trail(n)
		var open := Save.is_unlocked(n)
		var b := UI.button2(t.name[Save.lang()], t.name[Text.other_lang()], 34, UI.YELLOW if open else UI.GREY)
		b.disabled = not open
		b.pressed.connect(func(): goto.emit("trail", str(n)))
		UI.centered(self, b, at + Vector2(0, 110))
		b.position.x = clampf(b.position.x, 10, 1910 - b.size.x)
		b.position.y = minf(b.position.y, 1070 - b.size.y)
		if not open:
			add_child(UI.sprite("res://assets/ui/lock.png", at + Vector2(0, 20), 0.6))
		elif Save.is_done(n):
			var row := HBoxContainer.new()
			row.add_theme_constant_override("separation", 0)
			for i in 3:
				var r := TextureRect.new()
				r.texture = UI.tex("res://assets/ui/%s.png" % ("cone_icon" if i < Save.cones(n) else "cone_empty"))
				r.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
				r.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
				r.custom_minimum_size = Vector2(52, 52)
				row.add_child(r)
			UI.centered(self, row, at + Vector2(0, 20))
		else:
			var paw := UI.sprite("res://assets/ui/paw.png", at + Vector2(0, 10), 0.6)
			add_child(paw)
			UI.bob(paw, 8, 1.2)

	func _unhandled_input(event: InputEvent) -> void:
		if event is InputEventKey and event.pressed and event.keycode in [KEY_ENTER, KEY_KP_ENTER]:
			get_viewport().set_input_as_handled()
			goto.emit("trail", str(Save.latest_trail()))


class Book extends Node2D:
	signal goto(screen: String, arg: String)

	const TABS := ["photo", "basket", "herbarium", "treasures"]
	const PER_PAGE := 18
	const CARD := Vector2(128, 130)

	var tab := "photo"
	var page := 0
	var cards := Node2D.new()
	var detail: Node2D

	func _init(arg := "") -> void:
		if arg != "":
			var parts := arg.split(":")
			tab = parts[0]
			page = int(parts[1]) if parts.size() > 1 else 0

	func _ready() -> void:
		add_child(UI.backdrop("res://assets/rooms/atlas.png"))
		var h := HBoxContainer.new()
		h.add_theme_constant_override("separation", 14)
		for tb in TABS:
			var b := UI.button2(Text.t("tab_" + tb), Text.o("tab_" + tb), 36, UI.YELLOW if tb == tab else UI.GREEN)
			b.pressed.connect(func(): goto.emit("atlas", tb))
			h.add_child(b)
		UI.centered(self, h, Vector2(960, 55))
		add_child(cards)
		if tab == "treasures":
			_treasures()
		else:
			_entries()
		Screens.back_button(self, "map")
		UI.lang_switch(self, func(): goto.emit("atlas", "%s:%d" % [tab, page]), Vector2(1600, 1060))

	func _entries() -> void:
		var ids := Atlas.ids_in_tab(tab)
		var pages := ceili(ids.size() / float(PER_PAGE))
		page = clampi(page, 0, maxi(pages - 1, 0))
		var count := UI.bilabel("%d / %d" % [Save.distinct_found(ids), ids.size()], "", 40, UI.INK, 10)
		UI.centered(self, count, Vector2(700, 985))
		var shown := ids.slice(page * PER_PAGE, (page + 1) * PER_PAGE)
		for i in shown.size():
			var side := 0 if i < 9 else 1
			var k := i % 9
			var at := Vector2(260 + side * 820 + (k % 3) * 290, 280 + (k / 3) * 250)
			_card(shown[i], at)
		if page > 0:
			_arrow("◀", Vector2(20, 470), page - 1)
		if page < pages - 1:
			_arrow("▶", Vector2(1790, 470), page + 1)

	func _arrow(text: String, at: Vector2, to: int) -> void:
		var a := UI.button(text, 80)
		a.position = at
		a.pressed.connect(func(): goto.emit("atlas", "%s:%d" % [tab, to]))
		add_child(a)

	func _card(id: String, at: Vector2) -> void:
		var n := Save.found_count(id)
		var e := Atlas.entry(id)
		var pic := UI.sprite("res://assets/atlas/%s.png" % id, at, 0.62)
		if n == 0:
			pic.modulate = Color(0.15, 0.13, 0.1, 0.35)
		cards.add_child(pic)
		if n > 0:
			var names := UI.bilabel(Atlas.name_of(id), Atlas.name_of(id, Text.other_lang()), 30, UI.INK, 8)
			UI.centered(cards, names, at + Vector2(0, 100))
			var cnt := UI.label("×%d" % n, 26, UI.SOFT)
			cnt.position = at + Vector2(46, -86)
			cards.add_child(cnt)
		else:
			UI.centered(cards, UI.label("?", 44, UI.SOFT), at + Vector2(0, 100))
		if e.rare:
			var star := UI.label("★", 34, Color("e0a31e"), 8)
			star.position = at + Vector2(-80, -90)
			cards.add_child(star)
		var hit := Button.new()
		hit.flat = true
		hit.focus_mode = Control.FOCUS_NONE
		hit.size = Vector2(220, 230)
		hit.position = at - Vector2(110, 110)
		hit.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
		hit.pressed.connect(func(): _detail(id))
		cards.add_child(hit)

	func _detail(id: String) -> void:
		if detail:
			detail.queue_free()
		var e := Atlas.entry(id)
		var n := Save.found_count(id)
		detail = Node2D.new()
		detail.z_index = 100
		add_child(detail)
		var dim := ColorRect.new()
		dim.color = Color(0, 0, 0, 0.35)
		dim.size = Vector2(1920, 1080)
		dim.gui_input.connect(func(ev):
			if ev is InputEventMouseButton and ev.pressed:
				_close_detail())
		detail.add_child(dim)
		var p := UI.panel()
		var v := VBoxContainer.new()
		v.add_theme_constant_override("separation", 8)
		p.add_child(v)
		var img := TextureRect.new()
		img.texture = UI.tex("res://assets/atlas/%s.png" % id)
		img.custom_minimum_size = Vector2(260, 260)
		img.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		img.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		if n == 0:
			img.modulate = Color(0.15, 0.13, 0.1, 0.35)
		v.add_child(img)
		if n > 0:
			v.add_child(UI.label(Atlas.name_of(id), 56))
			v.add_child(UI.label(Atlas.name_of(id, "", true), 32, UI.SOFT))
		else:
			v.add_child(UI.tlabel("not_found", 44))
		var cat := UI.label(Text.t("cat_" + str(e.cat)), 32, UI.RED if e.cat == "poison" else UI.DONE)
		v.add_child(cat)
		if n > 0 and Atlas.fact(id) != "":
			var f := UI.label(Atlas.fact(id), 34)
			f.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
			f.custom_minimum_size = Vector2(820, 0)
			v.add_child(f)
		var where := []
		for t in Atlas.trails_of(id):
			where.append(Atlas.trail(t).name[Save.lang()])
		if not where.is_empty():
			var w := UI.label(Text.t("where") % ", ".join(where), 26, UI.SOFT)
			w.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
			w.custom_minimum_size = Vector2(820, 0)
			v.add_child(w)
		var close := UI.tbutton("back", 40, UI.GREEN)
		close.pressed.connect(_close_detail)
		v.add_child(close)
		UI.centered(detail, p)
		if n > 0:
			Sound.say_all(["name_" + id, "fact_" + id])

	func _close_detail() -> void:
		Sound.hush()
		if detail:
			detail.queue_free()
			detail = null

	func _treasures() -> void:
		UI.centered(self, UI.tlabel("treasures", 56), Vector2(500, 200))
		for n in range(1, Config.TRAIL_COUNT + 1):
			var k: Dictionary = Atlas.trail(n).keepsake
			var at := Vector2([270, 560, 850, 1080, 1370, 1660][n - 1], 420)
			var has := Save.has_keepsake(k.id)
			var s := UI.sprite("res://assets/keepsakes/%s.png" % k.id, at, 1.0)
			if not has:
				s.modulate = Color(0.15, 0.13, 0.1, 0.3)
			cards.add_child(s)
			if has:
				var l := UI.bilabel(k[Save.lang()], k[Text.other_lang()], 28, UI.INK, 8)
				for c in l.get_children():
					c.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
					c.custom_minimum_size = Vector2(240, 0)
				UI.centered(cards, l, at + Vector2(0, 150))
			else:
				UI.centered(cards, UI.label("?", 44, UI.SOFT), at + Vector2(0, 130))
		var total := Save.total_cones()
		var row := HBoxContainer.new()
		var cone := TextureRect.new()
		cone.texture = UI.tex("res://assets/ui/cone_icon.png")
		cone.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		cone.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		cone.custom_minimum_size = Vector2(90, 90)
		row.add_child(cone)
		row.add_child(UI.bilabel(Text.t("cones") % total, Text.o("cones") % total, 44))
		UI.centered(cards, row, Vector2(1420, 800))


class GamesMenu extends Node2D:
	signal goto(screen: String, arg: String)

	func _ready() -> void:
		add_child(UI.backdrop("res://assets/bg/palouky.png"))
		UI.centered(self, UI.label(Text.t("games"), 72, UI.INK, 18), Vector2(960, 80))
		for i in Games.ORDER.size():
			_card(i, Vector2(420 + (i % 3) * 540, 360 + (i / 3) * 430))
		Screens.back_button(self, "map")
		UI.lang_switch(self, func(): goto.emit("games", ""), Vector2(1790, 1050))

	func _card(i: int, at: Vector2) -> void:
		var id: String = Games.ORDER[i]
		var open := Save.game_unlocked(i)
		var p := UI.panel()
		p.custom_minimum_size = Vector2(460, 380)
		UI.centered(self, p, at)
		var pic := UI.sprite("res://assets/%s.png" % Games.ICON[id], at + Vector2(0, -60), 0.9)
		var tex_h := pic.texture.get_height() * 0.9
		if tex_h > 200:
			pic.scale *= 200.0 / tex_h
		if not open:
			pic.modulate = Color(0.2, 0.18, 0.15, 0.35)
		add_child(pic)
		var b := UI.button(Text.t("game_" + id), 38, UI.YELLOW if open else UI.GREY)
		b.disabled = not open
		b.pressed.connect(func(): goto.emit("game", id))
		UI.centered(self, b, at + Vector2(0, 90))
		UI.centered(self, UI.label(Text.t("skill_" + id), 28, UI.SOFT), at + Vector2(0, 150))
		if not open:
			add_child(UI.sprite("res://assets/ui/lock.png", at + Vector2(0, -60), 0.8))
			return
		var row := HBoxContainer.new()
		for k in 3:
			var r := TextureRect.new()
			r.texture = UI.tex("res://assets/ui/%s.png" % ("cone_icon" if k < Save.game_cones(id) else "cone_empty"))
			r.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
			r.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
			r.custom_minimum_size = Vector2(40, 40)
			row.add_child(r)
		UI.centered(self, row, at + Vector2(170, -150))

	func _unhandled_key_input(event: InputEvent) -> void:
		if event.pressed and event.keycode == KEY_ESCAPE:
			goto.emit("map", "")
