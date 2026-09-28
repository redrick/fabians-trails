# Fabiánova stezka / Fabian's Trail – typing game

A bilingual (CZ/EN) browser typing game for **Alica (7)** and **Hanka (4)**. You walk real autumn trails out of
Hostomice in Brdy with Joey the dog. Animals, mushrooms, fruit and plants peek out from behind bushes and rocks, and
typing the name collects them: animals get photographed, poisonous mushrooms are photo only ("Nesahat!"), edible
things go in the basket, plants into the herbarium. No lives, no fail state: the sun crossing the sky is the clock,
missed things just hide. Each trail ends with Fabián, the Brdy forest spirit, who gives a keepsake. Released on
itch.io (HTML5). Every text is shown in both languages; the chosen language is the one you type.

## Tech stack
- **Godot 4.6.3**, portable binary at `~/apps/godot-4.6/Godot_v4.6.3-stable_linux.x86_64`. GDScript only,
  GL Compatibility renderer, plain Godot (no plugins).
- Web export uses the **single-threaded** template (`variant/thread_support=false`), so itch needs no
  COOP/COEP headers. The export templates must be exactly 4.6.3.
- The engine (typing, keyboard, plaque, save, sound, UI helpers, tests, tools) was copied from
  `~/Projects/godot/pirates-ahoy` and adapted; the two repos don't share code.

## Layout
- `game/` – the Godot project (`res://`).
  - `scripts/main.gd` swaps screens. Each screen is a Node2D built in code that emits `goto(screen, arg)`:
    `Screens.Title/Players/Map/Book` (`screens.gd`; Book is the atlas) and `Trail` (`trail.gd`, the gameplay).
  - `trail.gd` runs one trail: stations (a stage = backdrop + covers + critters, slides away on the walk to the
    next one), the sun, Joey's paw meter and rare finds, the flights to camera/basket/herbarium, Fabián's finale
    and the summary. `critter.gd` is one find peeking from behind a cover (clip rect + slide), plus
    `Critter.Finale`, the plaque Fabián holds up. `wave.gd` paces one station.
  - Joey's games (mouse mini-games): `minigame.gd` is the base (intro voice, ghost-hand demo, counter, result), and
    `games.gd` holds the six games plus `Games.make(id)`; `Screens.GamesMenu` lists them, and each unlocks the next.
  - `typing.gd` holds the typing logic (lock the one closest to hiding by first letter, lenient accent folding, a
    miss keeps progress, Esc/Backspace releases the lock).
  - `config.gd` defines the ranks (Ježek / Veverka / Sova = Hedgehog / Squirrel / Owl), cover spots, map spots.
  - Autoloads: `Save` (`user://save.json`, IndexedDB on the web), `Sound` (synthesised SFX, forest ambience, voice
    `.ogg` files in `assets/voice/<lang>/`) and `Atlas` (the data below).
  - `text.gd` has every UI string in CS + EN (`Text.t` = chosen language, `Text.o` = the other one);
    `UI.bilabel`/`UI.tbutton` show only the chosen one while `UI.BILINGUAL` is false.
  - `data/facts_*.txt`: one kid-level fact per entry (`id | cs | en`), shown and voiced on the atlas card.
  - `data/atlas.txt`: one entry per line, `id | cs | en | cs long | en long | category | flags`. Short names are
    typed by Veverka, long ones by Sova, Ježek types the first letter. `data/trails/<n>.txt`: stations with their
    finds, rare finds (Joey), finale, Fabián's lines, keepsake. Plain text, exported via `include_filter="data/*"`.
    Names avoid Ď Ť Ň Ó (dead keys), hyphens and apostrophes; the tests enforce it.
  - `assets/` holds exported PNGs (`atlas/<id>`, `bg/<station>`, `covers/`, `chars/`, `keepsakes/`, `ui/`,
    `rooms/`), the voice files and the fonts. Missing art shows as a coloured placeholder circle.
- `art/` – Python-drawn art (reportlab, the "ligne claire" lib copied from the detective game). One module per
  group: `people` (rangers, Joey), `fabian` (Fabián, covers, keepsakes, UI icons), `animals`, `fungi`, `plants`,
  `places_a`/`places_b` (backgrounds, map, atlas book). Run
  `art/.venv/bin/python art/export_assets.py [--module name] [name-filter]`, then reimport.
- `tools/make_voice.sh` – CZ/EN voice lines with Piper neural TTS (Czech `cs_CZ-jirka-medium`, English
  `en_GB-alba-medium`), read from the data files; sets up `tools/.piper` (venv + models, gitignored) on first run and
  takes ~3 min. Reimport afterwards. Recordings replace the files one for one, keeping the same names.
- `assets/music/track_1..3.ogg` – Kevin MacLeod, CC BY 4.0 (see `CREDITS.txt`, credited on the title screen).
  `Sound` plays them as a playlist and ducks them while a voice line plays.

## Commands
```
GD=~/apps/godot-4.6/Godot_v4.6.3-stable_linux.x86_64
$GD --path game                                   # play
$GD --headless --import --path game               # after exporting art
$GD --headless --path game res://tests/run.tscn   # tests (exit code 1 on failure)
tools/build_web.sh && tools/serve_web.sh          # web build → http://localhost:8060/index.html
tools/build_desktop.sh                            # Linux + Windows builds and zips in build/
```
