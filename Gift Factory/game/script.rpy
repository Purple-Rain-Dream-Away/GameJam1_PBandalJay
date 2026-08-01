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

    jump chapter2

label chapter2:
    "As the wheel turns and the days go on, a multitude of people pass into the store."

    "Some... weirder than others"

    jump .noir_customer

    label .noir_customer:
        scene bg club  # The bg suddenly shifts to black and white to reflect the shift to noir

        "A cool crispy breeze rolls in through the window. Good timing, damned fan stopped working."

        "A rugged figure bursts through the door, panting and eyes drooping and...."

        "Perhaps still unbathed."

        "He brandishes a gun with his right hand, and extends his left towards you."

        c2 "Boss wants sumfin nice for his 78th birthday. Something real sparkly... or dangerous. Make it quick."

        menu:
            "Mafia bosses. Buncha gunk-drinkin slime-spittin fat lowlife thugs. They got a penchant for gold"

            "Real fond o' lead too. And all the ways you can pump people full of it."

            "Slide some 24-carat magic rings his way":
                jump .doll_customer

            "Clench your fist. Tell him you have a real nice gift for him in your hand. Then, make a rude gesture":
                jump dead

    label .doll_customer:
        

label dead:
    "Real clever, sticking it to him like that. Real cheap way to find yourself 6 feet under."




    return
