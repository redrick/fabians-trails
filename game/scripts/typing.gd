class_name Typing
extends RefCounted

enum Result { IGNORED, LOCKED, ADVANCED, COMPLETED, MISS }

const FOLD := {
	"Á": "A", "Č": "C", "Ď": "D", "É": "E", "Ě": "E", "Í": "I", "Ň": "N", "Ó": "O",
	"Ř": "R", "Š": "S", "Ť": "T", "Ú": "U", "Ů": "U", "Ý": "Y", "Ž": "Z",
}

var lenient := true
var targets: Array = []
var locked: Object = null


static func normalize(ch: String) -> String:
	return ch.to_upper()


static func fold(ch: String) -> String:
	var up := ch.to_upper()
	return FOLD.get(up, up)


static func char_from_event(ev: InputEvent) -> String:
	if not (ev is InputEventKey) or not ev.pressed or ev.echo:
		return ""
	if ev.unicode < 32:
		return ""
	return String.chr(ev.unicode)


func same(expected: String, typed: String) -> bool:
	if lenient:
		return fold(expected) == fold(typed)
	return normalize(expected) == normalize(typed)


func add(t: Object) -> void:
	targets.append(t)


func remove(t: Object) -> void:
	targets.erase(t)
	if locked == t:
		locked = null


func release() -> void:
	if locked:
		locked.progress = 0
		locked.on_progress()
	locked = null


func handle(ch: String) -> Result:
	if ch.is_empty():
		return Result.IGNORED
	if locked == null:
		var best: Object = null
		for t in targets:
			if not t.is_targetable():
				continue
			if same(t.word[0], ch) and (best == null or t.closeness() > best.closeness()):
				best = t
		if best == null:
			return Result.MISS
		locked = best
		return _advance()
	if same(locked.word[locked.progress], ch):
		return _advance()
	locked.on_miss()
	return Result.MISS


func _advance() -> Result:
	var t: Object = locked
	t.progress += 1
	t.on_progress()
	if t.progress >= t.word.length():
		locked = null
		targets.erase(t)
		t.on_complete()
		return Result.COMPLETED
	return Result.LOCKED if t.progress == 1 else Result.ADVANCED
