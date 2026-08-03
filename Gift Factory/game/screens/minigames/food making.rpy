default in_bowl = []
default bowl_score = 0

init python:
    def ingredient_dragged_to_bowl(drags, drop):
        if not drop:
            if drags[0] in store.in_bowl:
                store.in_bowl.remove(drags[0])

        else:
            if drags[0] not in store.in_bowl:
                store.in_bowl.append(drags[0])

    def finish_bowling():
        len_bowl = len(store.in_bowl)
        store.in_bowl = []
        if len_bowl == 4:
            store.bowl_score = 2
            return 2
        elif len_bowl <= 1:
            store.bowl_score = 0
            return 0
        else:
            store.bowl_score = 1
            return 1


screen cake_pt1:
    add "images/minigames/backgrounds/basic_background.png"
    
    add "images/minigames/backgrounds/table.png"

    draggroup:
        drag:
            drag_name "bowl"
            draggable False
            xpos 500 ypos 500

            add "images/minigames/food making/bowl.png"

        drag:
            drag_name "egg"
            droppable False
            xpos 250 ypos 500
            dragged ingredient_dragged_to_bowl

            add "images/minigames/food making/egg.png"
        
        drag:
            drag_name "flour"
            droppable False
            xpos 250 ypos 250
            dragged ingredient_dragged_to_bowl

            add "images/minigames/food making/flour.png"

        drag:
            drag_name "milk"
            droppable False
            xpos 750 ypos 500
            dragged ingredient_dragged_to_bowl

            add "images/minigames/food making/milk.png"

        drag:
            drag_name "sugar white stuff"
            droppable False
            xpos 750 ypos 250
            dragged ingredient_dragged_to_bowl

            add "images/minigames/food making/sugar white stuff.png"

    vbox:
        textbutton "finish step":
            action finish_bowling
