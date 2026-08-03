label chapter3:
    scene black with fade
    "Day 3"

    scene store with fade
    
    show desk

    "Historically, the number 3 holds a great deal of significance."

    "3 primary colors, 3 states of matter, 3 musketeers."

    "And of course, as they say, third time's the charm."

    "Today is your third day working at the Gift Factory."

    "According to previous workers, the third day is inexplicably always the hardest."

    "They say you're bound to meet the most mind-boggling customers of your life."

    label .elf_customer:
        scene store with fade
        
        show elf_customer
        
        show desk

        "A 7-foot tall, elegant figure strides through the doorway and into your shop"

        "It almost hovers as it comes to a stop, and you notice its sharp ears and frail form."

        "Is that.... an elf???"

        e "Greetings short one."

        e "My people require your aid..."

        e "Recently, our dearest World Tree has begun to wither."

        e "Its roots desperately reach out for sustenance to no avail..."

        e "Root absorption across millions of years has rendered the soil depleted and infirm."

        e "Our barksages and seers have determine the one course of action that shall save us.."

        e "We must procure a mythical fertilizer, solid in form and foul of smell."

        e "We have heard that it is produced only by a legendary creature, of which none of my kind have ever observed."

        e "A large, grazing beast, patterned black and white... I believe it is known as"

        e "The Cow."

        cow "Moo."

        "Was that a cow?"

        "In the store?"

        "What the fu-"

        e "I believe you have such a creature at your disposal, short one."

        "Shit. Literally."

        "I need to feed the cow for it to make his fertilizer."

        call screen feed_cow

        m "I just fed the cow, it'll take a while until it makes your request."

        "4 hours later."

        call screen take_shit

        m "Here you go..."

        e "My sincerest gratitude, short one, may you be blessed by the World Tree."

        jump .alien_customer
    
    label .alien_customer:
        show alien_customer

        "Here comes one right now."

        "A naked, green man stumbles through the door and stares at you with its space-black, beady eyes."

        "It awkwardly raises its hands in a sign of peace; then hesitantly lowers them."

        ad "Oxygen and Heat upon you, Earthling!"

        ad "My people, the Qudxy, require an {i}exotic animal{/i} for our arkship sanctuaries."

        ad "In time we hope to construct a zoo-arcology of such immense proportions as to be able to populate an entire world."

        ad "We've heard that this planet hosts a unique creature currently unknown to the cosmos at large."

        ad "A stout, gaseous and supposedly delicious herbivore known as: The Cow."

        ad "It'll be perfect for our kitch- sanctuaries! I meant sanctuaries!"

        "Guess I know what to do with the cow now."

        call screen get_cow



        jump .skeleton_customer

    label .skeleton_customer:

        show skeleton_customer
        "As the alien flies away on his UFO, a new customer steps into the shop..."

        "First come the legs, completely devoid of skin, hopping in like it's just another tuesday."

        "Then come the ribs, spine and skull, tossed in by an unseen individual."

        "Finally, the arms crawl in with a teeth-chattering rattle behind every stretch and grab."

        "The pieces all flail around and conjoin until reaching the correct arrangement: that of a humanoid skeleton."

        s "HAW HAW HAW! bet that scared you didn't it?"

        s "Not to worry fleshboy! I'm not here to hurt you"

        s "I'm here for your assistance! My dear husband, you see, we've been together for 7 years."

        s "He's always had the most {i}gorgeous{/i} bones. He plates them with gold, you see."

        s "Unfortunately, his ribs recently broke due to a skydiving incident. We were flying above the Bermuda Triangle you see."

        s "And so that brings us here. I require the most fabulous, ostentatious and audacious ribs you have in store!"


    label .final_customer:
        "As the day draws closer to its end, you feel an exceptional pressure from just beyond the Gift Factory's walls."

        "A weeping man stands at the doorway, brandishing a gun and aiming straight for your head."

        u "WHERE IS IT"

        u "TELL ME WHERE IT IS"

        u "WHERE DID YOU HIDE THE ASHES OF MY BROTHER"

        m "Woah woah calm dow-"

        u "DONT YOU TELL ME TO CALM DOWN"

        u "THAT MANIAC THAT CAME INTO YOUR STORE KILLED MY BROTHER"

        "He cocks his gun and takes a deep breath"

        u "He sent me that cake of yours. Said you used my brother's ashes to bake it."

        u "He's dead now. That animal got what he deserved."

        u "But there's still one lose end left."

        u "YOU"

        if not used_ashes:
            m "Wait! your brother's ashes are right here."

            m "I knew something was wrong with that man. He told me it was just powder."

            m "But when I looked into the box and saw... that, I knew something was up."

            m "Here. It's yours now."

            "He tenderly reaches for the box of ashes."

            u "..."

            u "Thank you."

            u "Thank you so much."

            jump good_ending
        else:
            m "Wait! I didn't mean to use your brother's ashes."

            m "When that man told me to use it, he said it was just powder!"

            m "I swear! I didn't know any better."

            "He sneers at you, and pulls the trigger."

            u "Go to hell."

            jump bad_ending

label good_ending:
    return

label bad_ending:
    return
    
    return