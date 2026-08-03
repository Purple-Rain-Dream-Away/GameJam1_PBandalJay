init python:
    def feed_cow(drags, drop):
        return -1

screen feed_cow:
    add "images/minigames/backgrounds/garden.jpg"

    draggroup:
        drag:
            drag_name "cow"
            align (0.5, 0.5)
            draggable False

            add "images/minigames/cow/cow.png"

        drag:
            drag_name "wheat"
            pos (100, 500)
            droppable False
            dragged feed_cow

            add "images/minigames/cow/wheat.png"

screen take_shit:
    add "images/minigames/backgrounds/garden.jpg"

    imagebutton:
        idle "images/minigames/cow/SHIT.png"
        pos (1300, 500)
        action Return(-1)

    add "images/minigames/cow/cow.png" align (0.5, 0.5)

screen get_cow:
    add "images/minigames/backgrounds/garden.jpg"

    imagebutton:
        idle "images/minigames/cow/cow.png"
        align (0.5, 0.5)
        action Return(-1)