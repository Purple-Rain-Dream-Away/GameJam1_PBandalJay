default chosen_for_dog = None
default look_behind = False
default your_health = 10
default enemy_health = 10
default enemy_action = 0
default your_damage = 0

label chapter2:
    "As the wheel turns and the days go on, a multitude of people pass into the store."

    "Some... weirder than others"

    label .dog_customer:
        scene bg uni
        with fade

        "A girl nervously walks into the store."
        
        kg "H-hello! I'd like to b-buy a collar."

        kg "For my d-dog."

        m "Alright, just give me a minute."

        "Why is she so nervous?"

        "Doesn't matter, let's go find what she needs."

        # PAN TO SHELF

        m "What kind of collar are you looking for?"

        kg "S-something simple, my \"dog\" isn't t-too picky."

        m "I'll see what we have in stock."

        # SHELF MINIGAME
        m "This one should do."

        # SWITCH TO COUNTER

        if chosen_for_dog == "good_collar":
            $ good_level += 1

            kg "Thank y-you. I'm sure my \"\"dog\"\" will love this a lot."

            m "You're welcome. If I may ask, could I see a picture of your dog?"

            kg "Y-you want to see a picture of my \"\"\"dog\"\"\"?"

            m "Yeah, I love dogs! I'd love to see the pupper this collar is going to."

            kg "S-sorry, I d-don't think he'd like it if I showed a s-stranger a p-picture of him."

            kg "M-my \"\"\"\"dog\"\"\"\", I m-mean."

            m "No worries, have a good day!"

            "Weird."

        elif chosen_for_dog == "decent_collar":
            kg "N-not exactly what he h-had in mind but it'll do."

            kg "My \"\"dog\"\", I mean."

            m "Sorry, it's all we had."

            kg "It's f-fine, I'm sure he'll still b-be happy with it. My \"\"\"dog\"\"\"."
        
            "Weird."

        else:
            $ good_level -= 1
            kg "W-what is this? I asked for a c-collar."

            kg "For m-my \"\"dog\"\"."

            kg "I don't t-think he's going to be too happy with this."

            kg "My \"\"\"dog\"\"\", I mean."

            "She takes the item and leaves, clearly upset"

            "What's up with her and her dog?"

        jump .noir_customer


    #jump .noir_customer

    label .noir_customer:
        # Also this is still a placeholder
        scene grey_store  # The bg suddenly shifts to black and white to reflect the shift to noir
        with fade

        show grey_desk

        "A cool crispy breeze rolls in through the window. Good timing, damned fan stopped working."

        show mafia_customer

        "A rugged figure bursts through the door, panting and eyes drooping and...."

        "Perhaps still unbathed."

        "He brandishes a gun with his right hand, and extends his left towards you."

        b "Boss wants sumfin nice for his 78th birthday. Something real sparkly. Make it quick."

        menu:
            "Mafia bosses. Buncha gunk-drinkin slime-spittin fat lowlife thugs. They got a penchant for gold"

            "Real fond o' lead too. And all the ways you can pump people full of it."

            "Slide some 24-carat magic rings his way":  # Consider making a minigame for this
                # BG CHANGE

                # EXPOSITORY DIALOGUE
                "As you reach for the model hand that holds the rings, a vicious sneer erupts from the palm."

                "It's alive."

                h "Hands off the bling bub else I'll knock ya flat."

                h "Ya know how I got all this drip? I strangled a fella for it. Bastard thought he could mug me."

                h "Least that one had some steel in his spine. Yer just a lowlife giftwrapping minimum wage worker fresh from college."

                h "I'll show you what happens when you mess with HANDY HOGAN"
                while your_health > 0 and enemy_health > 0:
                    if enemy_health > 0:
                        $ enemy_action = renpy.random.randint(0,1)
                    if enemy_action == 0:
                        "Looks like he's going for an attack."
                    else:
                        "He awaits your next move."
                    menu:
                        "Attack":
                            $ your_damage = renpy.random.randint(0, 4)
                            if your_damage == 0:
                                "He blocked it!"
                            else:
                                $ enemy_health -= your_damage
                                "You did some damage!"
                            if enemy_action == 0:
                                $ your_health -= renpy.random.randint(1,3)
                                "You were hit."
                                if your_health <= 0:
                                    "You black out."
                                    jump .murim_customer
                        "Defend":
                            if enemy_action == 0:
                                "You blocked his attack!"
                            else:
                                "That was pointless." 
                # BACK TO COUNTER
                $ good_level += 1
                # DIALOGUE HAND HIM THE RING
                jump .murim_customer

            "Clench your fist. Tell him you have a real nice gift for him in your hand. Then, make a rude gesture":
                jump mafia_death
    
    label .murim_customer:

        show murim_customer

        "It's been 500 years since the defeat of the Demonic Cult."

        "An era of peace for the Murim that proved to be quite prosperous."

        "The Gift Factory has been passed down for generations, known across the lands for offering wares for any occasion."
        
        "And as the day goes by, another customer has come looking for this humble merchant."

        show murim_customer

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
        scene bg uni
        with fade

        "Suddenly, the breeze turns downright frigid. A chill runs through your spine and plucks your every nerve."

        show doll_customer

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
                jump .ashes_customer

            "Dispose of it. Right now. That {i}thing{/i} isn't even a part of this shop. No one should ever handle this.":
                jump doll_death
  
    label .ashes_customer:
        "Satisfied, she tightly grips the doll, and starts running out as fast as her legs can carry her."

        "Shouting and screaming in delight the entire time."

        "As you ponder the, frankly, horrifying customers that have thus far been ruining your day, you decide to close up shop for now."
        
        "However, right as you reach for the keys to the Gift Factory, one last interloper swings the door open."

        show ashes_customer

        "He lazily strides in, carrying a small, dusty box with him. He sees you and smiles."

        a "I know the shop's about to close, but do you have the time for just one simple request?"

        a "I have th-this very special someone. I adore him really. I was wondering if you could bake a cake for him?"

        "Oh fine, I'll do this ONE thing, and I'll immediately run home."

        m "Got it. Cake. That should be easy. What flavor?"

        a "Something simple, like cheesecake or carrot cake. The flavor doesn't really matter."

        a "I just need you to place a {i}special{/i} ingredient while you're making it."

        "He holds out the box to you."

        m "And, uh, I hope it wouldn't be unreasonable to ask just {i}what{/i} that is exactly?"

        a "Oh nothing, it's just a bit of powder really. My friend, he loves the stuff. I'm sure he'll eat it right up."

        m "..."

        m "Alright then."

        menu:
            # insert minigame
            "Bake the cake using the ashes":
                ...

            "Bake the cake without using the ashes":
                ...




label fight_death:
    "DIE"

    return

label mafia_death:
    "Real clever, sticking it to him like that. Real cheap way to find yourself 6 feet under."

    return

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
