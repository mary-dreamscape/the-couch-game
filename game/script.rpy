# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elwyn", color="#FF0000")
define m = Character('[povname]', color="#000FFF")
define n = Character("Natalie", color="#000FFF")

# The game starts here.

label start:

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
             povname = "Hooman"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street newspaper
    play music "audio/bensound-onceagain.mp3" fadeout 1.0 fadein 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    "Another kid went missing? Didn't some guy go missing too yesterday? And the day before?"

    "Man, the world is slowly going bonkers."

    scene bg street

    show elwyn smile

    e "Hey, hey you there! I see you’re reading… about that news article."

    "I just nodded back at her, looking wary."

    e "Yeah… That’s actually about me. Well, my daughter. What’s your name?"

    "She looks so cheerful. But looking back at the picture of the little girl's family... Yeah, definitely her."

    m "[povname]. Nice to meet you."

    e "Great. Hi [povname]! I'm... well, Elwyn, which you probably already know from reading that."

    show elwyn happy with dissolve

    "Elwyn giggles a little bit, but I can see her feeling nervous. She must be trying to hide her sadness."

    show elwyn smile with dissolve

    e "You look like you’re really smart, so I thought… maybe you could help me out? Try to find my daughter for me? What do you think? Would you like to help out?"

menu:

    "Yes.":
        jump yes

    "No.":
        jump no

label no:
    play music "audio/bensound-betterdays.mp3" fadeout 1.0 fadein 1.0

    m "Ah, sorry. I don't think I can do that."

    show elwyn sad with dissolve

    "Elwyn's face falls. I feel bad, but I don't want to get involved in this..."

    e "Well, it's no problem! I guess I will see you around."

    scene dark with dissolve

    show text "Credits" with dissolve

    pause(2.0)

    show text "Character Designed and Written by\n\nMaryam" with dissolve

    pause(2.0)

    show text "Background Images: Free Wallpaper Access (https://wallpaperaccess.com/anime-store)" with dissolve

    pause(2.0)

    show text "Music: Free Music by Ben Sounds and Pixabay"

    pause(4.0)

    "Game End."

    return

label yes:

    m "Yeah, sure. I mean, I don't know how much help I can be but I will try my best."

    show elwyn happy with dissolve

    "Elwyn's face lights up. It makes me happy to see it. Maybe we might be able to find her daughter."

    e "I knew you are an amazing person, [povname]! I can just tell!"

    show elwyn smile with dissolve

    e "Well, I guess I should let you know what had happened first, so you have more context."

    jump flashback

label flashback:

    scene bg street past with dissolve
    play music "audio/bensound-adventure.mp3" fadeout 1.0 fadein 1.0

    show natalie happy at right

    n "Mom, mom! Look! That couch looks really pretty!"

    hide natalie happy
    scene garage sale

    "Couch? Wha— Oh, a garage sale. Figures, Natalie always loves garage sales."

    show elwyn surprised at left

    e "You want that couch?"

    hide elwyn surprised
    scene teddy bear couch

    "What type of couch is made fully from teddy bears? And... ugh, does this mean I would have to clean the entire couch first? Imagine the number of bugs in it!"

    "But Natalie nods excitedly, trying to give her signature puppy eyes."

    scene garage sale
    show natalie happy at right

    n "Please, mom? Pretty please? It's really cute and I promise I won't ask anything more of you after this!"

    hide natalie happy

    "She has been a pain for the past few days, throwing tantrums. Maybe this will make her better... Lesser headache for me, I guess if she's busy with it."

    "And only 25 dollars? For a couch? What a steal!"

    show elwyn smile at left

    e "Fine, we'll get it..."

    jump incident

label incident:

    hide elwyn smile
    scene living room
    play music "audio/your-own-personal-hell-8685.mp3" fadeout 1.0 fadein 1.0

    "Everything was great. Of course, it was. Until Natalie started throwing a tantrum again. It was horrible. She got bored of the couch."

    show elwyn angry at left

    e "WILL YOU PLEASE SHUT UP?"

    show natalie angry at right

    n "NO! All I want is macaroni and cheese. Mac and cheese, mac and cheese, mac and cheese!"

    hide elwyn angry
    hide natalie angry

    "I was boiling with rage at that point. God... If I knew what would happen after that... If I knew that was our last interaction..."

    show elwyn angry at left

    e "You wanted spaghetti! I made your spaghetti and it took me so long, and now you want macaroni and cheese?!"

    show natalie angry at right

    n "You're a horrible mother! A horrible mother who would not give me mac and cheese!"

    e "YEAH WELL, YOU'RE A HORRIBLE DAUGHTER AND I WISH I NEVER HAD YOU."

    hide natalie angry
    hide elwyn angry

    "And Natalie ran to the couch and I could hear her crying on it. That stupid... ugly couch that I wish I had never bought."

    "And I went back to my room. When I came out back an hour later..."

    jump gone

label gone:

    scene living room night

    "She was gone. Only that stupid couch was there. Natalie was gone."

    jump present

label present:

    scene living room
    play music "audio/bensound-betterdays.mp3" fadeout 1.0 fadein 1.0
    show elwyn sad

    e "So you see... They couldn't find her. Not the police officers, not the forensics. They dusted the entire house and it was like... she disappeared into thin air."

    show elwyn cry with dissolve

    "A small sob came out of Elwyn and I could feel myself tearing up. What a poor woman."

    "I look around and there it was... the couch. Man, it is ugly, like what Elwyn had said."

    m "Is this the teddy bear couch?"

    "I ask even though I already knew the answer. But I did not know what else to say. I'm not good at comforting people..."

    show elwyn surprised with dissolve

    "Elwyn's face clears up and looks towards it, then at me, looking like she had just realised that I'm there."

    e "OH, yes! Why don't you sit down? I'll grab some tea... or coffee if you would prefer."

menu:

    "Sit down.":
        jump sit

    "Don't sit down.":
        jump stand

label sit:

    scene living room sit

    m "Yeah. Yeah, alright. In the meantime, maybe I can try to look at your house from the perspective of an outsider."

    show elwyn smile

    "Elwyn lets out a wide smile as I sit down. She must have been relieved to have someone helping her. She nods back at me."

    e "Tea? You look like a tea person."

    show elwyn happy with dissolve

    "She chuckles and I can't help but smile back. I'm actually a coffee person, but whatever makes her happy."

    m "Tea's great!"

    "Elwyn gives me another smile before disappearing into the kitchen."

    hide elwyn happy

    "I decided to look around. It's a pretty nice house, I guess. Homey. Brighter than the one I live in."

    scene couch

    "My hand strays over the texture of the couch, my attention caught by it. It feels weird. Whoever created this couch did not think about the comfort level. It is like sitting on a pile of teddy bears and not in a good way."

    "I look at each of the teddy bears one by one. At a closer look, they actually seem... creepy. For some reason, it's like they are just... staring at me. I shudder, but I cannot seem to pull my attention away."

    "And they look so... worn and old. Gross, how long have these teddy bears been in here? How would one even clean this couch?"

    "But wait... This one... This one looks brand new."

    m "Elwyn? Elwyn, did you know that this teddy bear is new?"

    "Silence."

    scene living room sit

    "For some reason, my heart starts pounding. Something is wrong. And Elwyn has been gone for a long time. Should I check up on her?"

    "My gut is screaming at me to get out of the house. I almost stand up, but then Elwyn appears."

    show elwyn smile
    play music "audio/your-own-personal-hell-8685.mp3" fadeout 1.0 fadein 1.0

    m "Elwyn! Oh God, you scared me. Did you... Where's the tea?"

    "I frown but she just stands there smiling. Weird."

    e "She was so noisy."

    "Huh?"

    m "Who?"

    e "Natalie. She was so noisy and I could not take it anymore..."

    "I swallow hard against the lump in my throat. I need to get out of there. NOW."

    "I started to stand but suddenly something grips my shoulders. No... Something seems to be pushing me back against the couch."

    m "El— Wha— What's going... What is this?!"

    scene living room sit dark
    show elwyn smile
    with dissolve

    "I can feel myself panicking but the couch seems to... envelope itself around me."

    show elwyn surprised with dissolve

    e "I saw... I saw her being swallowed up and I just... I can't take it anymore. She was better off... being quiet forever. But then... it wanted more."

    e "It demands more... I'm sorry, I have no choice... There are only so many neighbours I can lure into my house before people start getting suspicious."

    e "I'm sorry..."

    scene dark with dissolve

    show text "Credits" with dissolve

    pause(2.0)

    show text "Character Designed and Written by\n\nMaryam" with dissolve

    pause(2.0)

    show text "Background Images: Free Wallpaper Access (https://wallpaperaccess.com/anime-store)" with dissolve

    pause(2.0)

    show text "Music: Free Music by Ben Sounds and Pixabay"

    pause(4.0)

    "THE END."

    return

label stand:

    scene living room

    hide elwyn surprised

    "I look towards the couch."

    m "Um... I think I will stand. That couch looks really creepy, don't you think?"

    "Silence."

    show living room sit
    show elwyn angry
    with dissolve

    play music "audio/your-own-personal-hell-8685.mp3" fadeout 1.0 fadein 1.0

    "I turn back towards Elwyn and she seems to be glaring at me."

    m "Elwyn...?"

    e "Sit."

    m "What?"

    e "I SAID SIT!"

    "I almost fall back when she screams. What is going on? She does not look like the sad woman I saw just now. Instead, she's just... angry. Why?"

    "My gut says to get out. Start running."

    m "Look, you're clearly still agitated over everything. I think... I think I should give you some space, okay?"

    show elwyn panicked with dissolve

    "Her face turns into a panicked expression."

    e "NO! You have to sit!"

    "I frown, confused."

    m "I'm just going to go—"

    show elwyn angry:
        parallel:
            ease .5 zoom 2.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.3 #or whatever fit.

    "I only had a split second before she runs into me, trying to push me back onto the couch."

menu:

    "Fall back onto couch.":
        jump sitdown

    "Push Elwyn back.":
        menu:
            "Fall back onto couch":
                jump sitdown
            "Push Elwyn back more.":
                menu:
                    "Fall back onto couch.":
                        jump sitdown
                    "PUSH ELWYN BACK REALLY HARD.":
                        jump fight

label sitdown:

    scene living room sit
    show elwyn panicked

    "I let myself fall back onto the couch. I don't understand. Did she really want me to help her that badly?"

    m "Okay, okay. I'm seated. Now, will you please calm down?"

    show elwyn sad with dissolve

    "Elwyn's eyes seem wide and she is breathing hard. Her voice is soft that I almost could not catch it."

    e "I tried my best..."

    "Huh?"

    e "I'm a good mother... Okay?"

    m "I didn't say that you are. And I'm sorry if I implied it."

    "But ignored me, her eyes dazed, lost in her own thoughts."

    e "I'm a good mother... But I have my limits. And I just... I had enough."

    "My heart starts to pound and I tried to stand up. But it feels like... something is pushing me back, further into the couch."

    show elwyn smile with dissolve

    "Elwyn smiles suddenly."

    e "I saw her getting swallowed up, but I didn't care. She was so noisy and I just started to wish she was gone."

    e "It was the perfect solution."

    scene living room sit dark
    show elwyn smile
    with dissolve

    "The... the couch. The couch seems like it's taking me... into it. I try to struggle and my vision is being blocked but I can see Elwyn just... looking on. I try to scream for help."

    e "But the couch... wants more. It demands more and soon, people are going to ask where my neighbours went. They might suspect me... And you look like you're not from around here."

    show elwyn happy with dissolve

    "Elwyn chuckles."

    e "I'm sorry, but this is the way it should be. Goodbye, [povname]."

    scene dark with dissolve

    show text "Credits" with dissolve

    pause(2.0)

    show text "Character Designed and Written by\n\nMaryam" with dissolve

    pause(2.0)

    show text "Background Images: Free Wallpaper Access (https://wallpaperaccess.com/anime-store)" with dissolve

    pause(2.0)

    show text "Music: Free Music by Ben Sounds and Pixabay"

    pause(4.0)

    "THE END."

    return

label fight:

    scene living room elwyn eaten
    hide elwyn panicked

    "I manage to swerve at the last minute and push her back onto the couch."

    e "NO!"

    "Elwyn starts to shriek in panic suddenly and I take a few steps back. She seems to be half way in the couch."

    m "What is... what is going on?"

    "She tries to stand but she fails and screams."

    e "NO, LET ME GO! IT'S SUPPOSED TO BE THEM, NOT ME. I BROUGHT FOR YOU SOMEONE!"

    "I take a few steps back and my heart almost drops as I see the most horrifying thing ever. The couch is slowly swallowing her up."

    scene living room elwyn eaten 2 with dissolve

    "I could not move, I could only stare as it swallows her up. I could only take in her screams as they slowly disappear into the couch."

    scene living room 2 with dissolve
    show living room 2 with dissolve:
        xpos 0.60 ypos 1.10 xanchor 0.5 yanchor 1.0 zoom 3.0

    "My eyes flitter over to the side of the couch suddenly and let out a small cry... as a teddy bear appeared, its shade the same skin tone as Elwyn."

    scene house with dissolve

    "I run. I turn around and run out of the house. And as I run, I thought I could hear low laughter coming from the couch."

    scene dark with dissolve

    show text "Credits" with dissolve

    pause(2.0)

    show text "Character Designed and Written by\n\nMaryam" with dissolve

    pause(2.0)

    show text "Background Images: Free Wallpaper Access (https://wallpaperaccess.com/anime-store)" with dissolve

    pause(2.0)

    show text "Music: Free Music by Ben Sounds and Pixabay"

    pause(4.0)

    "THE END."

    return
