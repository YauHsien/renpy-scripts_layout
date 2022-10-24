


label talk_others(char1, location1):
    show screen main_game(location1)

    if char1.get_action_allowed("talk_others") == False:
        $ l_text = char1.get_action_not_allowed_text("talk_others")
        char1.talk "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_15
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("talk_others", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    $ option0 = True
    $ option1 = True
    $ option2 = True
    $ option3 = True
    $ option4 = True
    $ option5 = True
    $ option6 = True
    $ option7 = True
    $ option8 = True
    $ option9 = True
    $ option10 = True
    $ option11 = True
    $ option12 = True
    if menu_active == False:
        $ l_menu_active_old = False
        $ menu_active = True
    elif True:
        $ l_menu_active_old = True

    label talk_others_menu:
    menu:
        "Ask her to call you [player.fname]" if player.fname <> char1.playername and option0:
            $ option0 = False
            pl "Hey [char1.fname], why don't you call me [player.fname]?"
            if char1.check_affection(1) == True:
                $ char1.playername = player.fname
                char1.talk "Sure [char1.playername], I am happy to do that. *smiles*"
            elif True:
                char1.talk "I don't think that would reflect our relationship [char1.playername]."
            jump talk_others_menu

        "Ask her about her bra size" if char1.bra_size_known == False and option1:
            $ option1 = False
            pl "[char1.fname] you have incredible breasts. I was wondering what your bra size might be."
            if char1.check_tease_sexual(2) == True:
                if char1.id == amy.id:
                    char1.talk "Nice try [char1.playername]! *grins*"
                    char1.talk "No way I'm just telling you my bra size... *smirks*"
                    pl "Ummm... Okay."
                elif True:
                    $ char1.bra_size_known = True
                    char1.talk "I am wearing a [char1.bra_size] bra."
                    "Wow what a girl. I wonder how she looks topless."
                    pl "No way! [char1.fname] that's incredible."
                    char1.talk "*smiles* I knew you would like to know that. But still it is a bit rude to ask."
                    $ player.change_lust(char1.sexiness + 2)
                    $ char1.change_affection(-20)
                    $ char1.change_lust(10)
            elif True:
                char1.talk "I don't think it is appropriate to ask a lady something like that."
            jump talk_others_menu

        "Ask her about her waist size" if char1.waist_size_known == False and option2:
            $ option2 = False
            pl "[char1.fname] I adore your figure. Would you tell me your waist size?"
            if char1.check_tease_sexual(1) == True:
                if char1.id == amy.id:
                    char1.talk "*smiles*"
                    char1.talk "Although you're really cute [char1.playername], I won't make it so easy for you to get my waist size."
                    char1.talk "You can already see that it's quite small."
                    pl "Oh... So you don't want to just tell me?"
                    char1.talk "Nope! *chuckles*"
                    char1.talk "I'm pretty sure you'll find a way to persuade me to tell you. *smirks*"
                    pl "If you say so..."
                elif True:
                    $ char1.waist_size_known = True
                    char1.talk "My waist size is [char1.waist_size]"
                    "[char1.fname], I am really impressed, you have such a sexy small waist."
                    $ player.change_lust(char1.sexiness/2 + 1)
                    char1.talk "Thank you [char1.playername] for the nice compliment. But was is really necessary to ask me that?"
                    $ char1.change_affection(-20)
            elif True:
                char1.talk "Why do you want to know that? Do you think I'm too fat?"
            jump talk_others_menu

        "Ask her about her hips size" if char1.hips_size_known == False and option3:
            $ option3 = False
            pl "[char1.fname] I love your hips and butt. Would you tell me your hips size?"
            if char1.check_tease_sexual(1) == True:
                $ char1.hips_size_known = True
                char1.talk "My hips size is [char1.hips_size]"
                "You have an adorable butt and hips."
                $ player.change_lust(char1.sexiness/2 + 1)
                char1.talk "Thank you [char1.playername] for the kind words, but was it necessary to ask that?"
                $ char1.change_affection(-20)
            elif True:
                char1.talk "Why do you want to know that? Don't you like my hips no matter the size?"
            jump talk_others_menu

        "Ask her how tall she is" if char1.body_height_known == False and option4:
            $ option4 = False
            pl "[char1.fname] I would love to know how tall you are."
            if char1.check_affection(0) == True:
                $ char1.body_height_known = True
                char1.talk "My height is [char1.body_height]"
                pl "That's nice to know, thank you [char1.fname] for telling me."
                char1.talk "No problem. It is not that much of a secret."
            elif True:
                char1.talk "I guess this is none of your business."
            jump talk_others_menu

        "Ask for her phone number" if char1.phone_number_known == False and option5:
            $ option5 = False
            pl "Hey [char1.fname] would you tell me your mobile number and messenger data."
            if char1.check_affection(1) == True:
                $ char1.phone_number_known = True
                char1.talk "Sure [char1.playername] here it is. I hope you call me."
                pl "Thank you [char1.fname], I sure will."
            elif True:
                char1.talk "Maybe you can get it later."
            jump talk_others_menu

        "Ask for her room number" if char1.room_number_known == False and option8:
            $ option8 = False
            pl "Ummm... [char1.fname], would you tell me your room number?"
            if char1.id <> sara.id and ((char1.id == amy.id and char1.check_affection(1) == True) or char1.check_affection(2) == True):
                $ char1.room_number_known = True
                char1.talk "Sure [char1.playername] it's room number [char1.room_number]."
                pl "Thank you, that's good to know."
                char1.talk "Don't forget to visit me! *smiles*"
                pl "I won't! *smiling back*"
            elif True:
                char1.talk "I don't know. Maybe you can get it later."
            jump talk_others_menu

        "Ask about her weight" if char1.weight_known == False and option6:
            $ option6 = False
            pl "Umm [char1.fname] I was wondering if you are willing to tell me your weight?"
            if char1.check_affection(3) == True:
                $ char1.weight_known = True
                char1.talk "Hmm okay [char1.playername]. My weight is [char1.weight]. Although I don't know why you need to know this."
                $ char1.change_affection(-30)
                pl "Sorry for asking [char1.fname]."
            elif True:
                char1.talk "Maybe I will tell you later. But I am not sure this is any of your business."
            jump talk_others_menu

        "Ask to meet with her later" if option9 and char1.get_action_allowed("schedule_appointment") == True and char1.is_special_character == False and unicode(location) <> "restaurant":
            $ option9 = False
            $ char1.add_action_cooldown("schedule_appointment", 24, "")
            call visit_girls_room_meet (char1, actions_left, False) from _call_visit_girls_room_meet_3
            jump talk_others_menu

        "Compliment her" if option12 and char1.get_action_allowed("compliment") == True and unicode(location) <> "restaurant":
            call compliment_girl (char1) from _call_compliment_girl
            if _return == True:
                $ option12 = False
            jump talk_others_menu

        "Talk to her about a calendar photo shooting for Nathan" if option10 and char1.fname == alice.fname and (player.get_quest_state("Denim_photo_shootings", jennifer) == 0 or player.get_quest_state("Denim_photo_shootings", jennifer) == 1) and location == "nightbar":
            $ option10 = False
            if player.get_quest_state("Denim_photo_shootings", jennifer) == 0:
                pl "Hey [char1.fname], do you have a minute?"
                if unicode(location) <> "restaurant":
                    call action_closeup (char1, location, False, False) from _call_action_closeup_12
                char1.talk "Sure, what's up?"
                pause 0.4
                pl "I've been talking with Jennifer and there's something you could help her with."
                char1.talk "There is?"
                char1.talk "Okay, I'm listening. *smiles*"
                pause 0.5
                pl "There is this good friend of hers who's a photographer that lost some of his main models recently."
                pl "His name is Nathan."
                pause 0.5
                char1.talk "Oh... {w}I hope you're not asking me to leave the island."
                pl "No, nothing like that."
                pl "He's doing a calendar with women wearing denim."
                pause 0.4
                char1.talk "Oh! So it's a topless calendar?"
                pl "Ummm... No!"
                pl "Not topless, wearing a top would be totally okay. As long as it's sexy looking."
                char1.talk "And quite small and tight I bet... *chuckles*"
                pause 0.5
                pl "Yeah. *grinning sheepishly*"
                pause 0.5
                char1.talk "Why doesn't Jennifer ask me herself?"
                pl "Yes, about that..."
                pl "Nathan would like a guy to take the photos. He thinks a guy would be better at picking the right angles."
                char1.talk "Aha... I see..."
                char1.talk "Why me? I mean there are a lot of beautiful girls on the island?"
                char1.talk "What's the {i}slogan{/i} for that calendar?"
                pause 0.5
                pl "Ummm... It's {w}{i}Super Busty Blondes in Denims{/i}."
                char1.talk "So it's about half covered huge tits... *musing*"
                char1.talk "That wasn't a question. *grins*"
                pause 0.4
                pl "If you put it that way..."
                pl "Are you still willing to help Jennifer and Nathan?"
            elif True:
                pl "Ummm... {w}About the photo shooting for Nathan's the calendar."
                if unicode(location) <> "restaurant":
                    call action_closeup (char1, location, False, False) from _call_action_closeup_13

            if char1.check_anger(4,0,False) == False:
                if player.get_quest_state("Denim_photo_shootings", jennifer) == 0:
                    char1.talk "Basically yes, but I'm still angry with you."
                    char1.talk "That's not a good basis for you being the photographer."
                    pause 0.4
                    pl "Ummm... Okay. Anything I can do in that regard?"
                    char1.talk "Be nice and surprise me."
                    pl "I'll give me best. *smiles*"
                    $ player.set_quest_state("Denim_photo_shootings", jennifer, 1, True)
                elif True:
                    char1.talk "I'm still angry with you, [char1.playername]."
                    char1.talk "Unless you do something about that, it's still a no!"
                    pause 0.5
                    pl "Okay."
            elif True:
                char1.talk "Yes, I'll do it."
                char1.talk "But I want something in return. *smiles*"
                pl "Okay. What is it?"
                pause 0.4
                char1.talk "Nothing complicated."
                char1.talk "I really love those small sweets... *smiles*"
                char1.talk "I just can't get enough of them."
                char1.talk "If you bring me three of those, I'll be all yours for the photo shoot."
                pause 0.5
                char1.talk "Does that sound fair?"
                pl "Sure, I think I can manage to get them. *smiles*"
                char1.talk "Only one of the small sweets per day. You don't want me to get fat, do you? *grins*"
                pause 0.4
                "Damn! That's one of those questions where it's almost impossible to find a good answer..."
                pause 0.5
                "Well, you still have to answer {i}something...{/i}"
                pause 0.5
                pl "I don't see how that could ever happen. I mean, you're perfect!"
                char1.talk "Thank you. *smiles*"
                pl "So we have a deal?"
                pl "I'll get you the sweets."
                pause 0.3
                char1.talk "After that, I'll do the photo shoot with you."
                char1.talk "And I'll select the clothes!"
                pause 0.4
                pl "Of course!"
                $ player.set_quest_state("Denim_photo_shootings", jennifer, 2, True)
            char1.talk "Anything else you'd like to talk about?"
            if unicode(location) <> "restaurant":
                hide screen closeup
                $ g_intimate_char = no_char
                $ location_detail = ""
            jump talk_others_menu

        "Talk to her about a calendar photo shooting for Nathan" if option10 and char1.fname == jessica.fname and player.get_quest_state("Denim_photo_shootings", jennifer) == 8:
            $ option10 = False
            pl "Ummm... [char1.fname], can I talk to you for a moment?"
            if unicode(location) <> "restaurant":
                call action_closeup (char1, location, False, False) from _call_action_closeup_14
            char1.talk "Sure, what's the matter?"
            pause 0.4
            pl "I've been talking with Jennifer and there's something she could use your help with."
            char1.talk "Really? And why doesn't she ask herself?"
            pause 0.5
            pl "Yeah, about that. It involves me too."
            char1.talk "Okay, I'm listening."
            pause 0.4
            pl "Jennifer has a good friend who's a photographer. His name is Nathan."
            pl "He lost some of his main models recently and he urgently needs more models to finish the photo series for a calendar."
            char1.talk "So you're asking me to model for him? *musing*"
            char1.talk "Do I have to leave the island or does he come here?"
            pause 0.4
            pl "Er... No, the plan is for me to take the photos and send him the pictures. Well... Jennifer will actually send him the pictures but I'll do the shoot..."
            pause 0.4
            char1.talk "Oh.. Yes, I've heard about the photo shoots you've done at the studio with some of the girls."
            char1.talk "They say you're good at it."
            char1.talk "So what type of calendar is it?"
            pause 0.5
            pl "Er... Yeah... It's about busty blondes wearing denim..."
            char1.talk "*chuckles* No wonder you're asking me. *chuckles some more*"
            pause 0.4
            pl "To be honest I already did a photo shoot with Alice."
            char1.talk "Now really... And why would you ask her first? *suspiciously*"
            pause 0.4
            pl "Ummm... Jennifer suggested it."
            char1.talk "And why would she do that? *even more suspiciously*"
            pause 0.4
            pl "*gulp* I don't know how to answer that..."
            char1.talk "Spill it out!"
            pl "Okay..."
            pl "She said since you have bigger breasts, I should start with Alice, so we don't spoil Nathan..."
            pl "Like keep the best for last."
            char1.talk "Ha... *grinning*"
            char1.talk "Okay, I'll do it!"
            pause 0.4
            char1.talk "You better wear some reinforced pants... *smirks*"
            char1.talk "You're going to get so hard and horny... *grins*"
            pause 0.4
            pl "*gulp*"
            char1.talk "This is going to be so much fun!"
            char1.talk "When do you want to do this photo shoot?"
            char1.talk "Tomorrow evening at 10pm?"
            pause 0.5
            pl "Er... Yeah, sure."
            $ player.add_appointment(29, char1, "photo_studio", 18, True)
            $ player.inc_quest_state("Denim_photo_shootings", jennifer, True)
            if unicode(location) <> "restaurant":
                char1.talk "Let me give you a hug! *smiles*"
                call action_hug (char1, location, True, 0) from _call_action_hug_12
                show screen main_game(location)
            elif True:
                char1.talk "Cool!"
            pause 0.4
            char1.talk "Anything else you'd like to talk about?"
            jump talk_others_menu

        "Ask if she wants to do another photo session" if player.get_quest_state("Brenda_photo_studio", char1) == 100 and player.has_appointment(25,brenda) == False and (location == "beach" or location == "pool") and char1.get_action_allowed("Brenda_photo_studio") == True:
            pl "Would you like to do another photo session at the studio?"
            if char1.check_love(2,0,False) == False or char1.check_affection(3,0,False) == False:
                $ char1.add_action_cooldown("Brenda_photo_studio", 48, "")
                char1.talk "Sorry, but I'm not really in the mood."
                char1.talk "Maybe ask me again when we know each other a little better, okay?"
                pause 0.4
                pl "Yeah, okay."
                jump talk_others_menu
            elif True:
                $ char1.add_action_cooldown("Brenda_photo_studio", 192, "")
                char1.talk "Sure, I'd love to. I had so much fun last time."
                pause 0.4
                pl "Great, how about this evening?"
                char1.talk "What time do you have in mind?"
                pl "Would 9 pm, after dinner, be okay for you?"
                pl "Yes, that works."
                if unicode(location) <> "restaurant":
                    call action_closeup (char1, location, False) from _call_action_closeup_8
                    char1.talk "Let me give you a hug! *smiles*"
                    pause 0.6
                    call action_hug (char1, location, True, 0) from _call_action_hug_11
                    show screen main_game(location)
                pl "I'll pick you up at your room."
                $ player.add_appointment(25, brenda, "Brenda_room", 20)
                char1.talk "Okay, see you at 9."

        "Talk with her about a swimwear photo session" if (player.get_quest_state("Brenda_photo_studio", char1) == 0 or player.get_quest_state("Brenda_photo_studio", char1) == 1 or (player.get_quest_state("Brenda_photo_studio", char1) == 2 and player.has_appointment(25,brenda) == False)) and (location == "beach" or location == "pool") and char1.get_action_allowed("Brenda_photo_studio") == True:
            $ char1.add_action_cooldown("Brenda_photo_studio", 48, "")
            if player.get_quest_state("Brenda_photo_studio", char1) == 0:
                pl "I've heard that you always wanted to be a swimwear model."
                char1.talk "Yes, that right. Who told you?"
                pause 0.5
                char1.talk "Oh... The letter I put in the mailbox for desires and wishes..."
                char1.talk "So Joy is really taking it seriously and it wasn't just for show."
                pause 0.6
                pl "Since we have that brand new photo studio on the island now..."
                pl "I thought you might want to try it out. *smiles*"
            elif player.get_quest_state("Brenda_photo_studio", char1) == 2:
                pl "Hey [char1.fname], I'm so sorry that I couldn't make it to our appointment for the photo shoot."
                pl "Would you still like to do it?"
            elif True:
                pl "Hey [char1.fname], would you like to do a swimwear photo shoot?"
            if char1.check_love(2,0,False) == False or char1.check_affection(3,0,False) == False:
                char1.talk "Sure. You mean I should talk with Jennifer about it?"
                pl "Ummm... I was thinking that maybe I could take the photos."
                char1.talk "Oh... So you want to take the photos..."
                char1.talk "I don't know if I'm comfortable with that."
                char1.talk "Maybe ask me again once we know each other a little better."
                pause 0.5
                pl "I thought you'd be happy to do it."
                char1.talk "I am, really! But you know it's much better if there is a certain familiarity between the model and the photographer."
                pl "Yeah okay, I can understand that."
                $ player.set_quest_state("Brenda_photo_studio", char1, 1)
                char1.talk "Thank you for understanding, [char1.playername]."
                jump talk_others_menu
            elif True:
                char1.talk "I'd love to!"
                char1.talk "Could you take the photos, [char1.playername]?"
                pl "Yes, that was the plan."
                char1.talk "Cool, it's going to be fun! {w}I hope for both of us. *smirks*"
                pause 0.4
                pl "I have no doubt that I'm going to enjoy it. *smiling*"
                pl "How about this evening?"
                char1.talk "I don't know where the photo studio is. Can you pick me up at me room?"
                pl "Sure, what time do you have in mind?"
                char1.talk "Would 9 pm, after dinner, be okay for you?"
                pl "Yes, that works."
                if unicode(location) <> "restaurant":
                    call action_closeup (char1, location, False) from _call_action_closeup
                    char1.talk "Let me give you a hug! *smiles*"
                    pause 0.6
                    call action_hug (char1, location, True, 0) from _call_action_hug_5
                    show screen main_game(location)
                elif True:
                    char1.talk "Great!"
                $ player.add_appointment(25, brenda, "Brenda_room", 20)
                $ player.set_quest_state("Brenda_photo_studio", char1, 2)

        "Ask if she needs help with anything" if option7:
            $ option7 = False
            pl "[char1.fname], are you okay? You look a bit lost in thoughts or worried."
            if player.get_quest_is_in_pool(char1.fname + " swimwear") == True and gameday >= 12:
                if player.get_quest_state(char1.fname + " swimwear", char1) == 0 or player.get_quest_state(char1.fname + " swimwear", char1) == 10:
                    char1.talk "I've already told you what I need."
                elif player.get_quest_state(char1.fname + " swimwear", char1) == -1:
                    char1.talk "Hmm I don't know how to answer that..."
                    pl "What is it [char1.fname]?"
                    if char1.id == amy.id:
                        char1.talk "I have seen some of the other girls in one of those sexy sling bikinis."
                        char1.talk "Too bad I didn't bring one myself."
                        char1.talk "Maybe you can somehow get one for me? {i}Pretty please{/i}."
                        menu:
                            "Yes" if True:
                                pl "I don't know how yet, but I will think of something and try to get one for you."
                                char1.talk "You are the best [char1.playername]. Let me give you a hug."
                                call action_hug (char1, location, True) from _call_action_hug_1
                                $ player.add_quest(char1.fname + " swimwear", char1, char1)
                                call show_quest_added (char1.fname + " swimwear", char1) from _call_show_quest_added
                            "No" if True:
                                pl "I'm sorry [char1.fname], but I have no idea how to do that."
                                char1.talk "That's too bad, Maybe some other time."
                elif True:
                    char1.talk "I'm ok, nothing to worry about."
                jump talk_others_menu

            char1.talk "I'm ok, nothing to worry about."
            pl "Hmm okay sure."
            jump talk_others_menu

        "Talk to her about the swimsuit photo" if char1.id == aly.id and (player.get_quest_state("Aly_jennifer_swimsuit", aly) == 1 or player.get_quest_state("Aly_jennifer_swimsuit", aly) == 4):
            pl "Hi [char1.fname], I'd like to talk to you about the swimsuit photo."
            if location == "nightbar" or location == "reception" or ( location == "workout" and actions_left <= 44 and actions_left >= 40 ) or len(list_of_chars_display_3) > 1:
                char1.talk "This is probably not the right time and place."
                char1.talk "I don't want Jennifer or anyone else to listen in on the conversation."
                pl "Oh, sure. Didn't think about that. I'll talk to you later."
                char1.talk "Okay great, [char1.playername]."
            elif player.get_quest_state("Aly_jennifer_swimsuit", aly) == 1:
                char1.talk "Sure! Did you ask Jennifer?"
                pl "Yes, about that. She was a bit angry that you showed me her picture."
                char1.talk "Oh really? She didn't say I wasn't supposed to do that..."
                pl "Yeah I know... But still she'd like you to promise not to show it to any of the other girls."
                char1.talk "I don't understand why she wants that, but if that's what it takes to let me wear it..."
                pl "I'm still not sure I can persuade her, but it would be a first step."
                char1.talk "Okay, you can tell her I won't show it to any of the other girls. Promise!"
                pl "Thank you [char1.fname]! I'm sure she appreciates that."
                char1.talk "Still she could have asked me herself..."
                char1.talk "Well, never mind. Let me know if she's willing to lend me the swimsuit."
                pl "Sure [char1.fname]! See you later."
                char1.talk "Bye [char1.playername]."
                $ player.inc_quest_state("Aly_jennifer_swimsuit", aly)
            elif True:
                $ player.inc_quest_state("Aly_jennifer_swimsuit", aly)
                char1.talk "Sure! Did you manage to persuade Jennifer?"
                pl "Yes I did! *smiles*"
                char1.talk "Great! Did she give it to you?"
                pl "Uhmm no, but I think she'll give it to you if you tell her that you will model it for her."
                pl "I told her you would send her some pictures. I hope that's okay with you."
                char1.talk "Absolutely! I love to show off every now and then... *giggles*"
                char1.talk "Just joking. If I can see the pictures you take and decide which ones she gets, I'm okay with it."
                pl "Cool! So you're gonna ask her?"
                char1.talk "Yes! Talk to me again maybe tomorrow and we can set something up to do the pictures."
                pl "Will do [char1.fname]!"
                char1.talk "See you tomorrow."
                pl "Bye!"
                $ char1.add_action_cooldown("Aly_jennifer_swimsuit", 40, "")
                $ actions_used += 1

        "Talk to her about the swimsuit modeling" if char1.id == aly.id and player.get_quest_state("Aly_jennifer_swimsuit", aly) == 5:
            pl "Did you get the swimsuit from Jennifer?"
            if char1.get_action_allowed("Aly_jennifer_swimsuit") == False:
                char1.talk "I haven't spoken with Jennifer yet. Ask me again later!"
                pl "Okay, sure. Bye [char1.fname]!"
            elif True:
                char1.talk "Yes, she gave it to me. I can't wait to see how it looks on me."
                char1.talk "How about tonight at 10:00 pm in my room?"
                pl "Sure, that works for me."
                char1.talk "Don't forget to bring your phone to take some pictures."
                pl "No worries, I won't!"
                char1.talk "Great, see you then."
                pl "See you tonight!"
                $ player.inc_quest_state("Aly_jennifer_swimsuit", aly)
                $ player.check_set_quest_fulfilled("Aly_jennifer_swimsuit", aly)
                $ player.add_appointment(6, aly, "Aly_room", 18)
                $ aly.add_action_cooldown("Clothes1_show_posing", 48, "")

        "Talk to her about the underwear Joy mentioned" if option11 and char1.id == alice.id and location == "nightbar" and player.get_quest_state("Lingerie_presents1_Alice", char1) == 0:
            $ option11 = False
            pl "Hey [char1.fname]!"
            char1.talk "Hi [char1.playername]. *smiles*"
            if player.check_charm(4) == True:
                pl "Did I tell you that you look splendid today?"
                char1.talk "No you didn't."
                if unicode(location) <> "restaurant":
                    call action_closeup (char1, location, False, i_show_text=False) from _call_action_closeup_40
                char1.talk "And thank you! *smiles*"
                char1.talk "Anything I can do for you?"
                pause 0.4
                "Looking at her, a lot of things come to your mind, but you decide to keep them to yourself."
                pause 0.4
                pl "Actually, I was hoping to be able to do something for you. *smiling*"
                char1.talk "Oh really? *grins*"
                pl "I'm collecting ideas about underwear and stuff for Joy."
                pl "She didn't tell me exactly what she wants to do, just that I should ask around."
                pause 0.4
                pl "Is there anything nice you've seen recently that would fit into the category?"
                char1.talk "*chuckles* That's a funny coincidence."
                char1.talk "I was talking with Jennifer about a really cute red underwear and stockings set I've seen just recently."
                pause 0.4
                pl "So you like red underwear?"
                char1.talk "I like all kinds of colors, so it doesn't have to be red."
                char1.talk "But the one I have seen was red and just {b}wow{/b}!"
                pause 0.4
                char1.talk "It looked amazing on the women showcasing it...{w}\n...and she had nowhere near my curves. *winks*"
                char1.talk "I'm pretty sure it would look even better on me."
                pause 0.4
                pl "I'm sure of it. *smiling*"
                char1.talk "Does this give you enough of an idea for now? *smirks*"
                pl "Ummm... Yeah, that's great."
                $ player.inc_quest_state("Lingerie_presents1_Alice", char1, True)
                char1.talk "Maybe we can talk later or have a drink?"
                pl "Sure, I'd love to."
                char1.talk "Great. See you later, [char1.playername]."
                pl "Bye [char1.fname]."
                if unicode(location) <> "restaurant":
                    hide screen closeup
                    $ g_intimate_char = no_char
                    $ location_detail = ""
            elif True:
                pl "Ummm... I wanted to ask what kind of underwear you like."
                char1.talk "What kind of question is that?"
                pause 0.4
                char1.talk "I don't think that's any of your business!"
                pl "I was just asking..."
                pl "I didn't mean to upset you."
                gameplayinfo "Maybe try again with a different approach, when your charm is higher?"
                char1.talk "Okay, whatever..."
                char1.talk "Anything else you want to talk about?"
                pause 0.4
                pl "Er... No."
                char1.talk "Okay. See you later, [char1.playername]."
                pl "Bye [char1.fname]."
        "That's all for now" if True:

            if not option0 or not option1 or not option2 or not option3 or not option4 or not option5 or not option6 or not option7 or not option8 or not option9 or not option12:
                pl "That's all I can think of right now."
                call actions_used (1) from _call_actions_used_17
                $ char1.add_pl_interaction("others")

    $ menu_active = l_menu_active_old
    return "intimate_others"
