default gloves_chosen = None

init python:
    def choose_glove(glove):
        store.gloves_chosen = glove
        return glove

screen shelf_boxing:
    add "images/minigames/backgrounds/basic_background.png"
    add "images/minigames/backgrounds/shelf.png"

    imagebutton:
        idle "images/minigames/boxing/boxing_gloves.png"
        pos (300, 100)
        action Function(choose_glove, "normal")

    imagebutton:
        idle "images/minigames/boxing/boxing_gloves_with_horseshoe.png"
        pos (900, 100)
        action Function(choose_glove, "horseshoe")
