class_name Text
extends RefCounted

const LANGS := ["cs", "en"]

const STRINGS := {
	"title": ["Fabiánova stezka", "Fabian's Trail"],
	"play": ["Hrát", "Play"],
	"who": ["Kdo dnes jde na stezku?", "Who's walking the trail today?"],
	"guest": ["Host", "Guest"],
	"back": ["Zpět", "Back"],
	"map": ["Mapa", "Map"],
	"again": ["Znovu", "Again"],
	"next": ["Dál", "Next"],
	"atlas": ["Atlas", "Atlas"],
	"look": ["Strážce", "Ranger"],
	"tab_photo": ["Fotky", "Photos"],
	"tab_basket": ["Košík", "Basket"],
	"tab_herbarium": ["Herbář", "Herbarium"],
	"tab_treasures": ["Poklady", "Treasures"],
	"found": ["Nalezeno %d z %d", "Found %d of %d"],
	"new": ["Nový!", "New!"],
	"new_count": ["Nové do atlasu: %d", "New in the atlas: %d"],
	"dont_touch": ["Nesahat! Jen fotit.", "Don't touch! Photo only."],
	"sunset": ["Slunce zapadá.", "The sun is setting."],
	"trail_done": ["Stezka je hotová!", "Trail complete!"],
	"next_trail": ["Nová stezka: %s", "New trail: %s"],
	"all_done": ["Prošel jsi všechny stezky!", "You walked every trail!"],
	"gift": ["Dárek: %s", "Gift: %s"],
	"locked": ["Zamčeno", "Locked"],
	"soon": ["Brzy", "Soon"],
	"where": ["Stezka: %s", "Trail: %s"],
	"trail_n": ["Stezka %d", "Trail %d"],
	"cones": ["Šišky od Fabiána: %d", "Cones from Fabián: %d"],
	"treasures": ["Poklady z cest", "Trail treasures"],
	"not_found": ["Ještě nenalezeno", "Not found yet"],
	"rare": ["Vzácné", "Rare"],
	"cat_animal": ["Zvíře", "Animal"],
	"cat_poison": ["Jedovatá houba", "Poisonous mushroom"],
	"cat_mushroom": ["Jedlá houba", "Edible mushroom"],
	"cat_fruit": ["Plody", "Fruit and nuts"],
	"cat_plant": ["Rostlina", "Plant"],
	"music_credit": ["Hudba: Kevin MacLeod (incompetech.com), CC BY 4.0", "Music: Kevin MacLeod (incompetech.com), CC BY 4.0"],
	"music": ["Hudba", "Music"],
	"type_sign": ["Napiš, co je na cedulce!", "Type what's on the sign!"],
	"press_letter": ["Zmáčkni písmenko z cedulky!", "Press the letter on the sign!"],
	"games": ["Joeyho hry", "Joey's games"],
	"game_done": ["Hotovo!", "All done!"],
	"game_joey": ["Joey na stopě", "Joey on the trail"],
	"game_leaves": ["Padající listí", "Falling leaves"],
	"game_sort": ["Co patří do košíku?", "What goes in the basket?"],
	"game_fog": ["Mlha na Plešivci", "Fog on Plešivec"],
	"game_orchard": ["V sadu", "In the orchard"],
	"game_photo": ["Fotolov", "Photo hunt"],
	"how_joey": ["Veď Joeyho myší a najdi všechny šišky.", "Lead Joey with the mouse and find all the cones."],
	"how_leaves": ["Klikni na listy, než dopadnou na zem.", "Click the leaves before they land."],
	"how_sort": ["Chyť věc a přetáhni ji. Jedlé do košíku, jedovaté k foťáku.", "Grab a thing and drag it. Food goes in the basket, poisonous things to the camera."],
	"how_fog": ["Drž tlačítko a rozháněj mlhu. Co se pod ní schovává?", "Hold the button and wipe the fog away. What is hiding under it?"],
	"how_orchard": ["Klikni dvakrát rychle za sebou na jablko nebo ořech.", "Click twice quickly on an apple or a walnut."],
	"how_photo": ["Zamiř rámečkem na ptáka a klikni.", "Point the frame at a bird and click."],
	"skill_joey": ["Pohyb myší", "Moving the mouse"],
	"skill_leaves": ["Klikání", "Clicking"],
	"skill_sort": ["Chyť a pusť", "Drag and drop"],
	"skill_fog": ["Drž a táhni", "Hold and move"],
	"skill_orchard": ["Dvojklik", "Double click"],
	"skill_photo": ["Pohyblivý cíl", "Moving targets"],
	"keys": ["Kouzelné klávesy", "Magic keys"],
	"clipboard": ["Schránka", "Clipboard"],
	"game_copy": ["Sázíme stromky", "Planting trees"],
	"game_cut": ["Kdo kde bydlí?", "Who lives where?"],
	"game_undo": ["Zlobivá sojka", "The naughty jay"],
	"game_rake": ["Hrabání listí", "Raking leaves"],
	"game_drill": ["Rychlé klávesy", "Quick keys"],
	"how_copy": ["Klikni na stromek a zmáčkni Ctrl + C. Pak klikni na prázdné místo a zmáčkni Ctrl + V.", "Click a tree and press Ctrl + C. Then click an empty spot and press Ctrl + V."],
	"how_cut": ["Klikni na zvíře a zmáčkni Ctrl + X. Pak klikni na jeho stín a zmáčkni Ctrl + V.", "Click an animal and press Ctrl + X. Then click its shadow and press Ctrl + V."],
	"how_undo": ["Sojka dělá nepořádek. Zmáčkni Ctrl + Z a vrať všechno zpátky.", "The jay makes a mess. Press Ctrl + Z to put everything back."],
	"how_rake": ["Zmáčkni Ctrl + A a vyber všechno listí. Pak ho smaž klávesou Delete.", "Press Ctrl + A to select all the leaves. Then press Delete to clear them away."],
	"how_drill": ["Co se má stát? Zmáčkni správnou zkratku.", "What should happen? Press the right shortcut."],
	"skill_copy": ["Ctrl + C, Ctrl + V", "Ctrl + C, Ctrl + V"],
	"skill_cut": ["Ctrl + X, Ctrl + V", "Ctrl + X, Ctrl + V"],
	"skill_undo": ["Ctrl + Z", "Ctrl + Z"],
	"skill_rake": ["Ctrl + A, Delete", "Ctrl + A, Delete"],
	"skill_drill": ["Všechny zkratky", "All the shortcuts"],
	"key_copy": ["Kopírovat", "Copy"],
	"key_paste": ["Vložit", "Paste"],
	"key_cut": ["Vyjmout", "Cut"],
	"key_undo": ["Zpět", "Undo"],
	"key_selectall": ["Vybrat vše", "Select all"],
	"key_save": ["Uložit", "Save"],
	"key_find": ["Najít", "Find"],
	"key_print": ["Tisk", "Print"],
	"key_rename": ["Přejmenovat", "Rename"],
	"key_delete": ["Smazat", "Delete"],
	"key_closetab": ["Zavřít kartu", "Close tab"],
	"key_newtab": ["Nová karta", "New tab"],
	"key_newwindow": ["Nové okno", "New window"],
	"key_switch": ["Přepnout okno", "Switch window"],
	"key_close": ["Zavřít program", "Close program"],
	"note_switch": ["Přepni do jiného okna a zase zpátky.", "Switch to another window and back."],
	"skip": ["Přeskočit", "Skip"],
	"note_close": ["Neboj, hra se nezavře.", "Don't worry, the game won't close."],
	"race": ["Závod se sluncem", "Race the sun"],
	"race_hint": ["Projdi stezku, než zapadne slunce!", "Finish the trail before sunset!"],
	"race_go": ["Teď!", "Go!"],
	"race_won": ["Hotovo včas!", "Made it in time!"],
	"time_up": ["Slunce zapadlo!", "The sun has set!"],
	"race_time": ["Čas: %s", "Time: %s"],
	"race_best": ["Nejlepší čas: %s", "Best time: %s"],
	"new_record": ["Nový rekord!", "New record!"],
	"medal_1": ["Bronzová medaile", "Bronze medal"],
	"medal_2": ["Stříbrná medaile", "Silver medal"],
	"medal_3": ["Zlatá medaile", "Gold medal"],
	"rank_jezek":["Ježek", "Hedgehog"],
	"rank_veverka": ["Veverka", "Squirrel"],
	"rank_sova": ["Sova", "Owl"],
}


static func lang() -> String:
	return Save.lang()


static func other_lang(l := "") -> String:
	var here := l if l != "" else lang()
	return LANGS[(LANGS.find(here) + 1) % LANGS.size()]


static func t(key: String, lang_id := "") -> String:
	var i := LANGS.find(lang_id if lang_id != "" else lang())
	return STRINGS[key][maxi(i, 0)]


static func o(key: String) -> String:
	return t(key, other_lang())


static func pick(pair: Dictionary, lang_id := "") -> String:
	return str(pair.get(lang_id if lang_id != "" else lang(), ""))


static func rank(id: String, lang_id := "") -> String:
	return t("rank_" + id, lang_id)


static func player_name(id: String) -> String:
	return t("guest") if id == "host" else str(Save.data.players[id].name)
