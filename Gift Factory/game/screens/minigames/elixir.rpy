screen shelf_elixir:
    add "images/minigames/backgrounds/basic_background.png"

    imagebutton:
        idle "images/minigames/murim/box_close.png"
        pos (1500, 600)
        action Return(-1)

    add "images/minigames/backgrounds/shelf.png"

screen box_elixir:
    add "images/minigames/backgrounds/basic_background.png"

    imagebutton:
        idle "images/minigames/murim/box_close.png"
        align (0.5, 0.5)
        action Return(-1)

screen elixir:
    add "images/minigames/backgrounds/basic_background.png"

    add "images/minigames/murim/box_open.png" at truecenter

    imagebutton:
        idle "images/minigames/murim/elixir.png"
        align (0.5, 0.5)
        action Return(-1)