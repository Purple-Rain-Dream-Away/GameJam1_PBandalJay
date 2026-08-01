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
                jump .murim_customer

            "Clench your fist. Tell him you have a real nice gift for him in your hand. Then, make a rude gesture":
                jump mafia_death
    
    label .murim_customer:
        scene bg uni  # Just a placeholder
        with fade

        "It's been 500 years since the defeat of the Demonic Cult."

        "An era of peace for the Murim that proved to be quite prosperous."

        "The Gift Factory has been passed down for generations, known across the lands for offering wares for any occasion."
        
        "And as the day goes by, another customer has come looking for this humble merchant."

        mg "Greetings, dear merchant. Alas, after a long journey to the west, I've finally arrived at the renowned Gift Factory!"

        "The Blessed Dragon of Mount Hua!? One of the most powerful martial artists across the Murim, known for his unrivaled sword technique that resembles plum blossom petals flowing through a summer breeze, seeking out this humble establishment?"

        mg "I've heard of plenty of tales that tell of the expertise of this workshop. I'd like to see for myself just how capable you are."

        "What could he possibly be looking for?"

        mg "I would like nothing more than the strongest elixir you offer."

        m "An elixir? What use is an elixir for someone already as strong as you?"

        mg "Ah, do not be mistaken, my friend. The elixir is not for me to use. One of my disciples has been having problems with their lower dantian, and the Divine Physician told me to seek out an elixir from you."

        #BG CHANGE
        "I swiftly searched for such an elixir, doubtful if such a thing existed within these walls."

        # PAUSE 
        "After a few minutes of scouring the place, I felt it."

        "A deeply unsettling aura emanating from a box in the corner."

        # SHOW THE BOX
        m "This must be it."

        # SCREEN WITH THE BOX, CLICK IT TO OPEN
        "As I opened it, I could feel the Qi emanating from this bottle no larger than my thumb."

        m "Why do we have this?"

        "I quickly went back to the prestiged customer with the elixir in hand."

        #BG CHANGE
        mg "Judging by that thing in your hand, I take you've found the elixir?"

        "A thought passes my mind. Do I really have to give this to him?"

        "If this truly is an elixir recommended by the Divine Physician and sought out by one of the strongest in the Murim, surely it must be able to make a nobody like me powerful enough to rival some of the strongest in the Murim, right?"
        
        menu:
            "Give him the elixir":
                # tweak this i suppose? unsure what to do depending on here
                $ good_level += 1
                mg "My deepest gratitude towards you, dear Gift Maker. The heavens shall repay your kindness in due time."

                mg "Now, I must be off at once. My disciple shall get their treatment as soon as possible!"
                jump .doll_customer

            "Take it for yourself":
                m "I couldn't find it. I don't think our store has such a thing."

                mg "And, pray tell, why would you lie, dear Gift Maker? I can sense the Qi coming off of that thing in your hand there."

                mg "To try to deceive me, when I've come to you with most honest intentions of saving my disciple. What mockery is this?"

                "He puts his hand on his blade. You can feel the atmosphere around you changing. The air around you feels colder, as he awaits for an answer."

                "I drink the elixir right in front of him."

                mg "The audacity!"

                "I could feel the Qi surging through me. I was growing stronger. Far stronger."

                mg "You will come to regret that."

                "Even stronger. You feel your power continue to rise."

                "It doesn't stop. Waves of Qi continue to rush within you."

                "You begin coughing up blood."

                m "What's happening to me!?"

                mg "Qi Reflux, my friend. It seems you were incapable of taking in that much energy."

                "You realize you never even learned how to circulate your Qi."

                "Your vision grows darker, as both pain and power course within you."

                "Your heart stops."

                return

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
