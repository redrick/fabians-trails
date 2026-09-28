extends Node2D

var screen: Node


func _ready() -> void:
	Input.set_custom_mouse_cursor(load("res://assets/ui/cursor.png"), Input.CURSOR_ARROW, Vector2(5, 5))
	Input.set_custom_mouse_cursor(load("res://assets/ui/cursor_hand.png"), Input.CURSOR_POINTING_HAND, Vector2(14, 6))
	show_screen("title", "")


func show_screen(name: String, arg: String) -> void:
	if screen:
		screen.queue_free()
		Sound.hush()
	match name:
		"players":
			screen = Screens.Players.new()
		"map":
			screen = Screens.Map.new()
		"atlas":
			screen = Screens.Book.new(arg)
		"games":
			screen = Screens.GamesMenu.new()
		"game":
			screen = Games.make(arg)
		"trail":
			screen = Trail.new(int(arg) if arg != "" else 1)
		_:
			screen = Screens.Title.new()
	screen.goto.connect(show_screen, CONNECT_DEFERRED)
	add_child(screen)


func _exit_tree() -> void:
	Input.set_custom_mouse_cursor(null, Input.CURSOR_ARROW)
	Input.set_custom_mouse_cursor(null, Input.CURSOR_POINTING_HAND)
