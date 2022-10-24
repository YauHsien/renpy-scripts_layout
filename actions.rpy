
# This is an example of Ren'Py scripts.

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




label change_outfit(char1, location1):
    show screen main_game(location1)
    $ l_swimwear_changed = -1
    $ l_nightwear_changed = -1
    $ l_swimwear_special = char1.fname + " swimwear"

    if char1.get_action_allowed("change_outfit") == False:
        $ l_text = char1.get_action_not_allowed_text("change_outfit")
        char1.talk "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_16
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("change_outfit", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    $ menu_active = True

    if char1.id == heather.id:
        $ l_nightwear_special = "Heather_sexy_nurse_outfit"
    elif True:
        $ l_nightwear_special = char1.fname + "_nightwear"

    if location1 in gl_locations_swimwear:
        menu:
            "[char1.fname] would you wear a bathing suit please?" if char1.swimwear <> 0:
                char1.talk "Sure, I can do that for you."
                $ l_swimwear_changed = 0
                if char1.check_love(2, 0, False) == False:
                    if char1.rsm[0].favor >= 5:
                        $ char1.change_favor(-5)
                    elif True:
                        $ char1.change_affection(-5)

            "[char1.fname] would you wear a bikini for me?" if char1.swimwear <> 1:
                if char1.check_affection(2) == True:
                    char1.talk "Sure, I can do that for you."
                    $ l_swimwear_changed = 1
                    if char1.check_love(3, 0, False) == False:
                        if char1.rsm[0].favor >= 8:
                            $ char1.change_favor(-8)
                        elif True:
                            $ char1.change_affection(-8)
                elif True:
                    char1.talk "I need to know you a little better to do that for you."

            "[char1.fname] would you wear your skimpy bikini for me?" if char1.swimwear <> 2:
                if char1.check_tease_sexual(3) == True:
                    char1.talk "Sure, I can do that for you."
                    $ l_swimwear_changed = 2
                    if char1.check_love(3, 0, False) == False:
                        if char1.rsm[0].favor >= 10:
                            $ char1.change_favor(-10)
                        elif True:
                            $ char1.change_affection(-16)
                    $ char1.change_lust(10)
                elif True:
                    char1.talk "I am not in the mood right now."

            "[char1.fname] would you wear your special bikini for me?" if char1.swimwear <> 3 and player.get_display_quest_item(l_swimwear_special) >= 20:
                if player.get_display_quest_item(l_swimwear_special) == 20:
                    pl "I have a gift for you [char1.fname]. I managed to get this swimsuit for you.\nHope you like it."
                    char1.talk "You are so sweet [char1.playername]. Thank you very much."
                    call change_char_max_affection (char1, 10) from _call_change_char_max_affection_5
                    $ char1.change_affection(10)
                    $ char1.change_favor(20)
                    call action_kiss_mouth (char1, location, True, 0) from _call_action_kiss_mouth_3
                    show screen main_game(location)
                    $ player.set_quest_state(l_swimwear_special, char1, 100)
                    $ player.use_item(l_swimwear_special,False)
                elif True:
                    char1.talk "I love that special bikini. Sure I wear it for you."
                $ l_swimwear_changed = 3
            "I've changed my mind" if True:

                pass

    elif location1 in gl_locations_nightwear:
        menu:
            "[char1.fname] would you wear your basic clothes?" if char1.nightwear <> 0:
                char1.talk "Sure, I can do that for you."
                $ l_nightwear_changed = 0
                if char1.check_love(2, 0, False) == False:
                    if char1.rsm[0].favor >= 5:
                        $ char1.change_favor(-5)
                    elif True:
                        $ char1.change_affection(-8)

            "[char1.fname] would you wear something a little bit revealing for me?" if char1.nightwear <> 1:
                if char1.check_affection(2) == True:
                    char1.talk "Sure, I can do that for you."
                    $ l_nightwear_changed = 1
                    if char1.check_love(3, 0, False) == False:
                        if char1.rsm[0].favor >= 8:
                            $ char1.change_favor(-8)
                        elif True:
                            $ char1.change_affection(-12)
                elif True:
                    char1.talk "I need to know you a little better to do that for you."

            "[char1.fname] would you wear your super sexy outfit for me?" if char1.nightwear <> 2:
                if char1.check_tease_sexual(3) == True:
                    char1.talk "Sure, I can do that for you."
                    $ l_nightwear_changed = 2
                    if char1.check_love(3, 0, False) == False:
                        if char1.rsm[0].favor >= 10:
                            $ char1.change_favor(-10)
                        elif True:
                            $ char1.change_affection(-16)
                    $ char1.change_lust(10)
                elif True:
                    char1.talk "I am not in the mood right now."

            "[char1.fname] would you wear your special outfit?" if char1.nightwear <> 3 and player.get_display_quest_item(l_nightwear_special) == 100:
                if char1.id == aly.id:
                    pl "Would you wear your special green and black evening outfit for me?"
                    char1.talk "Sure, I love that outfit. The boots are simply incredible!"
                    $ l_nightwear_changed = 3
                elif char1.id == amy.id:
                    pl "Would you wear your orange dress for me?"
                    char1.talk "Sure, I love that dress! And the heels are incredible too."
                    $ l_nightwear_changed = 3
                elif char1.id == heather.id:
                    pl "[char1.fname], would you wear your nurse costume for me?"
                    char1.talk "I love that cosplay! Sure I'm going to wear it for you. *smiles*"
                    $ l_nightwear_changed = 3
            "I've changed my mind" if True:

                pass

    if l_swimwear_changed >= 0 or l_nightwear_changed >= 0:
        char1.talk "Let me go to my room and change. It won't take longer than half an hour. *smiles*"
        $ char1.add_pl_interaction("others")
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        if l_nightwear_changed >= 0:
            $ char1.nightwear = l_nightwear_changed
        if l_swimwear_changed >= 0:
            $ char1.swimwear = l_swimwear_changed
        call create_list_of_chars_display () from _call_create_list_of_chars_display_1
        $ selected_char = no_char

    $ menu_active = False
    return "intimate_change_outfit"





label chat_char(char1, location1):
    $ location_detail = ""
    show screen main_game(location1)

    if char1.get_action_allowed("chat_char") == False:
        $ l_text = char1.get_action_not_allowed_text("chat_char")
        char1.talk "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_17
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("chat_char", 4, "You wanted to chat not long ago and I already said no!")
        return "nothing"

    if menu_active == False:
        $ l_menu_active_old = False
        $ menu_active = True
    elif True:
        $ l_menu_active_old = True
    $ l_times_talked = 0
    $ l_topic = ""

    $ shopping_last_results = char1.get_last_topic_results("shopping")
    $ sports_last_results = char1.get_last_topic_results("sports")
    $ music_last_results = char1.get_last_topic_results("music")
    $ films_last_results = char1.get_last_topic_results("films")
    $ gossip_last_results = char1.get_last_topic_results("gossip")
    $ politics_last_results = char1.get_last_topic_results("politics")
    $ science_last_results = char1.get_last_topic_results("science")
    $ island_last_results = char1.get_last_topic_results("island")
    $ herself_last_results = char1.get_last_topic_results(char1.get_topic("herself"))
    $ yourself_last_results = char1.get_last_topic_results("yourself")

    label chat_char_menu:
    $ talk_shopping = char1.get_topic_talk_again("shopping")
    $ talk_sports = char1.get_topic_talk_again("sports")
    $ talk_music = char1.get_topic_talk_again("music")
    $ talk_films = char1.get_topic_talk_again("films")
    $ talk_gossip = char1.get_topic_talk_again("gossip")
    $ talk_politics = char1.get_topic_talk_again("politics")
    $ talk_science = char1.get_topic_talk_again("science")
    $ talk_island = char1.get_topic_talk_again("island")
    $ talk_herself = char1.get_topic_talk_again(char1.get_topic("herself"))
    $ talk_yourself = char1.get_topic_talk_again("yourself")

    menu:
        "Talk about shopping [shopping_last_results]" if talk_shopping:
            $ l_topic = "shopping"
            jump chat_char_topic

        "Talk about sports [sports_last_results]" if talk_sports:
            $ l_topic = "sports"
            jump chat_char_topic

        "Talk about music [music_last_results]" if talk_music:
            $ l_topic = "music"
            jump chat_char_topic

        "Talk about movies [films_last_results]" if talk_films:
            $ l_topic = "films"
            jump chat_char_topic

        "Talk about gossip [gossip_last_results]" if talk_gossip:
            $ l_topic = "gossip"
            jump chat_char_topic

        "Talk about politics [politics_last_results]" if talk_politics:
            $ l_topic = "politics"
            jump chat_char_topic

        "Talk about science [science_last_results]" if talk_science:
            $ l_topic = "science"
            jump chat_char_topic

        "Talk about the island [island_last_results]" if talk_island:
            $ l_topic = "island"
            jump chat_char_topic

        "Talk about her [herself_last_results]" if talk_herself:
            $ l_topic = char1.get_topic("herself")
            jump chat_char_topic

        "Talk about yourself [yourself_last_results]" if talk_yourself:
            $ l_topic = "yourself"
            jump chat_char_topic
        "That's all for now" if True:

            jump chat_char_end

    label chat_char_topic:
    $ l_times_talked += 1
    $ chat_content = g_chat.get_topic(l_topic, char1)
    pl "[chat_content.init]"
    $ inclination = char1.get_topic_talk_inclination(l_topic)
    $ l_answer = chat_content.get_answer(inclination)
    char1.talk "[l_answer]"
    $ player.change_lust(chat_content.get_lust_change(inclination))
    $ char1.add_last_topic_result(l_topic, inclination)
    if inclination <> 0:
        if l_topic == "yourself" or l_topic.startswith("herself"):
            $ char1.change_affection(6*inclination)
        elif True:
            $ char1.change_affection(4*inclination)
    jump chat_char_menu

    label chat_char_end:
    $ menu_active = l_menu_active_old
    if l_times_talked > 0:
        if l_times_talked >= 5:
            if player.get_quest_state("Intro_plane_girl", char1) == 0:
                $ player.inc_quest_state("Intro_plane_girl", char1, True)
            call actions_used (2) from _call_actions_used_557
        elif True:
            call actions_used (1) from _call_actions_used_558
        $ char1.add_pl_interaction("others")
    return "intimate_chat"





label action_give_present_restaurant_table(char1):
    pl "Would you follow me to the restaurant entrance, [char1.fname]?"
    char1.fname "Why do you want me to do that?"
    pl "It's a surprise and I hope a nice one."
    pause 0.4
    char1.talk "Okay."
    "You stand up and walk to the main restaurant area."
    $ g_intimate_char = char1
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars
    scene expression l_image_main:
        zoom 0.3334

    call action_give_present (char1, "restaurant", i_transition=dissolve) from _call_action_give_present_5
    $ location_detail = "sit"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_1
    scene expression l_image_main:
        zoom 0.3334
    with dissolve
    "After handing over the present, you sit back at the table."
    $ l_char_focus = no_char
    call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image
    char1.talk "Thanks again, [char1.playername]."
    pl "You're welcome."
    return "intimate_give_present"





label action_give_present(char1, location1, i_gift="", i_show_screen=True, i_actions_used=1, i_transition=None):
    hide screen closeup

    if i_show_screen == True:
        $ location_detail = ""
        show screen main_game(location1)

    if char1.get_action_allowed("present") == False and i_gift == "":
        $ l_text = char1.get_action_not_allowed_text("present")
        "[l_text]"
        if i_show_screen == True:
            show screen main_game(location1)
        $ location_detail = ""
        return "nothing"

    $ location_detail = "intimate"
    $ g_intimate_char = char1
    $ l_zoom_present = 1.0
    $ l_zoom_hug = 1.0
    $ l_zoom_base = 1.0
    $ l_girl_image_base_xpos = 0

    if location1 == "restaurant" or (location1 == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar")):
        $ l_image_name_present = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_present.webp"
        $ l_image_name_hug = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_hug.webp"
        $ l_image_name_base = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_base.webp"
    elif location1 in gl_locations_swimwear:
        $ l_image_name_present = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_present.webp"
        $ l_image_name_hug = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_hug.webp"
        $ l_image_name_base = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_base.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name_present = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_present.webp"
        $ l_image_name_hug = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_hug.webp"
        $ l_image_name_base = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_base.webp"
    elif location1 == "reception":
        $ l_image_name_present = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_present.webp"
        $ l_image_name_hug = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_hug.webp"
        $ l_image_name_base = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_base2.webp"
    elif location1 == "doctor":
        $ l_image_name_present = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_present.webp"
        $ l_image_name_hug = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_hug.webp"
        $ l_image_name_base = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_base.webp"
        $ l_girl_image_base_xpos = -100

    if renpy.loadable(l_image_name_hug):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name_hug)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom_hug = 0.667
        elif l_x_size >= 1000:
            $ l_zoom_hug = 0.5

    if renpy.loadable(l_image_name_present):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name_present)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom_present = 0.667
        elif l_x_size >= 1000:
            $ l_zoom_present = 0.5

    if renpy.loadable(l_image_name_base):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name_base)
        if l_x_size > 800 and l_y_size > 1200:
            $ l_zoom_base = 0.333
        elif l_x_size > 500:
            $ l_zoom_base = 0.5
        if l_x_size > 1000:
            $ l_girl_image_base_xpos = -80

    if not renpy.loadable(l_image_name_present):
        if location1 in gl_locations_swimwear:
            $ l_image_name_present = "characters/!none/none_swim_present.webp"
        elif location1 in gl_locations_nightwear:
            $ l_image_name_present = "characters/!none/none_night_present.webp"
        elif location1 == "reception":
            $ l_image_name_present = "characters/!none/none_reception_present.webp"
        elif location1 == "doctor":
            $ l_image_name_present = "characters/!none/none_night_present.webp"
            $ l_zoom_present = 1.0

    if not renpy.loadable(l_image_name_hug):
        if location1 in gl_locations_swimwear:
            $ l_image_name_hug = "characters/!none/none_swim_hug.webp"
        elif location1 in gl_locations_nightwear:
            $ l_image_name_hug = "characters/!none/none_night_hug.webp"
        elif location1 == "reception":
            $ l_image_name_hug = "characters/!none/none_reception_hug.webp"
        elif location1 == "doctor":
            $ l_image_name_hug = "characters/!none/none_night_hug.webp"
            $ l_zoom_hug = 1.0

    if i_gift == "":
        call screen select_gift(char1, l_image_name_base, l_girl_image_base_xpos, l_zoom_base)
        with i_transition
        if _return == "gift_none" or not unicode(_return).startswith("gift_"):
            $ location_detail = ""
            if i_show_screen == True:
                show screen main_game(location1)
            $ g_intimate_char = no_char
            return "nothing"
        elif True:
            $ l_return_string = unicode(_return)
            $ l_gift_name = l_return_string[5:len(l_return_string)]
    elif True:
        $ l_gift_name = i_gift

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if i_show_screen == True:
        show screen main_game(location1)
    if location1 == "pool" and char1.id == mercedes.id:
        scene expression ("characters/Mercedes/Mercedes_pool_lifeguard_present.webp") with fade:
            zoom 0.5
    elif location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name_present, "", True, i_zoom = l_zoom_present)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name_present, "", True, i_zoom = l_zoom_present)
    elif location1 == "reception":
        show screen intimacy(l_image_name_present, "", True, i_zoom = l_zoom_present)
    elif location1 == "doctor":
        show screen intimacy(l_image_name_present, "locations/loc_doctor_main_overlay.webp", True, l_x_pos, l_zoom_present, 0.5)
    elif True:
        show screen intimacy(l_image_name_present, "", True, i_zoom = l_zoom_present)

    pause 0.5
    pl "[char1.fname], I have a present for you."
    if char1.get_action_allowed("anger_block") == False:
        char1.talk "So you think that will get you off the hook?"
        pl "I'm really sorry for what happened."
        char1.talk "Hmmm... {w}What is it?"
    elif True:
        char1.talk "Ohh, for me? What is it?"
    pl "Why don't you open it and see for yourself.\nI don't want to spoil the surprise. *smiles*"
    "[char1.fname] opens the present."
    pause 1.0
    if l_gift_name == "red rose":
        char1.talk "You got me flowers! Thank you very much [char1.playername]."
        char1.talk "I really love roses."
    elif l_gift_name == "rose perfume":
        char1.talk "Oh wow! You got me some rose fragrance perfume!"
        char1.talk "It's one of my all time favorites. But since it's no longer produced, it's super expensive now."
        char1.talk "Thank you so much, [char1.playername]."
    elif l_gift_name == "sweets small":
        if char1.fname == alice.fname and player.get_quest_state("Denim_photo_shootings", jennifer) >= 2 and player.get_quest_state("Denim_photo_shootings", jennifer) <= 4:
            if char1.get_action_allowed("sweets_small_for_quest") == True:
                $ char1.add_action_cooldown("sweets_small_for_quest", 48)
                char1.talk "I really love those. Thank you, [char1.playername]!"
                $ player.inc_quest_state("Denim_photo_shootings", jennifer, True)
                if player.get_quest_state("Denim_photo_shootings", jennifer) <= 4:
                    char1.talk "Looks like you're doing all you can to have me do that photo shoot. *smiles*"
                    pl "Yes, certainly. We're going to have fun. *grinning*"
                    pl "And it's to help Jennifer."
                    char1.talk "I haven't forgotten. *smiles*"
                elif True:
                    char1.talk "That was the third one. *smiles*"
                    char1.talk "I guess that means we're going to have that photo shooting. *smiles*"
                    pl "Cool. *smiling*"
                    char1.talk "How about tomorrow evening?"
                    pause 0.5
                    pl "Sure, sounds good."
                    pl "Would you like me to pick you up at your room?"
                    pause 0.4
                    char1.talk "Thanks, but I know where it is. We can meet at the studio."
                    pl "Okay. How about 9pm?"
                    char1.talk "Sounds good."
                    $ player.add_appointment(29, char1, "photo_studio", 20, True)
            elif True:
                char1.talk "I told you only one package of sweets per day..."
                char1.talk "So this one doesn't count. {w}But I still take it. *grins*"
                char1.talk "So thank you, [char1.playername]."
                pl "Ummm... {w}You're welcome."
        elif True:
            char1.talk "Thank you [char1.playername] for the sweets!"
            char1.talk "I really appreciate that."
    elif l_gift_name == "sweets large":
        char1.talk "Ohh! A huge box of sweets! Thank you [char1.playername]."
        char1.talk "I guess you're not worried that I'm getting fat... *giggles*"
    elif l_gift_name == "Aly's black rose":
        char1.talk "Oh wow! You got me a black rose!"
        char1.talk "Thank you so much [char1.playername]!"
        pl "You're welcome [char1.fname]."
        char1.talk "I didn't think you could possibly find one and get it to the island for me!"
        char1.talk "You have no idea how happy that makes me. *smiles*"
        char1.talk "As promised, I will send you the bikini picture from the day where I caused quite the commotion."
    elif l_gift_name == "Protein shake apple":
        char1.talk "Cool! My favorite protein shake!"
        char1.talk "How on earth did you get it to the island?"
        pl "I asked around and used some favor. *smiles*"
        char1.talk "You have no idea how happy that makes me. *smiles*"
    elif l_gift_name == "Aly_nightwear":
        char1.talk "Thank you so much [char1.playername]!"
        char1.talk "You got me a green and black outfit! I can't wait to wear it!"
        pl "You're welcome [char1.fname]."
    elif l_gift_name == "Amy's orange rose":
        char1.talk "Oh my god! How did you know this?"
        pl "I have my sources. *smiles*"
        char1.talk "Thank you so much [char1.playername]!"
        char1.talk "I love orange roses. You have no idea how happy you've made me. *smiles*"
        pl "You're welcome, [char1.fname]."
    elif l_gift_name == "Amy's orange dress":
        char1.talk "{b}Oh my god{/b}!"
        char1.talk "The dress is wonderful!"
        char1.talk "And you even got me a matching pair of high heels."
        pl "I'm really happy you like the dress."
        char1.talk "Thank you so much [char1.playername]!"
        pl "You're welcome, [char1.fname]."
    elif l_gift_name == "Heather's nurse dress":
        char1.talk "Oh my god! Joy told you, didn't she?"
        char1.talk "It's wonderful! I love it."
        pl "I'm really happy you like the costume."
        char1.talk "Thank you so much [char1.playername]!"
    elif l_gift_name == "Alice red underwear":
        char1.talk "{b}Oh my god!{/b}"
        char1.talk "Thank you very much, [char1.playername]!"
        pause 0.4
        char1.talk "You got me the amazing lingerie set we talked about!"
        pl "I hope it's the right one."
        pl "And that I got the size right."
        pause 0.4
        char1.talk "It's amazing! Just the one I wanted!"
        char1.talk "I'm sure you got the size right. *smiles*"
        pause 0.4
        pl "Okay. *smiling back*"
        pause 0.4
        char1.talk "Would you like me to send proof that it fits me? *smirks*"
        pause 0.4
        pl "Oh... {w}I'd love to see some pictures when you're wearing it."
        char1.talk "Make sure to check your phone the next couple of days."
        char1.talk "And now let me hug you!"
    elif l_gift_name == "Yvette blue underwear":
        char1.talk "{b}Oh wow!{/b}"
        char1.talk "How did you...?"
        char1.talk "I mean thank you so much! *smiles*"
        pause 0.4
        pl "I hope it's the right one - the one you saw in the boutique."
        pause 0.4
        char1.talk "Yes it is! How did you manage to get it here?"
        char1.talk "How did you even find it?"
        pause 0.4
        pl "I had some help."
        pl "It makes me happy to see you smile. *grinning*"
        char1.talk "I really don't know how to thank you!"
        pause 0.5
        char1.talk "*giggles*"
        pl "What?"
        char1.talk "I think I have an idea. *grins*"
        char1.talk "Check your messages for the next day or so."
        char1.talk "And now come here!"
    elif True:
        char1.talk "Thank you so much [char1.playername]. I absolutely love \"[l_gift_name]\"."

    if location1 == "pool" and char1.id == mercedes.id:
        scene expression ("characters/Mercedes/Mercedes_pool_lifeguard_hug.webp") with fade:
            zoom 0.5
    elif location1 == "nightbar" and (char1.id == jennifer.id or char1.id == yumiko.id):
        show screen intimacy(l_image_name_hug, "locations/loc_nightbar_main_empty.png" )
    elif location == "doctor":
        show screen intimacy(l_image_name_hug, "locations/loc_doctor_main_overlay.webp", False, 300 , l_zoom_hug, 0.5)
    elif True:
        show screen intimacy(l_image_name_hug, i_zoom = l_zoom_hug)

    call use_item_on_girl (l_gift_name, char1) from _call_use_item_on_girl
    "[char1.fname] hugs you tightly."
    pl "It's my pleasure, [char1.fname]."
    $ player.use_item(l_gift_name, False)
    if l_gift_name == "Heather's nurse dress":
        hide screen intimacy
        call action_closeup (char1, location1, False, i_show_text=False) from _call_action_closeup_9
        char1.talk "Can I wear it? I mean like right now?"
        pl "Sure, I'd love to see it on you."
        char1.talk "I'll go to my room and change. I'll be back in no time."
        pl "I'll wait for you."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.nightwear = 3
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        $ char1.locations[actions_left-2] = char1.fname + "_room"
        $ char1.locations[actions_left-3] = "nightbar"

    elif l_gift_name == "sweets small" and player.get_quest_state("Intro_plane_girl", char1) == 9:
        hide screen intimacy
        call action_closeup (char1, location, False, False) from _call_action_closeup_18
        char1.talk "That's great, [char1.playername]. Congratulations!"
        char1.talk "You've successfully finished my sub-quest of the intro quest line."
        pl "I have? That's cool! *smiling*"
        $ player.set_quest_state("Intro_plane_girl", char1, 100, True)
        pause 0.4
        char1.talk "I think a little reward is in order. *smirks*"
        "You just smile at her, admiring her breasts..."
        char1.talk "The way you're staring at my breasts..."
        pl "Ummm..."
        call action_flash_breasts_simple (char1, location, False) from _call_action_flash_breasts_simple_3
        pl "Holy shit, [char1.fname]!"
        char1.talk "You can touch them if you like. *smiles*"
        pl "Oh... Okay. *grinning*"
        "She leans into you, guiding your hand towards her exposed breasts."
        call action_grope (char1, location, True, 0) from _call_action_grope_4
        show screen main_game(location)
        pl "That was pretty hot! And you're too! {w}Hot I mean."
        char1.talk "I know! *winks*"
        char1.talk "And thanks again for the sweets."

    elif char1.get_action_allowed("anger_block") == False:
        char1.talk "Since this was really sweet, I forgive you. {w}This time!"
        pl "Okay. *sheepishly*"
        $ char1.rem_action_cooldown("anger_block")
        hide screen intimacy
    elif True:

        hide screen intimacy

    label action_give_present_end:
    $ char1.add_action_cooldown("present", 16, "You've just given " + char1.fname + " a present not long ago.\nWait a little or it's nothing special any more.")
    $ location_detail = ""
    $ g_intimate_char = no_char
    call actions_used (i_actions_used) from _call_actions_used_15
    $ char1.add_pl_interaction("present")
    return "intimate_give_present"





label action_hug(char1, location1, auto_succeed=False, i_actions_used_add=1, i_show_screen_main_game=True, i_transition=None):
    hide screen closeup

    if char1.get_action_allowed("action_hug") == False and auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("action_hug")
        "[l_text]"
        $ location_detail = ""
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_19
        char1.talk "Hey! Are you trying to hug me?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("action_hug", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    $ l_zoom_old = l_zoom
    $ l_zoom = 1.0
    $ location_detail = "intimate"
    $ g_intimate_char = char1
    if location1 == "restaurant" or (location1 == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar")):
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_hug.webp"
    elif location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_hug.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_hug.webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_hug.webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_hug.webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.667
        elif l_x_size >= 1000:
            $ l_zoom = 0.5

    if not renpy.loadable(l_image_name):
        if location1 in gl_locations_swimwear:
            $ l_image_name = "characters/!none/none_swim_hug.webp"
        elif location1 in gl_locations_nightwear or location1 == "restaurant" or location1 == "doctor":
            $ l_image_name = "characters/!none/none_night_hug.webp"
            $ l_zoom = 1.0
        elif location1 == "reception":
            $ l_image_name = "characters/!none/none_reception_hug.webp"

    if i_show_screen_main_game == True:
        show screen main_game(location1)

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        with i_transition
    elif location1 == "reception":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "doctor":
        show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
    elif True:
        show screen intimacy(l_image_name, i_zoom = l_zoom)

    if auto_succeed == True or char1.check_affection(1) == True:
        if auto_succeed == True or char1.check_lust(1, False) == True:
            $ breast_size_text = char1.get_breast_size_text()
            if char1.fname == ivy.fname:
                "Standing so close to [char1.fname], her [breast_size_text] are almost in your face while you hug her."
                char1.talk "[char1.playername], what is your hand doing on my butt?"
                pl "Ummm..."
                char1.talk "I'm just making fun of you. I don't mind some intimacy."
                $ breast_size_text = char1.get_breast_size_text()
                char1.talk "And you still maintain eye contact."
                char1.talk "With my [breast_size_text] one the same level as your head, that's no small feat. *grins*"
            elif True:
                "You can feel [char1.fname] pull you tighter, pressing her [breast_size_text] against you."
                char1.talk "I hope you enjoyed the hug as much as I did. *smirks*"
            $ lust_change = char1.sexiness // 2
            if lust_change < 2:
                $ lust_change = 2
            $ player.change_lust(lust_change)
        elif True:
            if char1.fname == ivy.fname:
                "You look up at [char1.fname] and hug her."
            elif True:
                "[char1.fname] returns your hug."

        if char1 in gl_girls_new_max_logic:
            $ char1.change_love(4)
        elif True:
            call change_char_max_affection (char1, 2) from _call_change_char_max_affection_6
            $ char1.change_love(2)
        $ char1.change_lust(4)
    elif True:
        char1.talk "Hey [char1.playername], what are you doing? Stop that."
        $ char1.change_anger(5)
        pl "Oh, I am sorry [char1.fname]. I did not want to embarrass you or make you feel uncomfortable."
        char1.talk "It's okay [char1.playername], just don't do it again until we know each other a little better."
        $ char1.change_anger(-3)

    hide screen intimacy
    $ l_zoom = l_zoom_old
    $ location_detail = ""
    $ g_intimate_char = no_char
    $ actions_used += i_actions_used_add
    $ char1.add_pl_interaction("hug/kiss")
    $ char1.add_action_cooldown("action_hug", 4, "You've just hugged me. Give me a break.")
    return "intimate_hug"





label action_hug_simple(char1, location1, i_image_detail="", i_transition=dissolve):
    hide screen closeup
    $ l_zoom = 1.0
    $ location_detail = "intimate"
    $ g_intimate_char = char1
    if location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_hug" + unicode(i_image_detail) + ".webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_hug" + unicode(i_image_detail) + ".webp"
    elif location1 == "restaurant":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_hug" + unicode(i_image_detail) + ".webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_hug" + unicode(i_image_detail) + ".webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + "_hug" + unicode(i_image_detail) + ".webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.667
        elif l_x_size >= 1000:
            $ l_zoom = 0.5

    if not renpy.loadable(l_image_name):
        if location1 in gl_locations_swimwear:
            $ l_image_name = "characters/!none/none_swim_hug.webp"
        elif location1 in gl_locations_nightwear or location1 == "restaurant" or location1 == "doctor":
            $ l_image_name = "characters/!none/none_night_hug.webp"
            $ l_zoom = 1.0
        elif location1 == "reception":
            $ l_image_name = "characters/!none/none_reception_hug.webp"

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "reception":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "doctor":
        show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
    elif True:
        show screen intimacy(l_image_name, i_zoom = l_zoom)
    with i_transition

    $ char1.add_pl_interaction("hug/kiss")
    return "nothing"





label action_hug_restaurant_table(char1):
    pl "[char1.fname]?"
    char1.fname "What is it?"
    pl "Can I hug you?"
    if char1.get_action_allowed("anger_block") == False:
        char1.talk "Now?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        $ char1.add_action_cooldown("action_hug", 4, "We had this not long ago. It's still {b}no{/b}!")
        return "nothing"

    if char1.check_affection(1) == False:
        char1.talk "Maybe once I know you a little better, okay?"
        pl "If you say so. *a little sad*"
        $ char1.add_action_cooldown("action_hug", 4, "We had this not long ago. It's still {b}no{/b}!")
        return "nothing"

    char1.talk "Sure, but we better stand up to do that."
    "You stand up and walk to the main restaurant area."
    $ g_intimate_char = char1
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_2
    scene expression l_image_main:
        zoom 0.3334

    call action_hug (char1, "restaurant", auto_succeed=True, i_transition=fade) from _call_action_hug_17
    $ location_detail = "sit"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_3
    scene expression l_image_main:
        zoom 0.3334
    with dissolve
    "After the hug, you sit back at the table."
    $ l_char_focus = no_char
    call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image_1
    char1.talk "That was nice, [char1.playername]."
    pl "I really enjoyed the hug too."
    return "intimate_hug"





label action_kiss_mouth_restaurant_table(char1):
    pl "Can I kiss you, [char1.fname]?"
    if char1.get_action_allowed("anger_block") == False:
        char1.talk "What?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        $ char1.add_action_cooldown("action_kiss_mouth", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    if char1.check_affection(2) == False:
        char1.talk "I don't know you well enough, so we better don't."
        pl "Okay. *a little sad*"
        $ char1.add_action_cooldown("action_kiss_mouth", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    char1.talk "Okay, but not while we're sitting at the table."
    char1.talk "Let's head over there so we have a little more space."
    pl "Okay."
    "You stand up and head to the main restaurant area."
    $ g_intimate_char = char1
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_4
    scene expression l_image_main:
        zoom 0.3334

    call action_kiss_mouth (char1, "restaurant", auto_succeed=True, i_transition=fade) from _call_action_kiss_mouth_2
    $ location_detail = "sit"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_5
    scene expression l_image_main:
        zoom 0.3334
    with dissolve
    "After the incredible kiss, you sit back at the table."
    $ l_char_focus = no_char
    call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image_2
    char1.talk "That was cute, [char1.playername]."
    pl "Yeah, I really enjoyed the kiss."
    return "intimate_kiss_mouth"





label action_kiss_mouth(char1, location1, auto_succeed=False, i_actions_used_add=1, i_show_screen_main_game=True, i_transition=None):
    hide screen closeup

    if char1.get_action_allowed("action_kiss_mouth") == False and auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("action_kiss_mouth")
        "[l_text]"
        $ location_detail = ""
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_20
        char1.talk "Hey! Are you trying to kiss me?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("action_kiss_mouth", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    $ l_zoom_old = l_zoom
    $ l_zoom = 1.0
    $ location_detail = "intimate"
    $ g_intimate_char = char1
    if location1 == "restaurant" or (location1 == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar")):
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_kiss.webp"
    elif location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_kiss.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_kiss.webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_kiss.webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_kiss.webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.667
        elif l_x_size >= 1000:
            $ l_zoom = 0.5

    if not renpy.loadable(l_image_name):
        if location1 in gl_locations_swimwear:
            $ l_image_name = "characters/!none/none_swim_kiss.webp"
        elif location1 in gl_locations_nightwear or location1 == "restaurant" or location1 == "doctor":
            $ l_image_name = "characters/!none/none_night_kiss.webp"
            $ l_zoom = 1.0
        elif location1 == "reception":
            $ l_image_name = "characters/!none/none_reception_kiss.webp"

    if i_show_screen_main_game == True:
        show screen main_game(location1)

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        with i_transition
    elif location1 == "reception":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "doctor":
        show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
    elif True:
        show screen intimacy(l_image_name, i_zoom = l_zoom)

    if auto_succeed == True or char1.check_affection(2) == True:
        $ l_kiss_okay = True
        if auto_succeed == True or char1.check_lust(1, False) == True:
            $ breast_size_text = char1.get_breast_size_text()
            if char1.height_type <> 4:
                "During the kiss, you can feel that [char1.fname] is also hugging you pretty tight. You can feel her [breast_size_text] pressing against you."
                char1.talk "I hope you enjoyed our kiss as much as I did. *smirks*"
            elif True:
                "During the kiss, [char1.fname] lifts you easily. You can feel her [breast_size_text] pressing against your chest."
                char1.talk "Next time I get more than a kiss from you. *smirks*"
            $ lust_change = char1.sexiness
            if lust_change < 4:
                $ lust_change = 4
            $ player.change_lust(lust_change)
        elif True:
            "[char1.fname] seemed to enjoy the kiss."

        if char1 in gl_girls_new_max_logic:
            $ char1.change_love(6)
        elif True:
            call change_char_max_love (char1, 2) from _call_change_char_max_love_5
            $ char1.change_love(4)
        $ char1.change_lust(8)

        if player.get_quest_state("Intro_plane_girl", char1) == 8:
            $ player.inc_quest_state("Intro_plane_girl", char1, True)
    elif True:
        char1.talk "Hey [char1.playername], what are you doing? Stop that."
        $ char1.change_anger(10)
        pl "Oh, I am sorry [char1.fname] that I went too far."
        char1.talk "It's okay [char1.playername], just don't do it again until we know each other a little better."
        $ char1.change_anger(-5)

    hide screen intimacy
    $ l_zoom = l_zoom_old
    if auto_succeed == True:
        hide screen main_game
    $ location_detail = ""
    $ g_intimate_char = no_char
    $ actions_used += i_actions_used_add
    $ char1.add_pl_interaction("hug/kiss")
    $ char1.add_action_cooldown("action_kiss_mouth", 4, "You've just kissed me. Give me a break.")
    return "intimate_kiss_mouth"





label action_grope_restaurant_table(char1):
    pl "This might sound a bit awkward..."
    char1.talk "What is it, [char1.playername]?"
    pause 0.4
    pl "Can I fondle your amazing breasts?"

    if char1.get_action_allowed("anger_block") == False:
        char1.talk "You want {b}what{/b}?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        $ char1.add_action_cooldown("action_kiss_mouth", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    if char1.relationship_type == 2:
        $ _return = char1.check_tease_sexual(1, 0, False)
    elif char1.relationship_type == 1:
        $ _return = char1.check_tease_sexual(2, 0, False)
    elif True:
        $ _return = char1.check_tease_sexual(3, 0, False)

    if _return == False:
        char1.talk "Really, [char1.playername]?"
        $ char1.change_anger(5)
        $ char1.change_affection(-4)
        char1.talk "What kind of request is that?"
        pl "I'm sorry that I went too far, [char1.fname]."
        if char1.check_affection(2,0,False) == True:
            char1.talk "It's okay [char1.playername], just don't ask again until I'm in the right mood!"
            $ char1.change_anger(-5)
        $ char1.add_action_cooldown("action_kiss_mouth", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    char1.talk "Someone is being naughty. *smirks*"
    char1.talk "Let's head over to the entrance where we have a little more space."
    pl "Sure. *grinning*"
    "You stand up and head to the entrance of the restaurant."
    $ g_intimate_char = char1
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_6
    scene expression l_image_main:
        zoom 0.3334

    call action_grope (char1, "restaurant", auto_succeed=True, i_transition=fade) from _call_action_grope_6
    $ location_detail = "sit"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_7
    scene expression l_image_main:
        zoom 0.3334
    with dissolve
    "After the incredible fondling and groping of her breasts, you sit back at the table."
    $ l_char_focus = no_char
    call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image_3
    char1.talk "That was kinky, [char1.playername]."
    pl "Yeah, a little. But damn, your breasts are amazing."
    char1.talk "Are they? *smirks*"
    return "intimate_grope"





label action_grope(char1, location1, auto_succeed=False, i_actions_used_add=1, i_show_screen_main_game=True, i_transition=None):
    hide screen closeup

    if char1.get_action_allowed("action_grope") == False and auto_succeed == False:
        show screen main_game(location1)
        $ l_text = char1.get_action_not_allowed_text("action_grope")
        "[l_text]"
        $ location_detail = ""
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_21
        char1.talk "Hey! Are you trying to grope me?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("action_grope", 4, "You just tried to this not long ago. It's still {b}no{/b}!")
        return "nothing"

    $ l_zoom = 1.0
    $ location_detail = "intimate"
    $ g_intimate_char = char1
    if location1 == "restaurant" or (location1 == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar")):
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_grope.webp"
    elif location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_grope.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_grope.webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_grope.webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_grope.webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.667
        elif l_x_size >= 1000:
            $ l_zoom = 0.5

    if not renpy.loadable(l_image_name):
        if location1 in gl_locations_swimwear:
            $ l_image_name = "characters/!none/none_swim_grope.webp"
        elif location1 in gl_locations_nightwear or location1 == "restaurant" or location1 == "doctor":
            $ l_image_name = "characters/!none/none_night_grope.webp"
            $ l_zoom = 1.0
        elif location1 == "reception":
            $ l_image_name = "characters/!none/none_reception_grope.webp"

    if i_show_screen_main_game == True:
        show screen main_game(location1)

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        with i_transition
    elif location1 == "reception":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "doctor":
        show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
    elif True:
        show screen intimacy(l_image_name, i_zoom = l_zoom)

    $ char1.execute_special_action(location1, "G")

    if auto_succeed == False:
        if char1.relationship_type == 2:
            $ _return = char1.check_tease_sexual(1, 0, False)
        elif char1.relationship_type == 1:
            $ _return = char1.check_tease_sexual(2, 0, False)
        elif True:
            $ _return = char1.check_tease_sexual(3, 0, False)
    elif True:
        $ _return = True
    if _return == True:
        if auto_succeed == False:
            if char1.relationship_type == 2:
                $ _return = char1.check_lust(1, False)
            elif char1.relationship_type == 1:
                $ _return = char1.check_lust(2, False)
            elif True:
                $ _return = char1.check_lust(3, False)
        elif True:
            $ _return = True
        if _return == True:
            $ breast_size_text = char1.get_breast_size_text()
            "While you grope and fondle her [breast_size_text], [char1.fname] presses her firm ass against your dick!"
            char1.talk "You're a naughty boy, [char1.playername]! *smirks*"
            pause 0.4
            char1.talk "So I'm a naughty girl for you too!"
            $ lust_change = char1.sexiness + 4
            if lust_change < 8:
                $ lust_change = 8
            $ player.change_lust(lust_change)
            $ char1.change_lust(20)
        elif True:
            "[char1.fname] got a bit turned on by your fondling..."
            $ char1.change_lust(12)
            "...but she didn't really enjoy it."
            $ char1.change_affection(-6)
    elif True:
        char1.talk "Hey [char1.playername], what are you doing? Stop that right now!!!"
        $ char1.change_anger(10)
        $ char1.change_affection(-8)
        pl "I'm really sorry that I went too far, [char1.fname]."
        if char1.check_affection(2,0,False) == True:
            char1.talk "It's okay [char1.playername], just don't do it again until I'm in the right mood!"
            $ char1.change_anger(-5)
        elif True:
            char1.talk "You better be! I won't forget this anytime soon!"
            if (location in gl_locations_swimwear or location in gl_locations_nightwear) and len(list_of_chars_display_3) > 1:
                $ char1.add_action_cooldown("anger_block", 16, ["After you groped me in front of the other girls? I don't think so!", "I'm still angry with you. Groping me in front of the other girls wasn't funny!", "Leave me alone! Why don't you grope someone else!"])
            elif True:
                $ char1.add_action_cooldown("anger_block", 16, ["After you groped me without my consent? I don't think so!", "Leave me alone! Why don't you grope someone else!", "I'm still angry with you. You can't just grope me!"])

    if _return == True and location1 == "nightbar" and char1.id == sara.id and char1.nightwear == 3 and char1.check_lust(3, False) == True:
        pause 0.7
        if len(list_of_chars_display_3) > 1:
            char1.talk "Too bad we're not alone right now..."
            pl "Why do you say that?"
            char1.talk "Just a thought. *smirks*"
            jump action_grope_end
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_grope2.webp"
        char1.talk "[char1.playername]..."
        pl "Yeah?"
        char1.talk "I want you to use both hands."
        pl "Are you sure?"
        char1.talk "Don't you want to?"
        pl "I'd love to!"
        char1.talk "So what are you waiting for?"
        show screen intimacy(l_image_name, i_zoom = l_zoom) with dissolve
        pause 0.6
        char1.talk "Do you like how round and firm they are?"
        $ player.change_lust(char1.sexiness)
        pl "They're amazing!"
        pause 0.5
        char1.talk "I hope my butt doesn't press too hard against your crotch. *smirks*"
        pl "Er... No, it's fine."
        $ player.change_lust(char1.sexiness)
        "Damn! What is she doing?"
        if char1.check_lust(4, False) == False:
            char1.talk "You better let go of my breasts now, before we have an accident. *grins*"
            pl "Ummm... Yeah, okay."
            jump action_grope_end

        $ char1.change_lust(10)
        pl "Wow! Your nipples are really hard."
        char1.talk "They're telling you to caress them with your hands and play with them."
        pl "I guess in that case, I need to oblige. *grinning*"
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_grope3.webp"
        show screen intimacy(l_image_name, i_zoom = l_zoom) with dissolve
        pause 0.7
        "While you play with her hard nipples, she rubs her butt even more against your hardening dick."
        $ player.change_lust(char1.sexiness+4)
        $ player.add_effect("erection")
        char1.talk "*giggles*"
        char1.talk "I got you rock hard! I can feel it."
        pl "What did you expect? I'm just a guy."
        char1.talk "Oh... I expected that it wouldn't take you so long. *grins*"
        pause 0.4
        pl "Haha, funny. *laughs*"
        char1.talk "Would you like me to..."
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_grope4.webp"
        show screen intimacy(l_image_name, i_zoom = l_zoom) with dissolve
        pause 0.3
        $ player.change_lust(char1.sexiness+4)
        pause 0.4
        pl "Damn! What are you doing?"
        char1.talk "You don't like it when I do this?"
        pl "Of course I do, but I don't want to cum in my pants..."
        pause 0.4
        pl "... and I will if you don't stop right now."
        pause 0.4
        char1.talk "Are you sure that you don't want me to continue just little longer? *smirks*"
        pause 0.4
        pl "Yes, please stop."
        char1.talk "Okay."
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_grope3.webp"
        show screen intimacy(l_image_name, i_zoom = l_zoom) with dissolve
        pause 0.7
        char1.talk "But I think in that case, you need to stop too."
        pl "Yeah, sorry."
        char1.talk "No need to be sorry. I really enjoyed it."
        $ char1.add_scene_seen("Nightbar_grope3")

    label action_grope_end:
    hide screen intimacy
    if auto_succeed == True:
        hide screen main_game
    $ location_detail = ""
    $ g_intimate_char = no_char
    $ actions_used += i_actions_used_add
    $ char1.add_pl_interaction("others")
    $ char1.add_action_cooldown("action_grope", 4, "You've just fondled my breasts! Give me a break.")
    return "intimate_grope"





label action_flash_breasts(char1, location1, auto_succeed=False, i_actions_used_add=1, i_show_screen_main_game=True):
    hide screen closeup
    $ location_detail = ""

    show screen main_game(location1)
    pl "Ummm [char1.fname]..."
    char1.talk "Yes [char1.playername]? What is it?"
    pl "Would you flash your breasts for a moment?"

    if char1.get_action_allowed("action_flash_breasts") == False and auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("action_flash_breasts")
        "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_22
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("action_flash_breasts", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    if location1 == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar"):
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_flash_breasts.webp"
    elif location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_flash_breasts.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_flash_breasts.webp"
    elif location1 == "restaurant":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_restaurant_table" + unicode(char1.dinerwear) + "_flash_breasts.webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_flash_breasts.webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_flash_breasts.webp"

    if location1 <> "restaurant_table":
        $ l_zoom = 1.0
        if renpy.loadable(l_image_name):
            $ l_x_size,l_y_size = renpy.image_size(l_image_name)
            if l_x_size > 750 and l_x_size < 1000:
                $ l_zoom = 0.667
            elif l_x_size >= 1000:
                $ l_zoom = 0.5

    if auto_succeed == False:
        if char1.check_anger(3, 0, True) == False:
            char1.talk "How dare you even ask that? I'm still angry with you."
            char1.talk "It's not going to happen right now!"
            $ char1.add_action_cooldown("action_flash_breasts", 4, "You asked me to expose my breasts not long ago! Give me a break.")
            return "nothing"

    if auto_succeed == False:
        if char1.relationship_type == 2:
            $ _return = char1.check_tease_sexual(1, 0, False)
        elif char1.relationship_type == 1:
            $ _return = char1.check_tease_sexual(2, 0, False)
        elif True:
            $ _return = char1.check_tease_sexual(3, 0, False)
    elif True:
        $ _return = True
    if _return == False:
        char1.talk "Hey [char1.playername], I'm not in the mood right now!"
        char1.talk "It's not funny asking something like that!"
        $ char1.change_anger(7)
        $ char1.change_affection(-5)
        $ char1.add_action_cooldown("action_flash_breasts", 4, "You asked me to expose my breasts not long ago! Give me a break.")
        return "nothing"

    if not renpy.loadable(l_image_name) and location1 <> "restaurant_table":
        show screen main_game(location1)
        if location1 in gl_locations_swimwear:
            char1.talk "Sorry, but with this particular swimwear it's just too complicated."
        elif True:
            char1.talk "Sorry, but I don't think this will work when I'm wearing these clothes."
        return "nothing"

    if char1.relationship_type <= 0 and location1 <> "restaurant_table":
        if len(list_of_chars_display_3) > 1:
            if char1.check_love(3, 0, False) == False:
                show screen main_game(location1)
                char1.talk "What kind of girl do you take me for?"
                char1.talk "I'm not exposing my breasts when some of the other girls are watching!"
                $ char1.change_anger(5)
                $ char1.add_action_cooldown("action_flash_breasts", 4, "You asked me to expose my breasts not long ago! Give me a break.")
                return "nothing"
            elif True:
                show screen main_game(location1)
                char1.talk "Ummm... We're not alone right now!"
                char1.talk "Some of the other girls are watching..."
                pause 0.3
                pl "If I say pretty please?"
                pause 0.3
                char1.talk "All right, since I'm really into you! *smiles*"
                char1.talk "Let me get a little closer..."
                jump action_flash_breasts_after_love_check

    elif char1.relationship_type <= 0 and location == "restaurant_table" and len(l_girls_at_table) > 1:
        if char1.check_love(3, 0, False) == False:
            char1.talk "What kind of girl do you take me for?"
            char1.talk "I'm not exposing my breasts when some of the other girls are sitting at the same table!"
            $ char1.change_anger(5)
            $ char1.add_action_cooldown("action_flash_breasts", 4, "You asked me to expose my breasts not long ago! Give me a break.")
            return "nothing"
        elif True:
            char1.talk "Ummm... We're not alone right now!"
            char1.talk "Some of the other girls are watching..."
            pause 0.3
            pl "If I say pretty please?"
            pause 0.3
            char1.talk "All right, since I'm really into you! *smiles*"
            jump action_flash_breasts_after_love_check

    if location1 <> "restaurant_table":
        if i_show_screen_main_game == True:
            show screen main_game(location1)

        char1.talk "Sure! *giggles*"
        char1.talk "But I really should get a little closer to you to show my goodies, don't you agree? *smiles*"
    elif True:
        char1.talk "Sure! *giggles*"

    label action_flash_breasts_after_love_check:
    $ char1.execute_special_action(location1, "F")
    if location1 <> "restaurant_table":
        pl "Absolutely! *grinning*"
        $ location_detail = "intimate"
        $ g_intimate_char = char1
    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "restaurant":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "reception":
        show screen intimacy(l_image_name, "", i_zoom = l_zoom)
    elif location1 == "doctor":
        show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
    elif location1 == "restaurant_table":
        if char1 == l_char1:
            $ l_images=["flash_breasts",1,1]
        elif char1 == l_char2:
            $ l_images=[1,"flash_breasts",1]
        elif char1 == l_char3:
            $ l_images=[1,1,"flash_breasts"]
        call scene_restaurant_table_image (l_images, i_use_current_zoom_align=True) from _call_scene_restaurant_table_image_4
    elif True:
        show screen intimacy(l_image_name, "", False, l_x_pos, l_zoom)

    pause 1.0
    $ l_breast_size_text = char1.get_breast_size_text()

    char1.talk "Here are my [l_breast_size_text]. Just for you! *smiles*"
    $ char1.change_lust(10)
    if char1.relationship_type > 0:
        if char1.check_lust(2, False) == True:
            if char1.breast_size >= 2:
                $ l_breast_size_text = char1.get_breast_size_text()
                char1.talk "Do you think about me and my [l_breast_size_text] when you masturbate?"
                char1.talk "I bet you dream about rubbing your dick between them."
            elif True:
                char1.talk "I bet you imagine me topless when you masturbate!"
            pl "Ummm... [char1.fname]!"
            char1.talk "I'm just teasing. You don't have to answer that [char1.playername]!"
            pause 0.5
            char1.talk "Is it working? *giggles*"
            "Yes, it definitely is working. You can feel it getting warmer and warmer!"
            $ player.change_lust(char1.sexiness + 4)
            $ char1.add_pl_interaction("tease_boobs")
        elif True:
            char1.talk "From the look in your eyes, I can see that you enjoy the view!"
            pl "Very much so [char1.fname]!"
            pl "You have incredible breasts."
            char1.talk "Thank you, I know. *smiles*"
            "The sight of her naked tits right in front of you is turning you on!"
            $ player.change_lust(char1.sexiness)
            $ char1.add_pl_interaction("others")
    elif True:
        if char1.check_lust(3, False) == True:
            $ l_breast_size_text = char1.get_breast_size_text()
            char1.talk "Do you dream about my [l_breast_size_text] before you fall asleep?"
            "Not only before you go to sleep, but also when you jerk off..."
            "...but you're not going to tell her that."
            $ player.change_lust(char1.sexiness + 4)
            pl "Er... Ummm..."
            char1.talk "I love it when you get embarrassed! It's really cute! *smiles*"
            pl "Uhhh okay *smiles back*"
            $ char1.add_pl_interaction("tease_boobs")
        elif True:
            char1.talk "From the look in your eyes, I can see that you enjoy the view!"
            pl "Very much so [char1.fname]!"
            pl "You have incredible breasts."
            char1.talk "Thank you [char1.playername]! You are sweet! *smiles*"
            "The sight of her naked tits right in front of you is turning you on!"
            $ player.change_lust(char1.sexiness)
            $ char1.add_pl_interaction("others")

    char1.talk "*giggles* I think you've stared long enough now!"
    char1.talk "I'll wrap them back up, before we get any accidents. *smirks*"
    "You're a bit disappointed that the show's over so soon."
    pause 1.0
    char1.talk "Hey, don't give me that look."
    char1.talk "I'm sure you'll have plenty of opportunities to see them again! *smiles*"
    if location1 in gl_locations_swimwear:
        "She wraps her tits back up in her bikini top and takes a step back."
    elif location1 == "restaurant_table":
        "She puts her tits back in, still smiling at you."
    elif True:
        "She wraps her tits back up and takes a step back."

    if location1 <> "restaurant_table":
        hide screen intimacy
        if auto_succeed == True:
            hide screen main_game
        $ location_detail = ""
        $ g_intimate_char = no_char
    elif True:
        call scene_restaurant_table_image ([1,1,1], i_use_current_zoom_align=True) from _call_scene_restaurant_table_image_5

    call actions_used (1) from _call_actions_used_463
    $ char1.add_pl_interaction("topless")
    $ char1.add_action_cooldown("action_flash_breasts", 4, "I've just shown you my breasts! Give me a break.")
    return "intimate_flash_breasts"





label action_pose_butt_restaurant_table(char1):
    pl "[char1.fname]?"
    char1.fname "[char1.playername]?"
    pl "That's a bit awkward, but would you show me your butt?"
    if char1.get_action_allowed("anger_block") == False:
        char1.talk "Now?"
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        $ char1.add_action_cooldown("action_pose_butt", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    if char1.check_anger(2, 0, True) == False:
        char1.talk "How dare you even ask that? I'm still angry with you."
        char1.talk "It's not going to happen right now!"
        $ char1.add_action_cooldown("action_pose_butt", 4, "You asked me to pose my butt not long ago! Give me a break.")
        return "nothing"

    if char1.relationship_type == 2:
        $ _return = char1.check_lust(1, False)
    elif char1.relationship_type == 1:
        $ _return = char1.check_lust(0, False)
    elif True:
        $ _return = char1.check_tease_sexual(2, 0, False)
    if _return == False:
        char1.talk "Sorry [char1.playername], but I'm not in the mood right now!"
        char1.talk "Why do you even ask something like that?"
        $ char1.change_anger(7)
        $ char1.change_affection(-5)
        $ char1.add_action_cooldown("action_pose_butt", 4, "You asked me to pose my butt not long ago! Give me a break.")
        return "nothing"

    char1.talk "Okay, let's head over to the entrance."
    char1.talk "You can't see my butt while I'm sitting on the chair. *smiles*"
    pl "Thank you. *smiling*"
    "You stand up and walk to the main restaurant area."
    $ g_intimate_char = char1
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_8
    scene expression l_image_main:
        zoom 0.3334

    call action_pose_butt (char1, "restaurant", auto_succeed=True, i_transition=fade, i_show_intro=False) from _call_action_pose_butt_3
    $ location_detail = "sit"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_9
    scene expression l_image_main:
        zoom 0.3334
    with dissolve
    "After enjoying the incredible sight of her behind, you sit back at the table."
    $ l_char_focus = no_char
    call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image_6
    char1.talk "I hope you enjoyed the view, [char1.playername]."
    pl "Yeah, definitely. *ginning*"
    return "intimate_pose_butt"





label action_pose_butt(char1, location1, auto_succeed=False, i_actions_used_add=1, i_show_screen_main_game=True, i_transition=dissolve, i_show_intro=True):
    hide screen closeup
    $ location_detail = ""
    $ l_image_name_horny = ""

    $ l_zoom = 0.3334
    $ l_main_zoom = 0.5
    show screen main_game(location1)
    if i_show_intro == True:
        pl "[char1.fname], can I ask you something?"
        char1.talk "Sure [char1.playername], what is it?"
        pl "Would you pose your butt for me?"

    if char1.get_action_allowed("action_pose_butt") == False and auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("action_pose_butt")
        "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_41
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("action_pose_butt", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    if location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_pose_butt.webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_pose_butt.webp"
    elif location1 == "restaurant":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_pose_butt.webp"
        $ l_main_zoom = 0.3334
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_pose_butt.webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_pose_butt.webp"
        $ l_image_name_horny = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_pose_butt_expose.webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.6667
        elif l_x_size >= 1000:
            $ l_zoom = 0.3334

    if auto_succeed == False:
        if char1.check_anger(2, 0, True) == False:
            char1.talk "How dare you even ask that? I'm still angry with you."
            char1.talk "It's not going to happen right now!"
            $ char1.add_action_cooldown("action_pose_butt", 4, "You asked me to pose my butt not long ago! Give me a break.")
            return "nothing"

    if auto_succeed == False:
        if char1.relationship_type == 2:
            $ _return = char1.check_lust(1, False)
        elif char1.relationship_type == 1:
            $ _return = char1.check_lust(0, False)
        elif True:
            $ _return = char1.check_tease_sexual(2, 0, False)
    elif True:
        $ _return = True
    if _return == False:
        char1.talk "Sorry [char1.playername], but I'm not in the mood right now!"
        char1.talk "Why do you even ask something like that?"
        $ char1.change_anger(7)
        $ char1.change_affection(-5)
        $ char1.add_action_cooldown("action_pose_butt", 4, "You asked me to pose my butt not long ago! Give me a break.")
        return "nothing"

    if not renpy.loadable(l_image_name):
        show screen main_game(location1)
        char1.talk "Sorry, but this has not been implemented yet."
        return "nothing"

    if char1.relationship_type <= 0 and auto_succeed == False:
        if len(list_of_chars_display_3) > 1:
            if char1.check_love(2, 0, False) == False:
                show screen main_game(location1)
                char1.talk "I'm not sticking out my butt for you when some of the girls are watching!"
                $ char1.change_anger(5)
                $ char1.add_action_cooldown("action_pose_butt", 4, "You asked me to pose my butt not long ago! Give me a break.")
                return "nothing"
            elif True:
                show screen main_game(location1)
                char1.talk "Ummm... We're not alone right now!"
                char1.talk "Some of the other girls are watching..."
                pause 0.3
                pl "If I say pretty please?"
                pause 0.3
                char1.talk "All right, since I'm really into you! *smiles*"
                jump action_pose_butt_after_love_check

    if i_show_screen_main_game == True:
        show screen main_game(location1)

    if i_show_intro == True:
        char1.talk "Sure, if you think you can handle the sight! *winks*"

    label action_pose_butt_after_love_check:
    $ char1.execute_special_action(location1, "B")
    if i_show_intro == True:
        pl "I'm pretty sure I can! *grinning*"
    $ location_detail = "intimate"
    $ g_intimate_char = char1
    $ l_x_pos = 800 + renpy.random.randint(-50,50)
    $ (l_bg_image,l_bg_zoom) = get_location_background_image_and_zoom(location, daytime)
    $ l_flip = renpy.random.choice([True,False])
    show screen intimacy2(l_image_name, l_bg_image, l_flip, l_x_pos, l_zoom, l_bg_zoom, l_main_zoom, i_char=char1)
    with i_transition

    pause 0.4
    "You eye her incredible butt for a moment..."
    pause 1.0
    char1.talk "Is that all? You don't want to take a closer look?"
    "Grinning, you do as she suggests..."
    show screen intimacy2(l_image_name, l_bg_image, l_flip, l_x_pos, l_zoom, l_bg_zoom, l_main_zoom, zoom_in_d, i_char=char1)
    $ player.change_lust(char1.sexiness)
    $ renpy.pause(3.0,hard=True)
    pl "Wow! I love your perfect butt!"
    if char1.get_mood() == "horny" and renpy.loadable(l_image_name_horny):
        pause 0.5
        char1.talk "I'm not done yet. *giggles*"
        "She slowly exposes parts of her perfect butt."
        show screen intimacy2(l_image_name_horny, l_bg_image, l_flip, l_x_pos, l_zoom, l_bg_zoom, l_main_zoom, zoom_in_d, i_char=char1)
        with dissolve
        $ player.change_lust(char1.sexiness)
        pause 0.7
        pl "Holy shit! Yeah, that's even better. *grinning*"
        $ renpy.pause(1.2,hard=True)
    char1.talk "I think you've stared long enough now! *giggles*"
    "You're a bit disappointed that the show's over already."
    if char1.get_mood() == "horny" and renpy.loadable(l_image_name_horny):
        "Too bad she covers her lovely butt again."
    show screen intimacy2(l_image_name, l_bg_image, l_flip, l_x_pos, l_zoom, l_bg_zoom, l_main_zoom, i_char=char1)
    with dissolve
    pause 0.7
    char1.talk "Hey, don't give me that look!"
    char1.talk "I'm sure you'll have plenty of opportunities to stare at my butt some more! *smiles*"
    pause 0.4
    "With a smirk on her face, she turns around again."
    $ char1.change_lust(4)

    hide screen intimacy2
    if auto_succeed == True:
        hide screen main_game
    $ location_detail = ""
    $ g_intimate_char = no_char
    with dissolve
    call actions_used (i_actions_used_add) from _call_actions_used_71
    $ char1.add_pl_interaction("tease_ass")
    $ char1.add_action_cooldown("action_pose_butt", 4, "I've just posed my butt! Give me a break.")
    return "intimate_pose_butt"





label action_pose_butt_simple(char1, location1, i_image_detail=""):
    $ l_zoom = 0.3334

    show screen main_game(location1)
    if location1 in gl_locations_swimwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_pose_butt" + unicode(i_image_detail) + ".webp"
    elif location1 in gl_locations_nightwear:
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_pose_butt" + unicode(i_image_detail) + ".webp"
    elif location1 == "restaurant":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_pose_butt" + unicode(i_image_detail) + ".webp"
    elif location1 == "reception":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_pose_butt" + unicode(i_image_detail) + ".webp"
    elif location1 == "doctor":
        $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + "_pose_butt" + unicode(i_image_detail) + ".webp"

    if renpy.loadable(l_image_name):
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.6667
        elif l_x_size >= 1000:
            $ l_zoom = 0.3334

    $ char1.execute_special_action(location1, "B")
    $ location_detail = "intimate"
    $ l_x_pos = 800 + renpy.random.randint(-50,50)
    $ (l_bg_image,l_bg_zoom) = get_location_background_image_and_zoom(location, daytime)
    $ l_flip = renpy.random.choice([True,False])
    hide screen closeup
    show screen intimacy2(l_image_name, l_bg_image, l_flip, l_x_pos, l_zoom, l_bg_zoom, 0.5, i_char=char1)
    with dissolve
    return "nothing"





label action_flash_breasts_simple(char1, location1, i_show_end_text=True):
    if location1 <> "restaurant_table":
        if location1 in gl_locations_swimwear:
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_flash_breasts.webp"
        elif location1 in gl_locations_nightwear:
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_flash_breasts.webp"
        elif location1 == "restaurant":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_flash_breasts.webp"
        elif location1 == "reception":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_flash_breasts.webp"
        elif location1 == "doctor":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_flash_breasts.webp"

        if not renpy.loadable(l_image_name):
            return False

        $ l_zoom = 1.0
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_x_size > 750 and l_x_size < 1000:
            $ l_zoom = 0.667
        elif l_x_size >= 1000:
            $ l_zoom = 0.5

    char1.talk "And you cannot even really see them..."
    char1.talk "...but I think I know what to do about that. *smirks*"
    "She slowly exposes her tits..."

    if location1 <> "restaurant_table":
        hide screen closeup
        $ location_detail = "intimate"
        $ g_intimate_char = char1
        show screen main_game(location1)

        $ l_x_pos = 270 + renpy.random.randint(30,80)
        if location1 == "nightbar" and char1.id == jobs.bartender.id:
            show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        elif location1 == "restaurant":
            show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        elif location1 == "reception":
            show screen intimacy(l_image_name, "", i_zoom = l_zoom)
        elif location1 == "doctor":
            show screen intimacy(l_image_name, "locations/loc_doctor_main_overlay.webp", False, l_x_pos, l_zoom, 0.5)
        elif True:
            show screen intimacy(l_image_name, "", False, l_x_pos, l_zoom)
    elif True:
        if char1 == l_char1:
            $ l_images=["flash_breasts",1,1]
        elif char1 == l_char2:
            $ l_images=[1,"flash_breasts",1]
        elif char1 == l_char3:
            $ l_images=[1,1,"flash_breasts"]
        call scene_restaurant_table_image (l_images, i_use_current_zoom_align=True) from _call_scene_restaurant_table_image_7

    pause 1.0
    $ l_breast_size_text = char1.get_breast_size_text()

    char1.talk "Here are my [l_breast_size_text]. Just for you! *smiles*"
    $ char1.change_lust(10)
    pause 1.0
    char1.talk "Don't look at me like you didn't want to see them... *smirks*"
    $ char1.add_pl_interaction("topless")
    if i_show_end_text == True:
        char1.talk "I probably better put them back in, before you get a heart attack. *giggles*"
        if location1 <> "restaurant_table":
            $ location_detail = ""
            hide screen intimacy
        elif True:
            call scene_restaurant_table_image ([1,1,1], i_use_current_zoom_align=True) from _call_scene_restaurant_table_image_8
    $ g_intimate_char = no_char
    $ char1.add_pl_interaction("topless")
    $ char1.add_action_cooldown("action_flash_breasts", 4, "I've just shown you my breasts not long ago!")
    return True




label action_closeup(char1, location1, i_hide_screen=True, i_show_text=True, i_emotion=""):
    if i_emotion == "":
        $ l_emotion = char1.get_mood()
    elif True:
        $ l_emotion = i_emotion
    $ l_location = location1

    if l_emotion == "walk":
        $ l_image_name = char1.get_walk_image(location)
    elif True:
        if l_location == "reception" and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar"):
            $ l_location = "restaurant"
        if l_location in gl_locations_swimwear:
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_" + l_emotion + ".webp"
            if not renpy.loadable(l_image_name):
                $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_swim" + unicode(char1.swimwear) + "_base.webp"
        elif l_location in gl_locations_nightwear:
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_" + l_emotion + ".webp"
            if not renpy.loadable(l_image_name):
                $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.nightwear) + "_base.webp"
        elif l_location == "restaurant":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_" + l_emotion + ".webp"
            if not renpy.loadable(l_image_name):
                $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_night" + unicode(char1.dinerwear) + "_base.webp"
        elif l_location == "reception":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_reception" + unicode(char1.receptionwear) + "_base2.webp"
        elif l_location == "doctor":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_" + l_emotion + ".webp"
            if not renpy.loadable(l_image_name):
                $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_doctor" + unicode(char1.doctorwear) + "_base.webp"
        elif l_location == "massage_wait":
            $ l_image_name = "characters/" + char1.fname.lower() + "/" + char1.fname + "_massage0_base.webp"

    if l_emotion == "walk":
        $ l_zoom = char1.get_walk_image_zoom(l_image_name)
    elif True:
        $ l_zoom = 2.0
        $ l_y_pos = 0
        $ l_x_size,l_y_size = renpy.image_size(l_image_name)
        if l_y_size >= 1600:
            $ l_zoom = 0.667
        elif l_y_size >= 1200:
            $ l_zoom = 1.0
        elif l_y_size > 900:
            $ l_zoom = 1.0

    if l_emotion == "walk":
        $ l_y_pos = 0
    elif True:
        if char1.id == yvette.id:
            $ l_y_pos -= 150
        elif char1.id == sara.id:
            $ l_y_pos -= 140
        elif char1.height_type == 1:
            $ l_y_pos -= 120
        elif char1.height_type == 2:
            $ l_y_pos -= 60
        elif char1.height_type == 3:
            $ l_y_pos -= 40
        elif char1.height_type == 4:
            $ l_y_pos += 140

        if l_y_size == 2160 or l_y_size == 1440:
            $ l_y_pos -= 200

    $ location_detail = "intimate"
    $ g_intimate_char = char1
    show screen main_game(location1)

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    if location1 == "nightbar" and char1.id == jobs.bartender.id:
        show screen intimacy(l_image_name, "", i_zoom = l_zoom, y_pos = l_y_pos)
    elif location1 == "restaurant":
        show screen closeup(l_image_name, "", i_zoom = l_zoom, y_pos = l_y_pos)
    elif location1 == "reception":
        show screen closeup(l_image_name, "", i_zoom = l_zoom, y_pos = l_y_pos)
    elif location1 == "doctor":
        $ l_x_pos = 100 + renpy.random.randint(30,80)
        show screen closeup(l_image_name, "locations/loc_doctor_main_overlay.webp", l_x_pos, l_zoom, i_zoom2 = 0.5,  y_pos = l_y_pos)
    elif location1 == "massage_wait":
        $ l_x_pos = 200 + renpy.random.randint(30,80)
        show screen closeup(l_image_name, "", l_x_pos, l_zoom, y_pos = l_y_pos)
    elif True:
        show screen closeup(l_image_name, "", l_x_pos, l_zoom, y_pos = l_y_pos)
    with dissolve

    if i_show_text == True:
        char1.talk "Thank you, [char1.playername]."
        char1.talk "That's really sweet!"
    if i_hide_screen == True:
        $ location_detail = ""
        hide screen closeup
        $ g_intimate_char = no_char
    return True





label action_bodyside(char1, location1):
    $ l_walk_image = "nothing"
    if location1 in gl_locations_swimwear or location1 in gl_locations_nightwear:
        $ l_walk_image = char1.get_walk_image(location1)

    if not renpy.loadable(l_walk_image):
        return False

    $ location_detail = "intimate"
    show screen main_game(location1)

    $ l_x_pos = 270 + renpy.random.randint(30,80)
    $ l_zoom = char1.get_walk_image_zoom(l_walk_image)
    show screen bodyside(l_walk_image, "", l_x_pos, l_zoom)

    char1.talk "How do you like the side view, [char1.playername]."
    pl "You're stunning!"
    pause 0.6
    char1.talk "And you're sweet. *smiles*"
    $ location_detail = ""
    hide screen bodyside
    return True





label action_sit(char1, location1):
    if location1 <> "restaurant":
        return False

    $ l_counter = 0
    $ l_girls_at_table = []
    $ l_overlay = []
    $ l_overlay_main = []
    $ l_table = "0"
    $ l_char1 = no_char
    $ l_char1_index = 0
    $ l_char2 = no_char
    $ l_char2_index = 1
    $ l_char3 = no_char
    $ l_char2_index = 2
    $ l_char_focus = no_char
    $ l_adjust_y = 0.0
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    $ l_overlay_main.append("binoculars/binoculars_empty.webp")
    if get_its_raining(True) == True:
        $ l_base_image_main = "locations/loc_restaurant_main_rain.webp"
    elif True:
        $ l_base_image_main = "locations/loc_restaurant_main.webp"
    $ l_zoom = 0.3334
    $ l_align_xy = (0.5, 0.5)
    $ ll_tint = get_daytime_outdoor_tint(daytime, 0.7, i_location=location1)
    $ l_table = char1.get_restaurant_table()
    $ l_girls_at_table = char1.get_girls_at_restaurant_table()
    $ l_base_image = "locations/loc_restaurant_table" + l_table + "_main.webp"
    call create_restaurant_table_chars () from _call_create_restaurant_table_chars_10

    pl "Would you mind if I join you at your table, [char1.fname]?"
    if get_its_raining(True) == True:
        $ l_image_main = Composite((3840,2160), (0,0), im.MatrixColor(l_base_image_main, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])), (0,0), "rain1_restaurant_main", (0,0), l_overlay_main[0], (0,0), l_overlay_main[1], (0,0), l_overlay_main[2], (0,0), l_overlay_main[3], (0,0), l_overlay_main[4], (0,0), l_overlay_main[5], (0,0), l_overlay_main[6], (0,0), l_overlay_main[7], (0,0), l_overlay_main[8])
    elif True:
        $ l_image_main = Composite((3840,2160), (0,0), im.MatrixColor(l_base_image_main, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])), (0,0), l_overlay_main[0], (0,0), l_overlay_main[1], (0,0), l_overlay_main[2], (0,0), l_overlay_main[3], (0,0), l_overlay_main[4], (0,0), l_overlay_main[5], (0,0), l_overlay_main[6], (0,0), l_overlay_main[7], (0,0), l_overlay_main[8])
    scene expression l_image_main:
        zoom 0.3334
    $ location_detail = "sit"
    $ start_scene()
    $ menu_active = True
    with Dissolve(0.3)
    char1.talk "Quite the opposite, [char1.playername]."
    if get_its_raining(True) == True:
        if l_table == "1":
            $ l_image_table = Composite((3840,2160), (0,0), l_base_image, (0,0), "rain1_restaurant_table1", (0,0), l_overlay[0], (0,0), l_overlay[1], (0,0), l_overlay[2])
        elif l_table == "2":
            $ l_image_table = Composite((3840,2160), (0,0), l_base_image, (0,0), "rain1_restaurant_table2", (0,0), l_overlay[0], (0,0), l_overlay[1], (0,0), l_overlay[2])
        elif l_table == "3":
            $ l_image_table = Composite((3840,2160), (0,0), l_base_image, (0,0), "rain1_restaurant_table3", (0,0), l_overlay[0], (0,0), l_overlay[1], (0,0), l_overlay[2])
    elif True:
        $ l_image_table = Composite((3840,2160), (0,0), l_base_image, (0,0), l_overlay[0], (0,0), l_overlay[1], (0,0), l_overlay[2])
    if len(l_girls_at_table) > 1:
        char1.talk "Please join us and have a seat."
    elif True:
        char1.talk "Please join me and have a seat."
    pause 0.4
    pl "Thanks."

    if persistent.walk_animations <> False:
        if l_table == "1":
            scene expression l_image_main:
                subpixel True zoom 0.3334 align (0.9,0.45)
                ease 2.6 zoom 0.7
            $ renpy.pause(2.9,hard=True)
        elif l_table == "2":
            scene expression l_image_main:
                subpixel True zoom 0.3334 align (0.05,0.4)
                ease 2.6 zoom 0.75
            $ renpy.pause(2.9,hard=True)
        elif l_table == "3":
            scene expression l_image_main:
                subpixel True zoom 0.3334 align (0.58,0.3)
                ease 2.8 zoom 0.8
            $ renpy.pause(3.1,hard=True)

    if len(l_girls_at_table) == 1:
        if l_char1 <> no_char:
            $ l_char_focus = l_char1
            call scene_restaurant_table_image ([1,1,1], i_transition=fade, i_focus_on=1) from _call_scene_restaurant_table_image_9

        elif l_char2 <> no_char:
            $ l_char_focus = l_char2
            call scene_restaurant_table_image ([1,1,1], i_transition=fade, i_focus_on=2) from _call_scene_restaurant_table_image_10
        elif True:

            $ l_char_focus = l_char3
            call scene_restaurant_table_image ([1,1,1], i_transition=fade, i_focus_on=3) from _call_scene_restaurant_table_image_11
    elif True:
        call scene_restaurant_table_image ([1,1,1], i_transition=fade) from _call_scene_restaurant_table_image_12

    $ l_zoom_init = l_zoom
    $ l_align_xy_init = l_align_xy

    if len(l_girls_at_table) > 1:
        pl "Hi girls!"
    elif True:
        pl "Hi [char1.fname]."

    if l_char1 <> no_char:
        pause 0.4
        l_char1.talk "Hey!"
    if l_char2 <> no_char:
        pause 0.4
        l_char2.talk "Hello [l_char2.playername]!"
    if l_char3 <> no_char:
        pause 0.4
        l_char3.talk "Hi, how are things?"
        pl "Great, thank you."
    pause 0.4


    if len(l_girls_at_table) == 3:
        $ chars_list = l_girls_at_table[:]
        if amy in chars_list and amy.get_action_allowed("restaurant_story_bus_amy") == True:
            if amy.get_event_seen_times("restaurant_story_bus") == 0 and renpy.random.randint(1,100) <= 75:
                call restaurant_story_bus_amy (chars_list) from _call_restaurant_story_bus_amy
                jump action_sit_check_actions_used
            elif (amy.get_event_seen_times("restaurant_story_bus") == 1 or amy.get_event_seen_times("restaurant_story_bus") == 2) and renpy.random.randint(1,100) <= 50:
                call restaurant_story_bus_amy (chars_list) from _call_restaurant_story_bus_amy_1
                jump action_sit_check_actions_used
            elif renpy.random.randint(1,100) <= 25:
                call restaurant_story_bus_amy (chars_list) from _call_restaurant_story_bus_amy_2
                jump action_sit_check_actions_used

    label action_sit_loop:
    call screen restaurant_table_menu_new_ui()
    if _return == "Leave_table":
        pl "It was nice talking with you."
        pl "See you later."
        if l_char1 <> no_char:
            pause 0.4
            l_char1.talk "I certainly hope so. *winks*."
        if l_char2 <> no_char:
            pause 0.4
            l_char2.talk "See you later."
        if l_char3 <> no_char:
            pause 0.4
            l_char3.talk "Bye [l_char3.playername]."
        "You head back to the main area of the restaurant."
        $ l_char_focus = no_char
        jump action_sit_end

    elif _return == "Focus_stop":
        $ l_char_focus = no_char
        call scene_restaurant_table_image ([1,1,1]) from _call_scene_restaurant_table_image_13

    elif _return == "Focus_on_left":
        $ l_char_focus = l_char1
        if l_char1.id == ivy.id:
            scene expression l_image_table:
                subpixel True zoom l_zoom align (l_align_xy[0],l_align_xy[1])
                ease 1.7 zoom 0.6 align (0.0,0.4)
            $ renpy.pause(1.9,hard=True)
            $ l_zoom = 0.6
            $ l_align_xy = (0.0,0.4)
        elif True:
            scene expression l_image_table:
                subpixel True zoom l_zoom align (l_align_xy[0],l_align_xy[1])
                ease 1.7 zoom 0.65 align (0.0,0.6)
            $ renpy.pause(1.9,hard=True)
            $ l_zoom = 0.65
            $ l_align_xy = (0.0,0.6)

    elif _return == "Focus_on_middle":
        $ l_char_focus = l_char2
        scene expression l_image_table:
            subpixel True zoom l_zoom align l_align_xy
            ease 2.0 zoom 0.85 align (0.45,0.5)
        $ renpy.pause(2.2,hard=True)
        $ l_zoom = 0.85
        $ l_align_xy = (0.45,0.5)

    elif _return == "Focus_on_right":
        $ l_char_focus = l_char3
        scene expression l_image_table:
            subpixel True zoom l_zoom align l_align_xy
            ease 1.7 zoom 0.62 align (1.0,0.65)
        $ renpy.pause(1.9,hard=True)
        $ l_zoom = 0.62
        $ l_align_xy = (1.0,0.65)

    if unicode( _return).startswith("Focus_on"):
        $ l_random = renpy.random.randint(1,5)
        if l_random == 1:
            pl "You look especially beautiful today, [l_char_focus.fname]."
            l_char_focus.talk "Thank you. *smiles*"
        elif l_random == 2:
            l_char_focus.talk "Are you staring at me, [l_char_focus.playername]?"
            pl "Ummm..."
            l_char_focus.talk "No worries, I think I like it. *smiling*"
        elif l_random == 3:
            l_char_focus.talk "I guess I've all of your attention now."
            l_char_focus.talk "Do you like what I have on?"
            pl "Yes, very much. *smiling*"
        elif l_random == 4:
            pl "You always take my breath away, [l_char_focus.fname]."
            char1.talk "Now that's cute, thanks."
        elif l_random == 5:
            l_char_focus.talk "See anything you like?"
            pl "Yes, definitely. *smiling*"
            l_char_focus.talk "Okay. *winks*"

    label action_sit_check_actions_used:
    if actions_used > 0:
        $ actions_left -= actions_used
        $ actions_used = 0
        $ cur_time = cl_utility().convert_ap_to_time(actions_left)
        call create_list_of_chars_display () from _call_create_list_of_chars_display_17
        if (l_char1 <> no_char and l_char1 not in char1.get_girls_at_restaurant_table()) or (l_char2 <> no_char and l_char2 not in char1.get_girls_at_restaurant_table()) or (l_char3 <> no_char and l_char3 not in char1.get_girls_at_restaurant_table()):
            call scene_restaurant_table_image (i_transition=dissolve, i_recreate_image=False) from _call_scene_restaurant_table_image_14

        if l_char1.id <> no_char.id and l_char1 not in char1.get_girls_at_restaurant_table():
            l_char1.talk "Okay, I've eaten all I can right now. *chuckles*"
            l_char1.talk "I better be gone from the restaurant."
            pause 0.4
            l_char1.talk "Bye."
            pl "See you, [l_char1.fname]."
            if l_char_focus == l_char1:
                $ l_char_focus = no_char
        if l_char2.id <> no_char.id and l_char2 not in char1.get_girls_at_restaurant_table():
            l_char2.talk "Time for me to head out. See you later."
            pl "Bye, [l_char2.fname]."
            if l_char_focus == l_char2:
                $ l_char_focus = no_char
        if l_char3.id <> no_char.id and l_char3 not in char1.get_girls_at_restaurant_table():
            l_char3.talk "Enjoy your meal, I'll be heading out."
            l_char3.talk "We'll see each other later."
            pl "Certainly, [l_char3.fname]. Bye."
            if l_char_focus == l_char3:
                $ l_char_focus = no_char
        $ l_char1_old = l_char1
        $ l_char2_old = l_char2
        $ l_char3_old = l_char3
        $ l_girls_at_table = char1.get_girls_at_restaurant_table()
        call create_restaurant_table_chars () from _call_create_restaurant_table_chars_11
        if l_char1_old <> l_char1 or l_char2_old <> l_char2 or l_char3_old <> l_char3:
            $ l_char_focus = no_char
            call scene_restaurant_table_image (i_transition=fade) from _call_scene_restaurant_table_image_15
        if l_char1_old <> l_char1 and l_char1 <> no_char:
            l_char1.talk "Hey [l_char1.playername], I hope you don't mind that I join you at your table."
            pl "Not at all. *smiling*"
        if l_char2_old <> l_char2 and l_char2 <> no_char:
            l_char2.talk "Hello [l_char1.playername], how are you doing?"
            pl "I'm fine, thanks for asking."
        if l_char3_old <> l_char3 and l_char3 <> no_char:
            pl "Hi [l_char3.fname], nice to have you here."
            l_char3.talk "Hey [l_char3.playername]."
            l_char3.talk "I'm super hungry. *grins*"
        if l_char1.id == no_char.id and l_char2.id == no_char.id and l_char3.id == no_char.id:
            "Since you're alone at the table, you head back to the main restaurant area."
            jump action_sit_end

    jump action_sit_loop

    label action_sit_end:
    $ selected_char = no_char
    $ l_char_focus = no_char
    $ location_detail = ""
    $ menu_active = False
    $ stop_scene()
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
