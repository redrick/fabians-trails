extends Node

const PATH := "user://save.json"
const VERSION := 1

var path := PATH
var data := {}
var current := ""


func _ready() -> void:
	load_data()


func defaults() -> Dictionary:
	return {
		"version": VERSION,
		"players": {
			"alica": new_player("Alica", "veverka", "alica"),
			"hanka": new_player("Hanka", "jezek", "hanka"),
			"host": new_player("Host", "sova", "tonda"),
		},
		"settings": {"sound": true, "music": true, "lang": "cs"},
	}


func new_player(name: String, profile: String, look: String) -> Dictionary:
	return {
		"name": name, "profile": profile, "look": look, "unlocked": 1, "done": [], "found": {}, "cones": {},
		"keepsakes": [], "speed": 1.0, "games": {},
	}


func load_data() -> void:
	data = defaults()
	if not FileAccess.file_exists(path):
		return
	var f := FileAccess.open(path, FileAccess.READ)
	if f == null:
		return
	var parsed = JSON.parse_string(f.get_as_text())
	if parsed is Dictionary and parsed.get("players") is Dictionary:
		for id in parsed.players:
			var p: Dictionary = parsed.players[id]
			var base: Dictionary = data.players.get(id, new_player(str(p.get("name", id)), "veverka", "tonda"))
			base.merge(p, true)
			base.unlocked = int(base.unlocked)
			var done := []
			for n in base.done:
				done.append(int(n))
			base.done = done
			data.players[id] = base
		if parsed.get("settings") is Dictionary:
			data.settings.merge(parsed.settings, true)


func write() -> void:
	var f := FileAccess.open(path, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(data, " "))


func player() -> Dictionary:
	return data.players.get(current, {})


func profile_id() -> String:
	return str(player().get("profile", "veverka"))


func profile() -> Dictionary:
	return Config.PROFILES[profile_id()]


func set_profile(id: String, profile_id: String) -> void:
	data.players[id].profile = profile_id
	write()


func look(id := "") -> String:
	var p: Dictionary = data.players.get(id if id != "" else current, {})
	return str(p.get("look", "tonda"))


func set_look(id: String, look_id: String) -> void:
	data.players[id].look = look_id
	write()


func add_found(id: String) -> bool:
	var found: Dictionary = player().found
	var fresh := not found.has(id)
	found[id] = int(found.get(id, 0)) + 1
	write()
	return fresh


func found_count(id: String) -> int:
	return int(player().get("found", {}).get(id, 0))


func distinct_found(ids: Array = []) -> int:
	var found: Dictionary = player().get("found", {})
	if ids.is_empty():
		return found.size()
	return ids.filter(func(id): return found.has(id)).size()


func is_unlocked(n: int) -> bool:
	return n <= int(player().get("unlocked", 1))


func is_done(n: int) -> bool:
	return n in player().get("done", [])


func finish_trail(n: int, cones: int, keepsake: String) -> int:
	var p := player()
	if not n in p.done:
		p.done.append(n)
	var key := str(n)
	p.cones[key] = maxi(int(p.cones.get(key, 0)), cones)
	if keepsake != "" and not keepsake in p.keepsakes:
		p.keepsakes.append(keepsake)
	var next := 0
	if n < Config.TRAIL_COUNT:
		next = n + 1
		p.unlocked = maxi(int(p.unlocked), next)
	write()
	return next


func cones(n: int) -> int:
	return int(player().get("cones", {}).get(str(n), 0))


func total_cones() -> int:
	var total := 0
	for k in player().get("cones", {}):
		total += int(player().cones[k])
	return total


func has_keepsake(id: String) -> bool:
	return id in player().get("keepsakes", [])


func latest_trail() -> int:
	return clampi(int(player().get("unlocked", 1)), 1, Config.TRAIL_COUNT)


func game_cones(id: String) -> int:
	return int(player().get("games", {}).get(id, 0))


func set_game(id: String, cones: int) -> void:
	var p := player()
	if not p.has("games"):
		p.games = {}
	p.games[id] = maxi(int(p.games.get(id, 0)), cones)
	write()


func game_unlocked(i: int) -> bool:
	return i == 0 or game_cones(Games.ORDER[i - 1]) > 0


func speed() -> float:
	return float(player().get("speed", 1.0))


func set_speed(v: float) -> void:
	player().speed = clampf(v, Config.SPEED_MIN, Config.SPEED_MAX)
	write()


func setting(key: String) -> bool:
	return bool(data.settings.get(key, true))


func set_setting(key: String, v: bool) -> void:
	data.settings[key] = v
	write()


func lang() -> String:
	var l := str(data.settings.get("lang", "cs"))
	return l if l in Text.LANGS else "cs"


func set_lang(l: String) -> void:
	data.settings.lang = l
	write()
