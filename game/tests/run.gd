extends Node

var failures := 0
var checks := 0
var save: Node
var atlas: Node


class FakeTarget:
	var word := ""
	var progress := 0
	var t := 0.0
	var done := false
	var misses := 0

	func _init(w: String, dist: float) -> void:
		word = w
		t = dist

	func is_targetable() -> bool:
		return progress == 0 and not done

	func closeness() -> float:
		return t

	func on_progress() -> void:
		pass

	func on_miss() -> void:
		misses += 1

	func on_complete() -> void:
		done = true


func check(cond: bool, what: String) -> void:
	checks += 1
	if not cond:
		failures += 1
		print("FAIL: ", what)


func _ready() -> void:
	_run.call_deferred()


func _run() -> void:
	save = get_tree().root.get_node("Save")
	atlas = get_tree().root.get_node("Atlas")
	save.path = "user://test_save.json"
	save.data = save.defaults()
	test_typing()
	test_atlas_data()
	test_trail_data()
	test_words()
	test_text()
	test_wave()
	test_save()
	test_assets()
	await test_trails()
	await test_screens()
	await test_games()
	DirAccess.remove_absolute(ProjectSettings.globalize_path("user://test_save.json"))
	print("%d checks, %d failures" % [checks, failures])
	get_tree().quit(1 if failures > 0 else 0)


func key(ch: String) -> InputEventKey:
	var e := InputEventKey.new()
	e.pressed = true
	e.unicode = ch.unicode_at(0)
	return e


func test_typing() -> void:
	check(Typing.fold("č") == "C", "fold lowercase č")
	check(Typing.char_from_event(key("ř")) == "ř", "unicode read from event")
	var ty := Typing.new()
	var near := FakeTarget.new("HŘIB", 0.8)
	var far := FakeTarget.new("HARE", 0.2)
	ty.add(far)
	ty.add(near)
	check(ty.handle("x") == Typing.Result.MISS, "unknown first letter misses")
	check(ty.handle("h") == Typing.Result.LOCKED and ty.locked == near, "letter locks the one closest to hiding")
	check(ty.handle("z") == Typing.Result.MISS and near.progress == 1, "miss keeps progress")
	check(ty.handle("r") == Typing.Result.ADVANCED, "lenient r matches Ř")
	ty.handle("i")
	check(ty.handle("b") == Typing.Result.COMPLETED and near.done, "word completed")
	var exact := Typing.new()
	exact.lenient = false
	exact.add(FakeTarget.new("ČAJ", 0.5))
	check(exact.handle("c") == Typing.Result.MISS, "exact mode rejects c for Č")
	var spaced := Typing.new()
	var s := FakeTarget.new("ROE DEER", 0.5)
	spaced.add(s)
	for ch in "roe deer":
		spaced.handle(ch)
	check(s.done, "space typed as part of a name")


func test_atlas_data() -> void:
	check(atlas.order.size() >= 60, "atlas has %d entries" % atlas.order.size())
	var dead := ["Ď", "Ť", "Ň", "Ó", "-", "'"]
	for id in atlas.order:
		var e: Dictionary = atlas.entries[id]
		check(e.cat in Config.TAB_OF, "%s has a known category" % id)
		for f in ["cs", "en", "cs_long", "en_long"]:
			var w: String = e[f]
			check(w != "" and w == w.to_upper(), "%s.%s filled and upper case" % [id, f])
			for d in dead:
				check(not d in w, "%s.%s avoids %s" % [id, f, d])
			for ch in w:
				check(ch == " " or Typing.fold(ch).unicode_at(0) in range(65, 91), "%s.%s only letters: %s" % [id, f, ch])
		check(e.en.length() <= 13 and e.cs.length() <= 17, "%s short names are short" % id)
		check(not atlas.trails_of(id).is_empty(), "%s appears on some trail" % id)
		for l in Text.LANGS:
			var f: String = atlas.fact(id, l)
			check(f.length() >= 40 and f.length() <= 320, "%s has a %s fact" % [id, l])
			check(ResourceLoader.exists("res://assets/voice/%s/fact_%s.ogg" % [l, id]), "%s fact voiced in %s" % [id, l])
	for tab in Config.TABS:
		check(atlas.ids_in_tab(tab).size() >= 10, "tab %s has entries" % tab)


func test_trail_data() -> void:
	var keepsakes := {}
	for n in range(1, Config.TRAIL_COUNT + 1):
		var t: Dictionary = atlas.trail(n)
		check(t.has("name") and t.has("finale") and t.has("target") and t.has("target_sova") and t.has("thanks") and t.has("keepsake"), "trail %d complete" % n)
		check(t.stations.size() >= 3, "trail %d has stations" % n)
		check(not t.rare.is_empty() and t.fabian.size() >= 1, "trail %d has rare finds and Fabián lines" % n)
		keepsakes[t.keepsake.id] = true
		for id in t.rare:
			check(atlas.entry(id).get("rare", false), "trail %d rare %s is flagged rare" % [n, id])
		for st in t.stations:
			for id in st.finds:
				check(atlas.entries.has(id), "trail %d station %s: %s exists" % [n, st.id, id])
				check(not atlas.entry(id).get("rare", true), "station %s: %s isn't a rare-only find" % [st.id, id])
			check(not ("liska" in st.finds and "liska_houba" in st.finds), "station %s never has fox and chanterelle together" % st.id)
			for prof in Config.PROFILE_ORDER:
				check(atlas.finds_for(n, t.stations.find(st), prof).size() >= Config.PROFILES[prof].per_station - 1, "station %s has enough finds for %s" % [st.id, prof])
		for l in Text.LANGS:
			for prof in Config.PROFILE_ORDER:
				var w: String = atlas.target_for(n, prof, l)
				check(w != "" and not "'" in w and not "Ď" in w, "trail %d %s/%s target %s" % [n, prof, l, w])
			check(t.name[l] != "" and t.thanks[l] != "" and t.keepsake[l] != "", "trail %d texts in %s" % [n, l])
			for line in t.fabian:
				check(line[l] != "", "trail %d Fabián line in %s" % [n, l])
	check(keepsakes.size() == Config.TRAIL_COUNT, "every trail has its own keepsake")
	check(not atlas.finds_for(1, 3, "veverka").has("zelena") and atlas.finds_for(1, 3, "sova").has("zelena"), "Sova-only entries filtered")


func test_words() -> void:
	check(atlas.word_for("hrib", "jezek", "cs") == "H" and atlas.word_for("hrib", "jezek", "en") == "P", "Ježek types the first letter of the name")
	check(atlas.word_for("zaba", "jezek", "cs") == "Z", "Ježek letter is folded")
	check(atlas.word_for("hrib", "veverka", "en") == "PORCINI" and atlas.word_for("hrib", "sova", "cs") == "HŘIB SMRKOVÝ", "rank picks short or long name")
	save.set_lang("cs")
	check(atlas.translation_pair("hrib", "veverka") == ["HŘIB", "PORCINI"], "translation pair follows language")
	check(atlas.target_for(1, "jezek", "cs") == "F" and atlas.target_for(3, "jezek", "en") == "R", "Ježek finale is a letter")
	atlas.reset()
	var seen := {}
	for i in 5:
		var id: String = atlas.pick(1, 0, "veverka", ["Z"])
		check(id != "" and atlas.first_letter(id, "veverka") != "Z", "pick avoids first letters (%s)" % id)
		seen[id] = true
	check(seen.size() == 5, "bag gives distinct finds")


func test_text() -> void:
	for k in Text.STRINGS:
		check(Text.STRINGS[k].size() == Text.LANGS.size(), "text %s has every language" % k)
	for prof in Config.PROFILE_ORDER:
		check(Text.STRINGS.has("rank_" + prof), "rank name for %s" % prof)
	for cat in Config.TAB_OF:
		check(Text.STRINGS.has("cat_" + cat), "category name for %s" % cat)
	save.set_lang("en")
	check(Text.t("map") == "Map" and Text.o("map") == "Mapa", "english primary, czech secondary")
	check(Text.rank("jezek") == "Hedgehog" and Text.player_name("host") == "Guest", "english ranks and names")
	check(Sound.has_voice("ui_who") and Sound.has_voice("name_hrib") and Sound.has_voice("letter_A"), "english voice")
	save.set_lang("cs")
	check(Sound.has_voice("ui_who") and Sound.has_voice("fabian_1_0") and Sound.has_voice("thanks_6"), "czech voice")


func test_wave() -> void:
	var w := Wave.new(Config.PROFILES.veverka)
	check(w.allowed_active() == 1 and w.wants_spawn(0), "veverka starts with one at a time")
	for i in 2:
		w.on_spawn()
		w.on_resolved(true)
	check(w.allowed_active() == 2, "then two at a time")
	w.add_rare()
	check(w.total == Config.PROFILES.veverka.per_station + 1 and w.rare_due, "rare adds one more find")
	w.on_spawn(true)
	check(not w.rare_due, "rare spawned")
	while not w.done():
		w.on_spawn()
		w.on_resolved(false)
	check(w.done() and w.caught == 2, "station ends even when things hide")
	var p := Wave.new(Config.PROFILES.jezek)
	var got := false
	for i in Config.PAWS_FOR_RARE:
		got = p.paws_after(true, true)
	check(got and p.paws == 0, "full paws trigger Joey")
	p.paws_after(true, true)
	check(not p.paws_after(false, false) and p.paws == 0, "a hidden find resets the paws")
	check(is_equal_approx(p.speed_after(1.0, false, false), 1.0 - Config.SPEED_DOWN), "slower after a miss")


func test_save() -> void:
	save.data = save.defaults()
	save.current = "alica"
	check(save.is_unlocked(1) and not save.is_unlocked(2), "only trail 1 open at start")
	check(save.finish_trail(1, 2, "cone") == 2 and save.is_unlocked(2) and not save.is_unlocked(3), "trails unlock in order")
	save.finish_trail(1, 1, "cone")
	check(save.cones(1) == 2 and save.player().keepsakes == ["cone"], "best cones kept, keepsake once")
	check(save.add_found("hrib") and not save.add_found("hrib"), "first find is new")
	check(save.found_count("hrib") == 2 and save.distinct_found() == 1, "finds counted")
	save.load_data()
	check(save.found_count("hrib") == 2 and save.is_done(1) and save.latest_trail() == 2, "save roundtrip")
	check(save.data.players.hanka.profile == "jezek" and save.look("hanka") == "hanka", "defaults merged")
	check(save.finish_trail(6, 3, "bead") == 0, "last trail has no next")
	save.data = save.defaults()


func test_assets() -> void:
	for id in atlas.order:
		check(ResourceLoader.exists("res://assets/atlas/%s.png" % id), "picture for %s" % id)
	for n in range(1, Config.TRAIL_COUNT + 1):
		var t: Dictionary = atlas.trail(n)
		for st in t.stations:
			check(ResourceLoader.exists("res://assets/bg/%s.png" % st.id), "background %s" % st.id)
		check(ResourceLoader.exists("res://assets/bg/%s.png" % t.finale.id), "finale background %s" % t.finale.id)
		check(ResourceLoader.exists("res://assets/keepsakes/%s.png" % t.keepsake.id), "keepsake %s" % t.keepsake.id)
	var kinds := {}
	for k in Config.COVERS:
		kinds[k] = true
	for st in Config.STATION_COVERS:
		for k in Config.STATION_COVERS[st]:
			kinds[k] = true
	for k in kinds:
		check(ResourceLoader.exists("res://assets/covers/%s.png" % k), "cover %s" % k)
	for f in ["bg/title", "rooms/map", "rooms/atlas", "chars/fabian_stand", "chars/fabian_talk", "chars/fabian_wave", "chars/joey_stand", "chars/joey_sniff", "chars/joey_bark"]:
		check(ResourceLoader.exists("res://assets/%s.png" % f), "art %s" % f)
	for look in Config.LOOKS:
		for mood in ["happy", "cheer", "walk"]:
			check(ResourceLoader.exists("res://assets/chars/%s_%s.png" % [look, mood]), "ranger %s_%s" % [look, mood])
	for u in ["camera", "basket", "herbarium", "sun", "cone_icon", "cone_empty", "lock", "paw", "house", "question"]:
		check(ResourceLoader.exists("res://assets/ui/%s.png" % u), "ui %s" % u)


func frames(n: int) -> void:
	for i in n:
		await get_tree().process_frame


func type_word(trail: Trail, w: String) -> void:
	for ch in w:
		trail._on_char(ch)


func play_trail(n: int, prof: String, lang: String, type_all: bool) -> Trail:
	save.data = save.defaults()
	save.set_lang(lang)
	save.current = "alica"
	save.set_profile("alica", prof)
	save.data.players.alica.unlocked = n
	var trail := Trail.new(n)
	get_tree().root.add_child(trail)
	await frames(2)
	var guard := 0
	while trail.phase != "over" and guard < 1500:
		guard += 1
		trail.cooldown = minf(trail.cooldown, 0.2)
		if trail._dialog:
			trail._next_line()
		if type_all:
			for c in trail.active():
				if c.is_targetable():
					type_word(trail, c.word)
			if trail.finale and trail.finale.progress == 0:
				type_word(trail, trail.finale.word)
		elif trail.finale and trail.finale.progress == 0:
			type_word(trail, trail.finale.word)
		else:
			for c in trail.active():
				c.t = 1.0
		await get_tree().create_timer(0.05).timeout
	print("  trail %d %s/%s typed=%s: phase=%s guard=%d appeared=%d caught=%d new=%d" % [n, prof, lang, type_all, trail.phase, guard, trail.appeared, trail.caught, trail.new_ids.size()])
	return trail


func test_trails() -> void:
	Engine.time_scale = 6.0
	for run in [[1, "veverka", "cs"], [2, "jezek", "cs"], [3, "sova", "cs"], [4, "veverka", "en"], [5, "jezek", "en"], [6, "sova", "en"]]:
		var n: int = run[0]
		var trail := await play_trail(n, run[1], run[2], true)
		var per: int = Config.PROFILES[run[1]].per_station
		check(trail.phase == "over" and save.is_done(n), "trail %d %s: walked to the end" % [n, run[1]])
		check(trail.caught == trail.appeared and trail.appeared >= per * trail.data.stations.size(), "trail %d %s: every find caught (%d/%d)" % [n, run[1], trail.caught, trail.appeared])
		check(save.cones(n) == 3 and save.has_keepsake(trail.data.keepsake.id), "trail %d: three cones and the keepsake" % n)
		check(save.distinct_found() == trail.new_ids.size() and save.distinct_found() > 0, "trail %d: finds saved" % n)
		check(n == Config.TRAIL_COUNT or save.is_unlocked(n + 1), "trail %d: next trail unlocked" % n)
		check(trail._rare_seen.size() >= 1, "trail %d: Joey found something rare" % n)
		trail.queue_free()
		await frames(2)
	var lazy := await play_trail(1, "veverka", "cs", false)
	check(lazy.phase == "over" and save.is_done(1), "doing nothing still reaches Fabián (no fail state)")
	check(lazy.caught == 0 and save.cones(1) == 1 and save.distinct_found() == 0, "nothing typed: one cone, nothing found")
	lazy.queue_free()
	Engine.time_scale = 1.0
	await frames(2)


func test_screens() -> void:
	save.data = save.defaults()
	save.current = "alica"
	save.add_found("hrib")
	save.finish_trail(1, 2, "cone")
	for lang in Text.LANGS:
		save.set_lang(lang)
		for sc in [Screens.Title.new(), Screens.Players.new(), Screens.Map.new(), Screens.Book.new(), Screens.Book.new("basket:0"), Screens.Book.new("treasures")]:
			get_tree().root.add_child(sc)
			await frames(1)
			var texts := []
			for b in sc.find_children("*", "Button", true, false):
				texts.append(b.text)
			check(texts.has("CS") and texts.has("EN"), "%s has language switch" % sc.get_script().resource_path)
			if sc is Screens.Book and sc.tab == "basket":
				sc._detail("hrib")
				await frames(1)
				check(sc.detail != null, "atlas detail opens")
			sc.queue_free()
		await frames(1)
	save.set_lang("cs")


func test_games() -> void:
	save.data = save.defaults()
	save.current = "alica"
	check(save.game_unlocked(0) and not save.game_unlocked(1), "only the first mouse game is open")
	for prof in ["jezek", "veverka", "sova"]:
		save.set_profile("alica", prof)
		for i in Games.ORDER.size():
			var id: String = Games.ORDER[i]
			var g: MiniGame = Games.make(id)
			get_tree().root.add_child(g)
			await frames(2)
			check(g.total > 0, "%s/%s has targets" % [id, prof])
			match id:
				"joey":
					for c in g.cones.duplicate():
						g.collect(c)
				"leaves":
					while g.spawned < g.total:
						g.catch(g.spawn())
				"sort":
					for it in g.items.duplicate():
						g.drop(it, g.camera.position if g._poison(it) else g.basket.position)
				"fog":
					for h in g.buried.duplicate():
						g.reveal(h)
				"orchard":
					for t in g.targets.duplicate():
						g.pick(t)
				"photo":
					while g.spawned < g.total:
						g.snap(g.spawn())
			await frames(3)
			check(g.done and g.got == g.total, "%s/%s finishes when everything is done (%d/%d)" % [id, prof, g.got, g.total])
			check(save.game_cones(id) == 3, "%s/%s perfect play gives three cones" % [id, prof])
			check(i == Games.ORDER.size() - 1 or save.game_unlocked(i + 1), "%s unlocks the next game" % id)
			g.queue_free()
			await frames(1)
	save.set_profile("alica", "veverka")
	var sort: MiniGame = Games.make("sort")
	get_tree().root.add_child(sort)
	await frames(2)
	var it: Sprite2D = sort.items[0]
	sort.drop(it, sort.basket.position if sort._poison(it) else sort.camera.position)
	check(sort.mistakes == 1 and it in sort.items, "wrong drop is a mistake and the item stays")
	sort.queue_free()
	var menu := Screens.GamesMenu.new()
	get_tree().root.add_child(menu)
	await frames(1)
	check(menu.find_children("*", "Button", true, false).size() >= 8, "games menu has its buttons")
	menu.queue_free()
	for l in Text.LANGS:
		for id in Games.ORDER:
			check(ResourceLoader.exists("res://assets/voice/%s/intro_%s.ogg" % [l, id]), "intro voice %s/%s" % [l, id])
	save.data = save.defaults()
