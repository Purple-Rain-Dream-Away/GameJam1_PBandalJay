default flower_count = 0
default flowers_in_bouquet = []

init python:

    def flower_dragged(drags, drop):
        if not drop:
            if drags[0] in flowers_in_bouquet:
                store.flowers_in_bouquet.remove(drags[0])
                store.flower_count -= 1

        else:
            drop.top()
            if drags[0] not in flowers_in_bouquet:
                store.flower_count += 1
                store.flowers_in_bouquet.append(drags[0])

    def finish_bouquet():
        return flower_count

screen bouquet_minigame:

    add "images/minigames/bouquet/bouquet bg.jpg"

    draggroup:

        drag:
            drag_name "Red"
            droppable False
            dragged flower_dragged
            xpos 100 ypos 100

            add "images/minigames/bouquet/red bouquet flower.png"
        
        drag:
            drag_name "Orange"
            droppable False
            dragged flower_dragged
            xpos 300 ypos 300

            add "images/minigames/bouquet/orange bouquet flower.png"

        drag:
            drag_name "Yellow"
            droppable False
            dragged flower_dragged
            xpos 100 ypos 500

            add "images/minigames/bouquet/yellow bouquet flower.png"

        drag:
            drag_name "Green"
            droppable False
            dragged flower_dragged
            xpos 1600 ypos 100

            add "images/minigames/bouquet/green bouquet flower.png"

        drag:
            drag_name "Blue"
            droppable False
            dragged flower_dragged
            xpos 1400 ypos 300

            add "images/minigames/bouquet/blue bouquet flower.png"
        
        drag:
            drag_name "Purple"
            droppable False
            dragged flower_dragged
            xpos 1600 ypos 500

            add "images/minigames/bouquet/purple bouquet flower.png"
        
        drag:
            drag_name "Bouquet"
            draggable False
            xpos 670 ypos 500
            add "images/minigames/bouquet/bouquet bouquet real.png"
    
    vbox:
        textbutton "finish bouquet":
            action finish_bouquet