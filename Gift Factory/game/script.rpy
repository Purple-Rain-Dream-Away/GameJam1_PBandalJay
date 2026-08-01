# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 = Character("Customer_1")
define c2 = Character("Customer_2")
define m = Character("Me")


# The game starts here.


# Standard gift giving
label start:
    "In the world of placeholder, the fancies of the mind find purchase in reality."

    "Children take flying rollercoasters to school, haunted houses are staffed by literal ghouls and ghosts"

    "And every marketing campaign is headed by a cabal of blood-sucking vampires"

    "Yet none of these match up to the Generous, Gorgeous, Gleaming, Glamorous Gift Factory."

    scene bg lecturehall  # This is just a placeholder
    with fade

    "Today is your first day working in the Gift Factory."

    "Your workplace has only one motto: the customer is always right"

    "When a customer asks for something, you give it to them!"

    "The dusty stacks and shelves of the Gift Factory are sure to contain exactly what they need."

    show sylvie blue normal  # Again, this is also a placeholder

    c1 "Good morning! I'm looking for a toy for my little sister."

    c1 "She's a real fan of boxers: Mika Twoson, Emma Paksiw, Sugar Ria Lena. The greats."

    # This line makes use of double quotes and italics. Note to self to check if it works
    c1 "I mean really she never shuts up about them, and I thought to myself, \"Wouldn't it be great if she put all that energy into learning how to {i}actually{/i} punch people, instead of just watching other people do it?\""

    c1 "So what I mean is, it'd be nice if I could give her something like a pair of boxing gloves."

    menu:
        "Boxing Gloves! What store doesn't have those."

        "Looking through the catalogue, you decide to: "

        "Give her a pair of small, red boxing gloves. A classic!":
            ...

        "Give her a pair of small, red boxing gloves with horseshoes inside it":  # This would be rly funny
            ...

        "Probably some other option":
            ...

    jump customer2

# Genre shift to noir??
label customer2:
    "As the wheel turns and the days go on, a multitude of people pass into the store."

    "Some... weirder than others"

    scene bg club  # The bg suddenly shifts to black and white to reflect the shift to noir 
    # Literally exact same background, but black and white
    # Maybe make some small changes





    return
