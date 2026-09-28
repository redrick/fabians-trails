extends Node

const RATE := 22050
const VOICE_DIR := "res://assets/voice/"
const MUSIC := ["res://assets/music/track_1.ogg", "res://assets/music/track_2.ogg", "res://assets/music/track_3.ogg"]

var sfx := {}
var _players: Array[AudioStreamPlayer] = []
var _voice := AudioStreamPlayer.new()
var _forest := AudioStreamPlayer.new()
var _music := AudioStreamPlayer.new()
var _track := -1
var _queue := []


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	for i in 6:
		var p := AudioStreamPlayer.new()
		add_child(p)
		_players.append(p)
	add_child(_voice)
	add_child(_forest)
	add_child(_music)
	_forest.volume_db = -16.0
	_music.volume_db = -8.0
	_music.finished.connect(_next_track)
	_voice.finished.connect(_voice_done)
	sfx = {
		"boing": _tone(0.32, func(t): return 320.0 * exp(-t * 3.0) + 110.0, 0.5, "sine", 7.0),
		"pop": _tone(0.07, func(_t): return 760.0, 0.35, "sine", 0.0),
		"lock": _tone(0.12, func(t): return 500.0 + t * 3000.0, 0.25, "triangle", 0.0),
		"shutter": _noise(0.09, 0.5),
		"plop": _tone(0.16, func(t): return 520.0 - t * 1800.0, 0.45, "sine", 0.0),
		"press": _tone(0.25, func(t): return 180.0 - t * 200.0, 0.4, "triangle", 0.0),
		"bark": _tone(0.22, func(t): return 420.0 * exp(-t * 4.0) + 160.0, 0.35, "saw", 0.0),
		"sniff": _noise(0.4, 0.12),
		"chime": _notes([1319.0, 1760.0, 2093.0], 0.07, 0.25),
		"jingle": _notes([1047.0, 1319.0, 1568.0, 2093.0], 0.09, 0.3),
		"fanfare": _notes([523.0, 659.0, 784.0, 1047.0, 784.0, 1047.0], 0.14, 0.35),
		"whoosh": _noise(0.5, 0.18),
	}
	_forest.stream = _forest_loop()


func _process(delta: float) -> void:
	var target := -16.0 if _voice.playing else -8.0
	_music.volume_db = move_toward(_music.volume_db, target, delta * 20.0)


func play(name: String) -> void:
	if not Save.setting("sound") or not sfx.has(name):
		return
	for p in _players:
		if not p.playing:
			p.stream = sfx[name]
			p.play()
			return
	_players[0].stream = sfx[name]
	_players[0].play()


func voice_path(key: String) -> String:
	return VOICE_DIR + Save.lang() + "/" + key + ".ogg"


func has_voice(key: String) -> bool:
	return ResourceLoader.exists(voice_path(key))


func voice_path_in(key: String, lang: String) -> String:
	return VOICE_DIR + lang + "/" + key + ".ogg"


func say(key: String, lang := "") -> void:
	_queue.clear()
	_play_voice(key, lang)


func say_all(keys: Array, lang := "") -> void:
	_queue.clear()
	for k in keys.slice(1):
		_queue.append([k, lang])
	_play_voice(keys[0], lang)


func _play_voice(key: String, lang: String) -> void:
	var path := voice_path_in(key, lang if lang != "" else Save.lang())
	if not Save.setting("sound") or not ResourceLoader.exists(path):
		return
	_voice.stream = load(path)
	_voice.play()


func _voice_done() -> void:
	if not _queue.is_empty():
		var next: Array = _queue.pop_front()
		get_tree().create_timer(0.35).timeout.connect(func(): _play_voice(next[0], next[1]))


func hush() -> void:
	_queue.clear()
	_voice.stop()


func say_after(key: String, lang: String, delay: float) -> void:
	get_tree().create_timer(delay).timeout.connect(func(): say(key, lang))


func speaking() -> bool:
	return _voice.playing


func letter_key(ch: String) -> String:
	return "letter_" + Typing.fold(ch)


func start_ambience() -> void:
	if Save.setting("sound") and not _forest.playing:
		_forest.play()
	if Save.setting("music") and not _music.playing:
		_next_track()


func _next_track() -> void:
	if not Save.setting("music"):
		return
	_track = (_track + 1) % MUSIC.size()
	if ResourceLoader.exists(MUSIC[_track]):
		_music.stream = load(MUSIC[_track])
		_music.play()


func set_music(on: bool) -> void:
	Save.set_setting("music", on)
	if on:
		_next_track()
	else:
		_music.stop()


func stop_ambience() -> void:
	_forest.stop()
	_music.stop()


func _wav(samples: PackedFloat32Array, loop := false) -> AudioStreamWAV:
	var bytes := PackedByteArray()
	bytes.resize(samples.size() * 2)
	for i in samples.size():
		bytes.encode_s16(i * 2, int(clampf(samples[i], -1.0, 1.0) * 32000.0))
	var w := AudioStreamWAV.new()
	w.format = AudioStreamWAV.FORMAT_16_BITS
	w.mix_rate = RATE
	w.data = bytes
	if loop:
		w.loop_mode = AudioStreamWAV.LOOP_FORWARD
		w.loop_end = samples.size()
	return w


func _osc(kind: String, phase: float) -> float:
	var f := fposmod(phase, 1.0)
	match kind:
		"square":
			return 1.0 if f < 0.5 else -1.0
		"saw":
			return f * 2.0 - 1.0
		"triangle":
			return 1.0 - absf(f * 4.0 - 2.0)
	return sin(phase * TAU)


func _tone(dur: float, freq: Callable, vol: float, kind: String, trem: float) -> AudioStreamWAV:
	var n := int(dur * RATE)
	var out := PackedFloat32Array()
	out.resize(n)
	var phase := 0.0
	for i in n:
		var t := float(i) / RATE
		phase += freq.call(t) / RATE
		var env := minf(1.0, t * 80.0) * pow(1.0 - t / dur, 1.5)
		var am := 1.0 if trem == 0.0 else 0.6 + 0.4 * sin(t * trem * TAU)
		out[i] = _osc(kind, phase) * env * am * vol
	return _wav(out)


func _notes(freqs: Array, step: float, vol: float) -> AudioStreamWAV:
	var dur := step * freqs.size() + 0.4
	var n := int(dur * RATE)
	var out := PackedFloat32Array()
	out.resize(n)
	for k in freqs.size():
		var start := int(k * step * RATE)
		for i in range(start, n):
			var t := float(i - start) / RATE
			var env := exp(-t * 6.0)
			out[i] += (sin(t * freqs[k] * TAU) + 0.3 * sin(t * freqs[k] * 2.0 * TAU)) * env * vol
	return _wav(out)


func _noise(dur: float, vol: float) -> AudioStreamWAV:
	var n := int(dur * RATE)
	var out := PackedFloat32Array()
	out.resize(n)
	var lp := 0.0
	for i in n:
		var t := float(i) / RATE
		lp = lerpf(lp, randf_range(-1.0, 1.0), 0.15)
		out[i] = lp * vol * 3.0 * minf(1.0, t * 40.0) * (1.0 - t / dur)
	return _wav(out)


func _forest_loop() -> AudioStreamWAV:
	var dur := 8.0
	var n := int(dur * RATE)
	var out := PackedFloat32Array()
	out.resize(n)
	var lp := 0.0
	for i in n:
		var t := float(i) / RATE
		lp = lerpf(lp, randf_range(-1.0, 1.0), 0.02)
		out[i] = lp * (0.5 + 0.5 * sin(t / dur * TAU * 3.0)) * 0.9
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	for k in 9:
		var start := rng.randf_range(0.2, dur - 1.0)
		var base := rng.randf_range(2600.0, 4200.0)
		var notes := rng.randi_range(2, 5)
		for j in notes:
			var s0 := int((start + j * 0.11) * RATE)
			for i in int(0.08 * RATE):
				var tt := float(i) / RATE
				var f := base + sin(tt * 90.0) * 400.0 - j * 120.0
				if s0 + i < n:
					out[s0 + i] += sin(tt * f * TAU) * 0.08 * sin(PI * tt / 0.08)
	for i in 2000:
		var k := float(i) / 2000.0
		out[i] *= k
		out[n - 1 - i] *= k
	return _wav(out, true)
