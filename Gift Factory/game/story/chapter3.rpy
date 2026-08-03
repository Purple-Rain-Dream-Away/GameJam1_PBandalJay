label chapter3:
    "Historically, the number 3 holds a great deal of significance."

    "3 primary colors, 3 states of matter, 3 musketeers."

    "And of course, as they say, third time's the charm."

    "Today is your third day working at the Gift Factory."

    "According to previous workers, the third day is inexplicably always the hardest."

    "They say you're bound to meet the most mind-boggling customers of your life."

    label .alien_customer:
        show alien_customer

        "Here comes one right now."

        "A naked, green man stumbles through the door and stares at you with its space-black, beady eyes."

        "It awkwardly raises its hands in a sign of peace; then hesitantly lowers them."

        a "Oxygen and Heat upon you, Earthling!"

        a "My people, the Qudxy, require an {i}exotic animal{/i} for our arkship sanctuaries."

        a "In time we hope to construct a zoo-arcology of such immense proportions as to be able to populate an entire world."

        a "We've heard that this planet hosts a unique creature currently unknown to the cosmos at large."

        a "A stout, gaseous and supposedly delicious herbivore known as: The Cow."

        a "It'll be perfect for our kitch- sanctuaries! I meant sanctuaries!"

        "It just so happens that the Gift Factory ALWAYS keeps a singular (1) cow on the premises for just this occassion."

        menu:
            "Let them take our company-mandated Big Bertha, never to be seen again.":
                ""  # Minigame maybe??

            "Inform them that Big Bertha is a beloved member of the family, and she has been for 50 long years! Nobody can take her away from us!":
                ""  # idk refusal tracker??

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

    label .elf_customer:
        show elf_customer
        
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

        #menu:
        #    "Unfortunately, for all of the Gift Factory's wonders, there has only ever been one cow in stock for the last 50 years."

        #    "And you just gave it to that lovely alien fellow a bit earlier."

            # Trying to use double quotation marks here
        #    "However! it is undoubtable that Big Bertha must have left some \"gifts\" of her own."

            # Insert cow poop minigame. js drag and drop cow poop??? maybe??

        jump .final_customer


    label .final_customer:
        "placeholder"
    
    return