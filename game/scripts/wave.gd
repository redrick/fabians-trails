class_name Wave
extends RefCounted

var total := 5
var max_active := 2
var spawned := 0
var resolved := 0
var caught := 0
var clean_streak := 0
var paws := 0
var rare_due := false


func _init(profile: Dictionary) -> void:
	total = profile.per_station
	max_active = profile.max_active


func allowed_active() -> int:
	if max_active <= 1:
		return 1
	return max_active if resolved >= 2 else max_active - 1


func wants_spawn(active: int) -> bool:
	return spawned < total and active < allowed_active()


func on_spawn(rare := false) -> void:
	spawned += 1
	if rare:
		rare_due = false


func add_rare() -> void:
	total += 1
	rare_due = true


func on_resolved(was_caught: bool) -> void:
	resolved += 1
	if was_caught:
		caught += 1


func done() -> bool:
	return resolved >= total


func progress() -> float:
	return clampf(float(resolved) / maxi(total, 1), 0.0, 1.0)


func paws_after(was_caught: bool, clean: bool) -> bool:
	if not was_caught:
		paws = 0
		return false
	if clean:
		paws += 1
	if paws >= Config.PAWS_FOR_RARE:
		paws = 0
		return true
	return false


func speed_after(speed: float, was_caught: bool, clean: bool) -> float:
	if not was_caught:
		clean_streak = 0
		return maxf(Config.SPEED_MIN, speed - Config.SPEED_DOWN)
	clean_streak = clean_streak + 1 if clean else 0
	if clean_streak >= Config.CLEAN_HITS_FOR_SPEEDUP:
		clean_streak = 0
		return minf(Config.SPEED_MAX, speed + Config.SPEED_UP)
	return speed
