# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 = Character("Clara")  # First customer
define mic = Character("Michelle")  # Bouquet customer
define b = Character("Big Billy")  # Noir customer
define t = Character("Tall Lady")
define m = Character("Me")


# The game starts here.


# Standard gift giving
label start:
    "In the world of placeholder, the fancies of the mind find purchase in reality."

    "Children take flying rollercoasters to school, haunted houses are staffed by literal ghouls and ghosts"

    "And every marketing campaign is headed by a cabal of blood-sucking vampires"

    "Yet none of these match up to the Generous, Gorgeous, Gleaming, Glamorous Gift Factory."

    jump .first_customer

    label .first_customer:
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
                jump .bouquet_customer

            "Give her a pair of small, red boxing gloves with horseshoes inside it":  # This would be rly funny
                jump .bouquet_customer  # Make special reaction to this? idk

            "Probably some other option":
                ...

    label .bouquet_customer:
        scene bg meadow  # Just a placeholder
        with fade

        "The Gift Factory is a miracle on Earth... A place where every dream is fulfilled and every wish granted."

        "All sorts of people desperately seek refuge and healing through this fine establishment's wares."

        "Just look at this fine young lady here: the tapping of her feet and the twinkling of her eyes betray her turbulent feelings."

        mic "Hi! yes uhm, I was wondering if you had anything, uh, well anything {i}sophisticated{/i} and {i}lovely{/i} and {i}fragrant{/i} and..."

        "Looks like {i}someone's{/i} in loveeeee."

        mic "romantic?? Like, {size=-8}say{/size}, {size=-14}for instance{/size}, {size=-19}a bouquet...?{/size}"

        "For Eons, young hopeful lovers have turned to the Gift Factory for the perfect present with which to woo the apple of their eyes."

        menu:
            "Today, it seems, is no different."

            "Insert Minigame":
                ...
                jump chapter2



label chapter2:
    "As the wheel turns and the days go on, a multitude of people pass into the store."

    "Some... weirder than others"

    jump .noir_customer

    label .noir_customer:
        # Also this is still a placeholder
        scene bg club  # The bg suddenly shifts to black and white to reflect the shift to noir
        with fade

        "A cool crispy breeze rolls in through the window. Good timing, damned fan stopped working."

        "A rugged figure bursts through the door, panting and eyes drooping and...."

        "Perhaps still unbathed."

        "He brandishes a gun with his right hand, and extends his left towards you."

        b "Boss wants sumfin nice for his 78th birthday. Something real sparkly... or dangerous. Make it quick."

        menu:
            "Mafia bosses. Buncha gunk-drinkin slime-spittin fat lowlife thugs. They got a penchant for gold"

            "Real fond o' lead too. And all the ways you can pump people full of it."

            "Slide some 24-carat magic rings his way":  # Consider making a minigame for this
                jump .doll_customer

            "Clench your fist. Tell him you have a real nice gift for him in your hand. Then, make a rude gesture":
                jump mafia_death

    label .doll_customer:
        default look_behind = False
        scene bg uni
        with fade

        "Suddenly, the breeze turns downright frigid. A chill runs through your spine and plucks your every nerve."

        "A tall, grinning woman stoops through the door and pads towards you. It takes her only 3 steps to reach the counter."

        "She stays there, staring, smiling for a good few seconds. Finally, she speaks."

        t "Give me... a doll. Something preeeettyyy..."

        t "Something any child will love..."

        "She points behind you."

        t "Like that one, right there"

        "As per Company Regulation #355.1: all Gift Factory products are to be stored within the shelves and nooks of the establishment."

        "There are no such shelves or nooks behind you. Only a blank, peeling wall and.... a window"

        while not look_behind:
            menu:
                "Look behind you":
                    $ look_behind = True

                "Keep looking forward":
                    "You have no choice. "

        "Sitting innocently on the ledge right behind the window is a rancid, partly broken doll."

        "In the places where it cracks, you see sickly green flesh. It makes this awful strained sound, like a laughing, dying goose."

        "It has a voicebox, right on its chest. It looks broken."

        t "As I said dear. I'll be taking that one."

        menu:
            "Give it to her. Whatever it is, you don't need it haunting you.":
                jump chapter3

            "Dispose of it. Right now. That {i}thing{/i} isn't even a part of this shop. No one should ever handle this.":
                jump doll_death

label mafia_death:
    "Real clever, sticking it to him like that. Real cheap way to find yourself 6 feet under."

label doll_death:
    "The drive home is a blur. Nothing but chrome-colored unfinished buildings line the way home anyway."

    "You pull up into the driveway and fiddle with the singular key on your keychain."

    "It slips. You bend down to retrieve it but it slips once more, into the bushes beside the stairway."

    "You reach into the brush to grab it, only to be met with gashes running down your hand when you pull it back."

    "You fling the door open and, once inside, slam it closed. You turn every light on, close every curtain, and flee for your bedroom."

    "Just like you always did when you were a child. When you thought the monster would get you if you didn't run fast enough."

    "But the soft, warm bed and the sturdy door always kept you safe. It always kept you safe."

    "You slip under your blanket and you pray and your pray and your pray."

    "Your mind drifts to someplace far away, where a closet begins to creak open."

    "Somewhere, halfway across the world you like to think, a shadow peers from the closet door."

    "Somewhere, so very far away from you, a rotten smell creeps closer and closer to your flimsy blanket fortress."

    "This is the only way it could have ended."
    return
