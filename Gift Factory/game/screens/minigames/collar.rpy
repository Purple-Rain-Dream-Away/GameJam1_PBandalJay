default chosen_for_dog = None

init python:
    def choose_collar(collar):
        store.chosen_for_dog = collar
        return collar

screen shelf_collar:
    add "images/minigames/backgrounds/basic_background.png"
    add "images/minigames/backgrounds/shelf.png"

    imagebutton:
        idle "images/minigames/collar/collar.png"
        pos (300, 100)
        action Function(choose_collar, "good_collar")

    imagebutton:
        idle "images/minigames/cow/wheat.png"
        pos (900, 100)
        action Function(choose_collar, "shit")

    imagebutton:
        idle "images/minigames/food making/egg.png"
        pos (300, 500)
        action Function(choose_collar, "shit")

    imagebutton:
        idle "images/minigames/boxing/boxing_gloves_with_horseshoe.png"
        pos (900, 500)
        action Function(choose_collar, "decent_collar")
