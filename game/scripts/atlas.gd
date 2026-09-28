extends Node

const ATLAS := "res://data/atlas.txt"
const TRAILS := "res://data/trails/%d.txt"
const FACTS := ["res://data/facts_animals.txt", "res://data/facts_fungi.txt", "res://data/facts_plants.txt"]

var entries := {}
var order: Array[String] = []
var trails := {}
var _bags := {}


func _ready() -> void:
	load_all()


func load_all() -> void:
	entries.clear()
	order.clear()
	trails.clear()
	for cols in _rows(ATLAS):
		var e := {
			"id": cols[0], "cs": cols[1], "en": cols[2], "cs_long": cols[3], "en_long": cols[4], "cat": cols[5],
			"rare": false, "sova": false,
		}
		for flag in cols.slice(6):
			e[flag] = true
		entries[e.id] = e
		order.append(e.id)
	for n in range(1, Config.TRAIL_COUNT + 1):
		trails[n] = _read_trail(n)
	for path in FACTS:
		for cols in _rows(path):
			if entries.has(cols[0]) and cols.size() >= 3:
				entries[cols[0]].fact = {"cs": cols[1], "en": cols[2]}


func _rows(path: String) -> Array:
	var out := []
	var f := FileAccess.open(path, FileAccess.READ)
	if f == null:
		return out
	for line in f.get_as_text().split("\n"):
		var l := line.strip_edges()
		if l.is_empty() or l.begins_with("#"):
			continue
		var cols := []
		for c in l.split("|"):
			cols.append(c.strip_edges())
		out.append(cols)
	return out


func _read_trail(n: int) -> Dictionary:
	var t := {"n": n, "stations": [], "rare": [], "fabian": []}
	for cols in _rows(TRAILS % n):
		match cols[0]:
			"name":
				t.name = {"cs": cols[1], "en": cols[2]}
			"station":
				t.stations.append({"id": cols[1], "cs": cols[2], "en": cols[3], "finds": Array(cols[4].split(" ", false))})
			"rare":
				t.rare = Array(cols[1].split(" ", false))
			"finale":
				t.finale = {"id": cols[1], "cs": cols[2], "en": cols[3]}
			"target":
				t.target = {"cs": cols[1], "en": cols[2]}
			"target_sova":
				t.target_sova = {"cs": cols[1], "en": cols[2]}
			"fabian":
				t.fabian.append({"cs": cols[1], "en": cols[2]})
			"thanks":
				t.thanks = {"cs": cols[1], "en": cols[2]}
			"keepsake":
				t.keepsake = {"id": cols[1], "cs": cols[2], "en": cols[3]}
	return t


func entry(id: String) -> Dictionary:
	return entries.get(id, {})


func fact(id: String, lang := "") -> String:
	return str(entry(id).get("fact", {}).get(lang if lang != "" else Save.lang(), ""))


func trail(n: int) -> Dictionary:
	return trails.get(n, {})


func name_of(id: String, lang := "", long := false) -> String:
	var e := entry(id)
	var l := lang if lang != "" else Save.lang()
	return str(e.get(l + "_long" if long else l, ""))


func word_for(id: String, profile_id: String, lang := "") -> String:
	var p: Dictionary = Config.PROFILES[profile_id]
	var w := name_of(id, lang, p.long)
	return Typing.fold(w[0]) if p.letters else w


func translation_pair(id: String, profile_id: String) -> Array:
	var long: bool = Config.PROFILES[profile_id].long
	return [name_of(id, Save.lang(), long), name_of(id, Text.other_lang(), long)]


func target_for(n: int, profile_id: String, lang := "") -> String:
	var t := trail(n)
	var l := lang if lang != "" else Save.lang()
	var p: Dictionary = Config.PROFILES[profile_id]
	if p.long:
		return t.target_sova[l]
	var w: String = t.target[l]
	return Typing.fold(w[0]) if p.letters else w


func finds_for(n: int, station: int, profile_id: String) -> Array:
	var out := []
	for id in trail(n).stations[station].finds:
		if entry(id).sova and profile_id != "sova":
			continue
		out.append(id)
	return out


func pick(n: int, station: int, profile_id: String, avoid: Array = []) -> String:
	var key := "%d/%d/%s" % [n, station, profile_id]
	var bag: Array = _bags.get(key, [])
	if bag.is_empty():
		bag = finds_for(n, station, profile_id)
		bag.shuffle()
		_bags[key] = bag
	if bag.is_empty():
		return ""
	for i in bag.size():
		if not _first(bag[i], profile_id) in avoid:
			return bag.pop_at(i)
	return bag.pop_back()


func pick_rare(n: int, avoid: Array = []) -> String:
	var pool: Array = trail(n).rare.filter(func(id): return not id in avoid)
	if pool.is_empty():
		return ""
	var fresh := pool.filter(func(id): return Save.found_count(id) == 0)
	return (fresh if not fresh.is_empty() else pool).pick_random()


func _first(id: String, profile_id: String) -> String:
	return Typing.fold(word_for(id, profile_id)[0])


func first_letter(id: String, profile_id: String) -> String:
	return _first(id, profile_id)


func reset() -> void:
	_bags.clear()


func trails_of(id: String) -> Array:
	var out := []
	for n in trails:
		var t: Dictionary = trails[n]
		var here: bool = id in t.rare
		for s in t.stations:
			here = here or id in s.finds
		if here:
			out.append(n)
	return out


func ids_in_tab(tab: String) -> Array:
	return order.filter(func(id): return Config.TAB_OF[entries[id].cat] == tab)


func station_count(n: int) -> int:
	return trail(n).stations.size()
