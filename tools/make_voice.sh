#!/usr/bin/env bash
# Voice lines with Piper neural TTS -> game/assets/voice/<lang>/*.ogg, read from the game data.
# Czech = cs_CZ-jirka-medium, English = en_GB-alba-medium. Sets up tools/.piper (venv + models) on first run.
# Real recordings (Andrej/Alica) replace these files one-for-one, same names.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=game/assets/voice
DATA=game/data
PIPER=tools/.piper
MODELS="https://huggingface.co/rhasspy/piper-voices/resolve/main"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [ ! -x "$PIPER/bin/python" ]; then
	python3 -m venv "$PIPER"
	"$PIPER/bin/pip" install -q piper-tts
fi
mkdir -p "$PIPER/voices"
for v in cs/cs_CZ/jirka/medium/cs_CZ-jirka-medium en/en_GB/alba/medium/en_GB-alba-medium; do
	n=$(basename "$v")
	[ -f "$PIPER/voices/$n.onnx" ] || curl -sfL -o "$PIPER/voices/$n.onnx" "$MODELS/$v.onnx"
	[ -f "$PIPER/voices/$n.onnx.json" ] || curl -sfL -o "$PIPER/voices/$n.onnx.json" "$MODELS/$v.onnx.json"
done

say() {
	"$PIPER/bin/python" -m piper -m "$PIPER/voices/$VOICE.onnx" -f "$TMP/$1.wav" --length-scale "${SLOW:-1.0}" -- "$2"
	ffmpeg -loglevel error -y -i "$TMP/$1.wav" -af "silenceremove=start_periods=1:start_threshold=-50dB,loudnorm=I=-18:TP=-2" -ar 22050 -c:a libvorbis -q:a 4 "$OUT/$1.ogg"
}

cap() { sed -E 's/^(.)(.*)$/\1\L\2/'; }

data_lines() {
	grep -v '^#' "$DATA/atlas.txt" | awk -F'|' -v c="$1" 'NF>5 {gsub(/^ +| +$/, "", $1); gsub(/^ +| +$/, "", $c); print $1 "|" $c}'
}

fact_lines() {
	cat "$DATA"/facts_*.txt | grep -v '^#' | awk -F'|' -v c="$1" 'NF>2 {gsub(/^ +| +$/, "", $1); gsub(/^ +| +$/, "", $c); print "fact_" $1 "|" $c}'
}

trail_lines() {
	for f in "$DATA"/trails/*.txt; do
		n=$(basename "$f" .txt)
		awk -F'|' -v c="$1" -v n="$n" '
			{gsub(/^ +| +$/, "", $1); gsub(/^ +| +$/, "", $c)}
			$1 == "fabian" {print "fabian_" n "_" i++ "|" $c}
			$1 == "thanks" {print "thanks_" n "|" $c}' "$f"
	done
}

voice_lang() {
	local col=$1
	OUT="$ROOT/$LANG_ID"; mkdir -p "$OUT"; rm -f "$OUT"/*.ogg
	for k in "${!LETTERS[@]}"; do say "letter_$k" "${LETTERS[$k]}"; done
	for k in "${!UI[@]}"; do say "$k" "${UI[$k]}"; done
	while IFS='|' read -r id name; do say "name_$id" "$(echo "$name" | cap)."; done < <(data_lines "$col")
	while IFS='|' read -r id line; do say "$id" "$line"; done < <(fact_lines "$col")
	SLOW=1.1
	while IFS='|' read -r id line; do say "$id" "$line"; done < <(trail_lines "$col")
	SLOW=1.0
}

LANG_ID=cs; VOICE=cs_CZ-jirka-medium
declare -A LETTERS=(
	[A]="á" [B]="bé" [C]="cé" [D]="dé" [E]="é" [F]="ef" [G]="gé" [H]="há" [I]="í" [J]="jé"
	[K]="ká" [L]="el" [M]="em" [N]="en" [O]="ó" [P]="pé" [Q]="kvé" [R]="er" [S]="es" [T]="té"
	[U]="ú" [V]="vé" [W]="dvojité vé" [X]="iks" [Y]="ypsilon" [Z]="zet"
)
declare -A UI=(
	[ui_who]="Kdo dnes jde na stezku?"
	[ui_map]="Vyber si stezku."
	[ui_joey]="Joey něco vyčenichal!"
	[ui_dont_touch]="Nesahat! Tuhle houbu jenom vyfotíme."
	[ui_done]="Hurá! Stezka je hotová!"
	[ui_type_sign]="Napiš, co je na cedulce!"
	[ui_press_letter]="Zmáčkni písmenko z cedulky!"
	[ui_wrong_place]="Tahle patří jinam."
	[ui_game_done]="Hotovo! Šikula!"
	[intro_joey]="Veď Joeyho myší a najdi všechny šišky."
	[intro_leaves]="Klikni na listy, než dopadnou na zem."
	[intro_sort]="Chyť věc a přetáhni ji. Jedlé do košíku, jedovaté k foťáku."
	[intro_fog]="Drž tlačítko a rozháněj mlhu. Co se pod ní schovává?"
	[intro_orchard]="Klikni dvakrát rychle za sebou na jablko nebo ořech."
	[intro_photo]="Zamiř rámečkem na ptáka a klikni."
)
voice_lang 2

LANG_ID=en; VOICE=en_GB-alba-medium
LETTERS=(
	[A]="ay" [B]="bee" [C]="see" [D]="dee" [E]="ee" [F]="eff" [G]="jee" [H]="aitch" [I]="eye" [J]="jay"
	[K]="kay" [L]="ell" [M]="em" [N]="en" [O]="oh" [P]="pee" [Q]="queue" [R]="ar" [S]="ess" [T]="tee"
	[U]="you" [V]="vee" [W]="double you" [X]="ex" [Y]="why" [Z]="zed"
)
UI=(
	[ui_who]="Who's walking the trail today?"
	[ui_map]="Pick a trail."
	[ui_joey]="Joey sniffed something out!"
	[ui_dont_touch]="Don't touch! We only take a photo of this mushroom."
	[ui_done]="Hooray! The trail is complete!"
	[ui_type_sign]="Type what's on the sign!"
	[ui_press_letter]="Press the letter on the sign!"
	[ui_wrong_place]="That one goes somewhere else."
	[ui_game_done]="All done! Well done!"
	[intro_joey]="Lead Joey with the mouse and find all the cones."
	[intro_leaves]="Click the leaves before they land."
	[intro_sort]="Grab a thing and drag it. Food goes in the basket, poisonous things to the camera."
	[intro_fog]="Hold the button and wipe the fog away. What is hiding under it?"
	[intro_orchard]="Click twice quickly on an apple or a walnut."
	[intro_photo]="Point the frame at a bird and click."
)
voice_lang 3

echo "wrote $(ls "$ROOT"/*/*.ogg | wc -l) files to $ROOT"
