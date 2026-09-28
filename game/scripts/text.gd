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
	"rank_jezek": ["Ježek", "Hedgehog"],
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
