class_name Config
extends RefCounted

const PROFILES := {
	"jezek": {
		"letters": true, "long": false, "max_active": 1, "peek_time": 16.0, "per_station": 4,
		"lenient": true, "keyboard": true, "speak": true,
	},
	"veverka": {
		"letters": false, "long": false, "max_active": 2, "peek_time": 13.0, "per_station": 5,
		"lenient": true, "keyboard": false, "speak": false,
	},
	"sova": {
		"letters": false, "long": true, "max_active": 3, "peek_time": 12.0, "per_station": 6,
		"lenient": false, "keyboard": false, "speak": false,
	},
}
const PROFILE_ORDER := ["jezek", "veverka", "sova"]
const LOOKS := ["alica", "hanka", "tonda"]

const TRAIL_COUNT := 6
const TABS := ["photo", "basket", "herbarium"]
const TAB_OF := {"animal": "photo", "poison": "photo", "mushroom": "basket", "fruit": "basket", "plant": "herbarium"}

const MAP_HOME := Vector2(960, 560)
const MAP := {1: Vector2(1000, 900), 2: Vector2(1350, 230), 3: Vector2(1450, 860), 4: Vector2(400, 700), 5: Vector2(900, 180), 6: Vector2(1700, 540)}
const MAP_FOG := [Vector2(150, 420), Vector2(250, 960)]

const SPOTS := [Vector2(620, 930), Vector2(1010, 880), Vector2(1400, 930), Vector2(1760, 880)]
const SPOTS_KEYBOARD := [Vector2(620, 700), Vector2(1400, 700), Vector2(1760, 1010)]
const COVERS := ["bush", "grass", "log", "fern"]
const STATION_COVERS := {
	"zator": ["bush", "grass", "reeds", "bush"],
	"chumava": ["reeds", "rock", "fern", "reeds"],
	"sut": ["rock", "fern", "rock", "log"],
	"kuchynka": ["rock", "fern", "bush", "log"],
	"provazec": ["log", "fern", "rock", "log"],
	"jezirko": ["reeds", "rock", "reeds", "bush"],
	"plesivec": ["heather", "rock", "heather", "rock"],
	"lsten": ["grass", "bush", "grass", "bush"],
	"pole": ["grass", "reeds", "grass", "bush"],
	"radous": ["bush", "grass", "bush", "grass"],
	"sady": ["grass", "bush", "grass", "log"],
	"ves": ["reeds", "bush", "grass", "reeds"],
	"hrebeny": ["fern", "log", "heather", "fern"],
}

const SPEED_MIN := 0.8
const SPEED_MAX := 1.3
const SPEED_UP := 0.05
const SPEED_DOWN := 0.1
const CLEAN_HITS_FOR_SPEEDUP := 3
const PAWS_FOR_RARE := 4


static func covers_for(station: String) -> Array:
	return STATION_COVERS.get(station, COVERS)


static func cones_for(caught: int, appeared: int) -> int:
	if appeared <= 0:
		return 1
	var r := float(caught) / appeared
	if r >= 0.9:
		return 3
	return 2 if r >= 0.6 else 1
