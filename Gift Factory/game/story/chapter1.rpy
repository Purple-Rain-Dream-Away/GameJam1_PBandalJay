image cake good = "images/minigames/food making/cake_good.png"
image cake okay = "images/minigames/food making/cake_okay.png"
image cake bad = "images/minigames/food making/cake_bad.png"
image cake = "images/minigames/food making/cake_base.png"

label chapter1:
    "In the world of placeholder, the fancies of the mind find purchase in reality."

    "Children take flying rollercoasters to school, haunted houses are staffed by literal ghouls and ghosts"

    "And every marketing campaign is headed by a cabal of blood-sucking vampires"

    "Yet none of these match up to the Generous, Gorgeous, Gleaming, Glamorous Gift Factory."

    jump .first_customer

    label .first_customer:
        scene store
        with fade

        show desk

        "Today is your first day working in the Gift Factory."

        "Your workplace has only one motto: the customer is always right"

        "When a customer asks for something, you give it to them!"

        "The dusty stacks and shelves of the Gift Factory are sure to contain exactly what they need."

        show clara_customer

        hide desk

        show desk

        c1 "Good morning! I'm looking for a toy for my little sister."

        c1 "She's a real fan of boxers: Mika Twoson, Emma Paksiw, Sugar Ria Lena. The greats."

        # This line makes use of double quotes and italics. Note to self to check if it works
        c1 "I mean really she never shuts up about them, and I thought to myself, \"Wouldn't it be great if she put all that energy into learning how to {i}actually{/i} punch people, instead of just watching other people do it?\""

        c1 "So what I mean is, it'd be nice if I could give her something like a pair of boxing gloves."

        "Boxing Gloves! What store doesn't have those."

        "Looking through the catalogue, you decide to give her:"
        
        call screen shelf_boxing

        if gloves_chosen == "normal":
            "place"
        elif gloves_chosen == "horseshoe":
            "holder"

        jump .bouquet_customer



    label .bouquet_customer:
        scene store
        with fade

        show desk

        "The Gift Factory is a miracle on Earth... A place where every dream is fulfilled and every wish granted."

        "All sorts of people desperately seek refuge and healing through this fine establishment's wares."

        "Just look at this fine young lady here: the tapping of her feet and the twinkling of her eyes betray her turbulent feelings."

        show delinquent_customer
        
        hide desk

        show desk

        mic "Hi! yes uhm, I was wondering if you had anything, uh, well anything {i}sophisticated{/i} and {i}lovely{/i} and {i}fragrant{/i} and..."

        "Looks like {i}someone's{/i} in loveeeee."

        mic "romantic?? Like, {size=-8}say{/size}, {size=-14}for instance{/size}, {size=-19}a bouquet...?{/size}"

        "For Eons, young hopeful lovers have turned to the Gift Factory for the perfect present with which to woo the apple of their eyes."

        menu:
            "Today, it seems, is no different."

            "Make her a bouquet for her dearly beloved":
                call screen bouquet_minigame

                # tweak this i suppose? unsure what to do depending on the bouquet given + placeholder dialogue
                if flower_count == 0:
                    mic "what the fuck is this"
                    $ good_level -= 1
                elif flower_count == 6:
                    mic "thank you you are an angel sent from heaven"
                    $ good_level += 2
                else:
                    mic "ok then"

                jump .tinapay_customer

    label .tinapay_customer:
        scene store
        with fade

        show desk

        "The sun sets as the end of the day draws closer."

        if good_level > 0:
            "You begin to grow attached to this job. Seeing the smiles on the customer's face, excited to bring joy to someone they hold dear."

        show construction_customer
        
        hide desk

        show desk

        "A middle-aged man walks in. He looks exhausted, presumably from a hard day's work."

        m "What can I get you, good sir?"

        mm "I'd like a cake, please. Thought I'd bring home a little surprise for my children back at home."

        "How sweet. Pun intended."

        m "Alright, what kind of cake do you want?"

        mm "Red Velvet. Not really a fan of it myself, but the kids seem to love that stuff."

        m "One Red Velvet cake, coming right up!"

        "By some miracle, you have everything you need to make such a cake."

        "You quickly get to work."

        hide construction_customer

        call screen cake_pt1
       
        if bowl_score == 0:
            show cake bad at truecenter
        elif bowl_score == 1:
            show cake okay at truecenter
        else:
            show cake good at truecenter
        
        "Voila!"

        hide cake

        # cut content, might bring back
        # mm "Must be boring sitting around all day in here, huh?"

        # m "It's not that bad, customers come by pretty often and their requests can sometimes be entertaining."

        # m "What do you do for work, by the way?"

        # mm "I'm a construction worker. Working on the building just a few blocks over."

        # mm "It's hard, and I always come home exhausted, but I'd do anything for my family."

        #cake minigame pt3

        menu:   
            "Give him the cake":
                m "Here you go!"


        if bowl_score <= 0:
            mm "This is... not really what I had in mind..."

            menu:
                "Make him a new cake.":
                    #m "Oh, sorry! My mistake, I was just so engrossed in our conversation."
        
                    m "I'll make you a new one as a replacement, how about that?"
                    
                    call screen cake_pt1
                
                    if bowl_score == 0:
                        show cake bad at truecenter
                    elif bowl_score == 1:
                        show cake okay at truecenter
                    else:
                        show cake good at truecenter
                    
                    "Voila!"

                    hide cake

                "Give him this cake.":
                    "The man leaves dissapointed."
                    $ good_level -= 1
                    jump chapter2
            
    
        if bowl_score <= 0:
            mm "You know what, I'll just take it. I'm sure my kids will be happy with it anyway."
            $ good_level -= 2
            
            jump chapter2


        # edit cake quality boundaries
        elif 0 < bowl_score <= 3:
            mm "This looks great, thank you! I'm sure my kids will love it."
            
            $ good_level += 1

            jump chapter2

        else:
            mm "This is perfect! Thank you so much, I didn't expect to get such an amazing cake!"

            mm "My kids will be so happy when they see it, I'm sure of it!"

            $ good_level += 2
            
            jump chapter2