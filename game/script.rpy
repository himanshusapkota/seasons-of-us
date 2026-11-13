# Definition of the characters

define a = Character("Aarav", color="#5DADE2")
define s = Character("Sia", color="#FF69B4")
define r = Character("Rohan", color="#58D68D")


# Importing the background images

image bg school = im.Scale("images/backgrounds/school.jpg", 1920, 1080)
image bg classroom = im.Scale("images/backgrounds/classroom.jpg", 1920, 1080)
image bg examhall = im.Scale("images/backgrounds/examhall.jpg", 1920, 1080)
image bg schoolyard = im.Scale("images/backgrounds/schoolyard.jpg", 1920, 1080)
image bg hallway = im.Scale("images/backgrounds/school_hallway_night.jpg", 1920, 1080)
image bg sunset = im.Scale("images/backgrounds/sunset.jpg", 1920, 1080)
image bg bedroom = im.Scale("images/backgrounds/bedroom.jpg", 1920, 1080)


# Importing the character images of AARAV

image aarav angry = "images/aarav/aarav_school_angry.png"
image aarav angry talk = "images/aarav/aarav_school_angrytalk.png"
image aarav clueless = "images/aarav/aarav_school_clueless.png"
image aarav happy = "images/aarav/aarav_school_happy.png"
image aarav happy blush = "images/aarav/aarav_school_happyblush.png"
image aarav huh = "images/aarav/aarav_school_huh.png"
image aarav normal = "images/aarav/aarav_school_normal.png"
image aarav normal blush = "images/aarav/aarav_school_normalblush.png"
image aarav tears = "images/aarav/aarav_school_tears.png"
image aarav upset = "images/aarav/aarav_school_upset.png"
image aarav annoyed = "images/aarav/aarav_school_angry.png"


# Importing the character images of SIA

image sia angry = "images/sia/sia angry.png"
image sia annoyed = "images/sia/sia annoyed.png"
image sia blush angry = "images/sia/sia blush_angry.png"
image sia blushing cry = "images/sia/sia blushing_cry.png"
image sia confused = "images/sia/sia confused.png"
image sia dark distant = "images/sia/sia dark_distant.png"
image sia dark sad = "images/sia/sia dark_sad.png"
image sia mischievous = "images/sia/sia mischievous.png"
image sia norm smile = "images/sia/sia norm_smile.png"
image sia oh = "images/sia/sia oh.png"
image sia playful smile = "images/sia/sia playful_smile.png"
image sia sad blush = "images/sia/sia sad_blush.png"


# Importing the character images of ROHAN

image rohan evil = "images/rohan/rohan evil.png"
image rohan fear = "images/rohan/rohan fear.png"
image rohan happy = "images/rohan/rohan happy.png"
image rohan nervous = "images/rohan/rohan nervous.png"
image rohan normal = "images/rohan/rohan normaltalking.png"
image rohan normal talking = "images/rohan/rohan normaltalking.png"


# Basic Position Setting

transform left:
    xalign 0.25
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0


label start:

    scene bg school
    with fade

    pause 1.0

    "Some stories begin with something big."
    "A special day."
    "A big decision."
    "Something that changes everything."

    "But some stories begin normally."
    "Just another school morning."
    "Another classroom."

    # Intro of AARAV

    show aarav normal
    with dissolve

    a "I'm Aarav."
    a "I'm usually quiet around people I don't know."
    a "But once I get comfortable, I can talk way too much."
    a "I like simple things."
    a "Hanging out with friends, studying when I actually feel like it..."
    a "And trying to make the most out of normal school days."

    hide aarav
    with dissolve

    # Intro of SIA

    show sia norm smile
    with dissolve

    s "I am Sia."
    s "I am probably more talkative than Aarav."
    s "I like joking around, annoying my friends, and making boring days a little more interesting."
    s "Sometimes I make decisions without thinking too much."
    s "But I always care about the people close to me."

    hide sia
    with dissolve

    # Intro of ROHAN

    show rohan normal
    with dissolve

    r "I am Rohan."
    r "I joined the school a little later than the others."
    r "I am pretty confident, so making new friends was not really a problem."
    r "I like competition."
    r "And honestly..."
    r "I do not mind getting involved in other people's stories."

    hide rohan
    with dissolve

    scene bg schoolyard

    show aarav normal at left
    show sia norm smile at center
    show rohan normal at right
    with dissolve

    "Three people."
    "Three different personalities."
    "And a lot of moments they haven't experienced yet."

    a "So... this is going to be a normal school year, right?"
    s "Definitely."
    r "You really think so?"
    a "Why wouldn't it be?"
    s "I don't know."
    s "Something tells me things are going to get interesting."

    "And she was right."
    "Before the story begins, choose how you want to play."

    menu:
        "Normal Mode":
            jump normal_mode

        "Cheating Mode":
            jump cheating_mode


label normal_mode:

    scene bg school
    with fade

    "Grade 8."
    "The first day of a new school year."
    "New books."
    "Old teachers. Some might be new too."
    "New classmates."
    "And for Aarav, another year of trying not to get in trouble."

    show aarav normal
    with dissolve

    a "I really should have stayed in bed."

    "Aarav looked around the classroom."
    "Most of the students were already talking with their friends."
    "Some were comparing the timetables."
    "Some were complaining about new teachers."
    "And some toppers were already discussing the homework."

    a "First day and people are already talking about homework."
    a "How am I supposed to fit in with them?"

    scene bg classroom

    show sia playful smile at left
    with dissolve

    show aarav normal blush at right
    with dissolve

    s "Heyy!"
    a "Heyyy!"
    s "Is that seat taken?"
    a "Nahh."
    s "Good!"

    "Sia sat down."

    a "You are new?"
    s "Kind of."
    s "I was in another section last year."
    a "Ohhh."
    s "You are Aarav, right?"
    a "Ahh yep, I am."
    s "I heard you are good at maths."
    a "Who told you that?"
    s "Someone."
    a "That's sus!"
    s "Whyyyy?"
    a "Because I am not."
    s "So you were lying to everyone?"
    a "Apparently."

    show sia norm smile
    with dissolve

    "Sia laughed."
    "Aarav smiled without realizing it."

    "The first few weeks passed quickly."
    "Aarav and Sia started talking more."
    "At first, it was only about school."
    "Then homework."
    "Then teachers."
    "Then friends."
    "Then completely random things."

    show aarav normal blush
    show sia norm smile at right
    with dissolve

    s "What is your favorite subject?"
    a "Computer?"
    s "Really?"
    a "Yeah."
    s "I thought you'd say maths."
    a "Why?"
    s "You look like someone who likes maths."
    a "What does a maths person look like?"
    s "I really don't know."
    a "Exactly."
    s "Okay, fine."
    a "What's yours?"
    s "English."
    a "That makes sense."
    s "Why?"
    a "You talk a lot."
    s "That's not related, Aarav."
    a "Definitely it is."
    s "You are annoying."
    a "You have said that before."
    s "Yeah, I will keep saying this."

    scene bg schoolyard
    with fade

    "During lunch breaks, they often sat together."
    "Sometimes their friends joined them."
    "Sometimes it was just the two of them."

    show aarav happy at left
    show sia mischievous at right
    with dissolve

    s "I bet you can't finish this before me."
    a "Finish what?"
    s "Your food."
    a "That's not a competition."
    s "Everything is a competition."
    a "You are weird."
    s "And you are slow."
    a "Watch me."

    "Aarav started eating a lot faster than before."

    s "Wait, seriously?"
    a "You challenged me."
    s "I didn't think you would actually do this."
    s "Crazy, man!"
    a "Too late!"

    "Sia started laughing."
    "Aarav laughed too."
    "They didn't notice how quickly they were becoming so close."

    scene bg classroom
    with fade

    "One afternoon, Sia stayed behind after class."

    show aarav normal at left
    show sia sad blush at right
    with dissolve

    a "You are still here?"
    s "Yeah."
    a "Everything okay?"
    s "Yeahhh."
    a "You don't look okay today."
    s "I am just tired."
    a "Want to talk?"
    s "Maybeee."

    "Aarav sat beside her."

    s "Sometimes I feel like everyone expects too much."
    a "School?"
    s "School. Parents. Everything."
    a "Yeahhh."
    s "You ever feel like that?"
    a "Sometimes."
    s "What do you do?"
    a "Usually?"
    s "Yeah."
    a "I complain."
    s "That's your solution?"
    a "Actually, it works."

    "Sia laughed silently."

    s "Thanksss."
    a "For what?"
    s "Just listening..."
    a "Anytime."

    scene bg sunset
    with fade

    "That evening, Aarav realised something."
    "He didn't just enjoy talking with Sia."
    "He cared about her."
    "More than he expected."

    show aarav normal blush
    with dissolve

    a "I think I like her."
    "He immediately regretted saying it out loud."
    a "Great."
    a "Now I will be talking to myself."

    scene bg schoolyard
    with fade

    show aarav normal blush at left
    show sia norm smile at right
    with dissolve

    s "You wanted to tell me something?"
    a "Yeah."
    s "What?"
    a "I don't know how to say it."
    s "Just say it."
    a "I like you."

    "Sia became quiet."

    a "You don't have to say anything."
    s "I like you too."
    a "Really?"
    s "Yeah."
    a "Oh."
    s "That's all you have to say?"
    a "I was not prepared for you to say yes."
    s "You are funny."
    a "I am serious."
    s "I know."

    "They both smiled."
    "That was the beginning."

    scene bg school
    with fade

    "Grade 9."
    "A year had passed."
    "Aarav and Sia were still together."
    "They had learned a lot about each other."
    "They also learned that being together didn't mean they would agree on everything."

    show aarav annoyed at left
    show sia annoyed at right
    with dissolve

    s "You forgot again."
    a "I did not forget."
    s "You forgot."
    a "I was busy."
    s "You could have told me."
    a "I know."
    s "Then why didn't you?"
    a "I don't know."

    "They stayed quiet."
    "Neither wanted to continue arguing."

    a "I am sorry."
    s "I am sorry too."
    a "We are okay."
    s "Yes."

    "It wasn't perfect."
    "But they were learning how to fix things."

    scene bg schoolyard
    with fade

    show sia playful smile at right
    show aarav normal at left
    with dissolve

    s "Guess what?"
    a "What?"
    s "I got the highest marks in science."
    a "Seriously?"
    s "Yep."
    a "I thought I was going to beat you."
    s "Your thinking is wrong, Aarav."
    a "Next exam."
    s "Deal."
    a "Yesss."

    "Their competition became one of their favorite things."
    "Neither wanted the other to fail."
    "They simply wanted to push each other."

    scene bg classroom
    with fade

    "Class 10 arrived."
    "Everything suddenly felt more serious."
    "Board exams were getting closer."
    "Teachers gave more homework."
    "Everyone talked about marks."

    show aarav upset at left
    show sia annoyed at right
    with dissolve

    a "I don't understand this chapter."
    s "You haven't even tried."
    a "I did."
    s "For 5 minutes."
    a "I am still trying."
    s "Give me your notebook."
    a "Whyy?"
    s "I will explain it."
    a "You are saving me again."
    s "Someone has to."

    "They studied together almost every day."
    "Sometimes they understood everything."
    "Sometimes they understood nothing."
    "Sometimes they spent 20 minutes talking instead of studying."

    show sia mischievous
    with dissolve

    s "We have been studying for an hour."
    a "We studied for 10 minutes."
    s "The rest was discussion."
    a "About snacks."
    s "Important discussion."
    a "Very important."

    scene bg bedroom
    with fade

    "The night before the exams was different."
    "There were fewer jokes."
    "More books."
    "More pressure."

    show aarav normal at left
    show sia norm smile at right
    with dissolve

    a "Are you still awake?"
    s "Yeah."
    a "You should sleep."
    s "You too."
    a "This time I mean it."
    s "Sure."
    a "Good luck tomorrow."
    s "Good luck."

    scene bg examhall
    show aarav normal at left
    with dissolve

    "The exam day finally arrived."
    "Aarav sat down."
    "Sia sat nearby."

    show sia confused at right
    with fade

    s "Nervous?"
    a "Ahh, a little."
    s "You will do fine."
    a "You too."

    "The teacher handed out the papers."
    "The room became silent."
    "Aarav looked at the first question."

    a "Okay, let's do this."

    "For the next three hours, there was nothing except the sound of pens."
    "When the exam ended, everyone walked outside."
    "The same happened on each of the remaining exam days."

    scene bg school
    with fade

    show aarav happy at left
    show sia playful smile at right
    with dissolve

    s "How were the exams?"
    a "Better than I expected."
    s "Same."
    a "Think you will beat me?"
    s "Definitely."
    a "We will see."

    scene bg sunset
    with fade

    "The results came."
    "Aarav had the first place."
    "Sia had the second place."

    show aarav happy at left
    show sia playful smile at right
    with dissolve

    s "Congratulations."
    a "You too."
    s "You finally beat me."
    a "Finally."
    s "Don't get too proud."
    a "Too late."

    "Both knew that Grade 10 was ending soon and they would have to leave."

    scene bg schoolyard
    with fade

    show aarav normal at left
    show sia sad blush at right
    with dissolve

    s "I am going to miss this place."
    a "Me too."
    s "Even the teachers?"
    a "Maybe not that much."
    s "I knew it."
    a "What about you?"
    s "I will miss the people."
    a "Me?"
    s "Especially you."
    a "Good answer."
    s "Idiot."

    "They smiled."

    "They knew things were going to change."
    "But they did not want change to mean goodbye."

    scene bg sunset
    with fade

    "After Class 10, life became busier."
    "Different classes."
    "Different schedules."
    "Different responsibilities."
    "But Aarav and Sia stayed together."
    "They called each other."
    "They studied together whenever they could."
    "They celebrated each other's achievements."
    "They argued sometimes."
    "Then they made up."
    "They were growing up."
    "And they were doing it together."

    scene bg school
    with fade

    "Years passed."
    "School became college."
    "Their lives became bigger than the classroom where they first met."
    "But whenever they talked about the past..."
    "They would come back to Class 8."

    show aarav happy at left
    show sia norm smile at right
    with fade

    a "Do you remember the seat?"
    s "Which seat?"
    a "The one you stole."
    s "It was mine."
    a "There was no name on it."
    s "There should have been."
    a "You still say that?"
    s "Forever."
    a "Fair enough."

    "Aarav smiled."

    a "I am glad you stole it."
    s "Why?"
    a "Because otherwise..."
    a "We might never have talked."
    s "Maybe."
    a "And that would have been terrible."
    s "Very."

    scene bg sunset
    with fade

    "Years later."
    "Aarav stood beside Sia."

    show aarav happy at left
    show sia norm smile at right
    with dissolve

    a "Ready?"
    s "I have been ready for a long time."
    a "Nervous?"
    s "A little."
    a "Me too."
    s "Then don't mess it up."
    a "I won't."

    "The two people who had met over a school chair years ago were now beginning another chapter of their lives."
    "They had grown together."
    "They had supported each other."
    "They had chosen each other."
    "And after all those years..."
    "They were still choosing each other."

    scene bg sunset
    with fade

    "Sometimes the best stories aren't about finding the perfect person."
    "They are about growing with someone."
    "Learning."
    "Forgiving."
    "Laughing."
    "And staying when life becomes difficult."
    "Aarav and Sia started in a classroom."
    "But it did not end there."
    "It became a lifetime."
    "The End!!"

    "Normal mode finished."
    return


label cheating_mode:

    scene bg school
    with fade

    "The classroom was louder than usual."

    show aarav normal at left
    a "I should have stayed home."
    show sia norm smile at right
    s "Why?"
    a "Too many people."
    s "You are one of the people."
    a "Exactly."
    s "I am Sia."
    a "Aarav."
    s "I know."
    a "Everyone knows my name apparently."
    s "The teacher does."
    a "That's different."
    s "Not really."

    scene bg classroom
    with dissolve

    show aarav clueless at left
    show sia norm smile at right
    s "Did you understand today's lesson?"
    a "No."
    s "Honest."
    a "Yesh."
    s "Want my notes?"
    a "Yes."
    s "Then you owe me."
    a "What do I owe you?"
    s "A snack."
    a "That's expensive."
    s "Then study harder."
    a "Deal."

    scene bg schoolyard
    with dissolve

    show aarav happy at right
    show sia playful smile at left
    a "Here."
    s "What's that?"
    a "Your snack."
    s "You actually remembered."
    a "I remember the important things."
    s "Am I important?"
    a "Maybe."
    s "Maybe?"
    a "Don't get excited."
    s "Too late."

    "They laughed."


    menu:
        "Spend the whole break talking with Sia":
            a "I don't have anywhere else to be."
            s "Good, you are stuck with me."
            a "Sounds dangerous."
            s "It is."

            "They spent the rest of the break talking about music, school, and random things."

        "Invite Rohan and the others to join":
            a "Should we call the others?"
            s "Sure, more people, more chaos."

            show rohan happy at center
            r "What are you two talking about?"
            s "Nothing you would understand."
            r "That's rude."
            a "She's like that."
            "They all laughed."
            hide rohan

    scene bg classroom
    with fade

    show aarav normal at left
    show sia norm smile at right
    with dissolve

    s "Aarav."
    a "Yes, Sia?"
    s "Do you like anyone?"
    a "Maybe."
    s "Who?"
    a "Ahhhh."
    s "Whooo?"
    a "Ahhhhh."
    a "...."
    s "Why are you taking such a long pause?"
    a "It's you, Sia."

    show sia blushing cry at right
    with dissolve

    s "Ohh."
    a "Bad answer?"
    s "Noo."
    s "I like you too."

    scene bg sunset
    with fade

    show aarav happy blush at left
    show sia playful smile at right
    with dissolve

    s "So we are together?"
    a "Yes."
    s "Good."
    a "That's it?"
    s "What else do you want me to say?"
    a "Something memorable."
    s "Kinda... three magical words."
    a "Yess."
    s "You say it first."
    a "Ahhhh."
    a "....."
    s "Huhh? Sayyy."
    a "I love you, Sia."
    s "I love you too, Aarav."

    scene bg sunset
    with fade

    "And just like that, the classmates from the start of Grade 8..."
    "Became lovers."
    "Class 8 had finally ended."
    "They were excited to join Class 9."
    "And to make new memories."
    "But they didn't know what was coming in Class 9."
    "They were happy. That's all."


    # Story of class 9
    # Rohan is going to join the story

    scene bg school
    with fade

    "One year later..."
    "Grade 9 began with new subjects, new classmates, and a few new problems."

    scene bg classroom
    with dissolve

    show aarav happy at left
    show sia norm smile at right
    with dissolve

    a "Finally, a new year."
    s "And more homework."
    a "Don't ruin the moment."
    s "I am just being realistic."

    show rohan normal talking at center
    with dissolve

    r "Heyy, you two."
    a "Oh, hey Rohan."
    s "You are in our class this year?"
    r "Looks like it."
    a "Good luck surviving."
    r "I think I will be fine."
    s "That's what everyone says."

    "Rohan quickly became part of their group, and everything felt normal."
    "Suddenly the group of two became a group of three."
    "Aarav was afraid of losing Sia."


    scene bg schoolyard
    with fade

    show aarav normal at left
    show sia playful smile at center
    show rohan happy at right
    with dissolve

    r "You both always sit together."
    a "Pretty much."
    a "She is basically my permanent class partner."
    s "And he is my unpaid homework assistant."
    r "Sounds like a great deal."
    a "For her, maybe."

    menu:
        "Joke about Rohan joining your group":
            a "Don't worry, Rohan. We might let you sit with us."
            r "How generous."
            s "Only if you bring snacks."
            r "I knew there would be conditions."

        "Ask Rohan what he thinks of the class":
            a "So, what do you think of our class?"
            r "It's alright. People are friendly."
            s "And the teachers?"
            r "I will need more time to judge them..."
            a "Fair answer."

    scene bg classroom
    with fade

    "As the week passed, Aarav noticed that Sia and Rohan were talking more."
    "It did not seem strange at first. They were friends, after all."

    show aarav normal at left
    show sia norm smile at right
    with dissolve

    a "Are you coming to the library after class?"
    s "Maybe. I have something to do."
    a "What thing?"
    s "Just something..."
    a "Okay."

    "Sia quickly changed the topic."

    menu:
        "Ask Sia if something was wrong":
            a "You seem a little different lately. Is everything okay?"
            s "Yeah, Aarav. I am just busy."
            a "If something is bothering you, you can tell me."
            s "I know. Thank you."
            "She smiled, but Aarav felt that something was left unsaid."

        "Give her some space":
            a "Okay. Message me when you are free."
            s "I will."

            "Aarav decided not to overthink it."

        "Ask if Rohan is the reason":
            a "Is this about Rohan?"
            s "What? No."
            a "I was just asking..."
            s "Please don't make this weird."

            "The conversation ended earlier than Aarav expected."

    scene bg hallway
    with fade

    "A few days later, Aarav came back to the classroom to collect his notebook."
    "He heard Rohan and Sia nearby."

    show sia norm smile at left
    show rohan normal at right
    with dissolve

    r "You haven't told him?"
    s "Not yet."
    r "You should."
    s "I know. Just give me time."

    "Aarav stopped near the doorway. He wasn't sure what they were talking about."

    menu:
        "Walk in and ask what they are discussing":
            show aarav huh at center
            with dissolve
            a "What are you two talking about?"
            s "Nothing important."
            r "Just class stuff."
            a "Okay..."

            "Their answer came too quickly. Aarav picked up his notebook and left."

        "Stay quiet and leave":
            "Aarav quietly picked up his notebook and left. He decided to ask Sia later."

        "Wait until Rohan leaves and talk to Sia":

            show sia confused at left
            show aarav upset at right
            hide rohan
            with dissolve
            a "Can I ask you something...?"
            s "Of course."
            a "What haven't you told me?"
            s "Aarav... not here..."
            a "Then when? Where?"
            s "Aarav, I will explain later..."
            "Aarav nodded, but the answer did not make him feel better."


    scene bg schoolyard
    with dissolve

    "The next week, Sia started cancelling plans."
    "Sometimes she said she had homework."
    "Sometimes she said she was tired."
    "Sometimes she didn't reply at all."

    show aarav normal
    with dissolve

    menu:
        "Send Sia a calm message":
            a "Hey, we haven't talked properly lately. Can we meet after school?"
            show sia dark distant
            s "Maybe tomorrow. I am busy today."
            a "Okay, let me know."

        "Call Rohan and ask if he knows anything":
            show rohan normal at right
            with dissolve
            a "Hey, have you talked to Sia recently?"
            r "Yes! Sometimes. Why?"
            a "She's been distant."
            r "Maybe she is dealing with something. Don't worry too much."
            "Rohan sounded unusually careful with his words."

        "Focus on school and wait":
            hide aarav

            "Aarav decided to focus on his studies. He had exams coming up."
            "Still, the unanswered questions stayed in his mind."


    # The first biggest lie........
    scene bg hallway
    with fade

    "One afternoon, Aarav was sitting outside the classroom. Sia had told him she was going to the library."
    "But when he passed the schoolyard, he saw her with Rohan."

    show sia playful smile at left
    show rohan happy at right
    with dissolve

    r "You should have seen his face today."
    s "I know! I couldn't stop laughing."
    s "Definitely."

    "Aarav stood still. They looked comfortable together. Much more comfortable than he expected."

    menu:
        "Walk up and ask why they lied":
            show aarav annoyed at center
            with dissolve
            a "I thought you were in the library."
            s "Aarav..."
            r "Hey, man."
            a "You both told me different things."
            s "Can we talk later?"
            a "That's what you always say."

            "The mood changed immediately."

        "Leave before they notice you":
            "Aarav turned around and walked away. He wanted an explanation, not an argument."

        "Ask Rohan to talk privately":
            show aarav normal at center
            with dissolve
            a "Rohan! Can I talk to you for a minute?"
            r "Sure."
            hide sia
            with dissolve
            a "What's going on between you and Sia?"
            r "We are only friends."
            a "Only friends?"
            r "You should ask her."
            "Rohan looked away. That answer told Aarav more than he wanted to know."


    scene bg bedroom
    with fade

    "That night, Aarav kept thinking about the afternoon. He decided he needed a clear answer."

    menu:
        "Message Sia: We need to talk":
            "Aarav sent the message."
            s "Okay, tomorrow."
            "Aarav put his phone down."

        "Call Sia immediately":
            "Aarav called Sia. She answered after a few rings."
            s "Hello!!"
            a "Can you tell me what's happening?"
            s "Not on the phone, Aarav."
            a "Then tomorrow. No excuses."
            s "Okay."

        "Do nothing tonight":
            "Aarav decided to sleep and speak to her the next day."

    # The truth

    scene bg schoolyard
    with fade

    "The next afternoon, Sia finally met Aarav."

    show aarav normal at left
    show sia dark distant at right
    with dissolve

    a "Can we talk honestly?"
    s "Yes..."
    a "Are you hiding something from me?"
    s "Aarav..."
    a "Please. Just answer."

    menu:
        "Ask directly about Rohan":
            a "Is there something going on between you and Rohan?"
            s "I didn't want you to find out like this."
            a "Find out what?"
            s "We've been spending a lot of time together."
            a "I noticed."
            s "And I started liking him."
            a "While we were together?"
            s "I don't know how to explain it."
            a "Try."

        "Ask why she has been avoiding you":
            a "Why have you been avoiding me?"
            s "I did not know how to talk to you."
            a "About what?"
            s "About Rohan. I think my feelings have changed."
            a "You could have told me."
            s "I know..."

        "Give her one chance to tell the truth":
            a "I am going to ask once. Is there anything I should know?"
            s "Yes."
            a "I am listening."
            s "Rohan and I have become close. Closer than we should have."
            a "So it wasn't just friendship."
            s "I am sorry, Aarav."
            a "I wish you had told me earlier."

    show sia sad blush at right
    show aarav upset
    with dissolve

    s "I never wanted to hurt you..."
    a "But you still did."
    s "I know."
    a "Were you going to tell me?"
    s "I was trying to find the right time."
    a "There is no perfect time to tell someone the truth."


    menu:
        "Ask if she still wants to be with you":
            a "So do you still want this relationship?"
            s "Honestly, I don't know."
            a "Then I can't keep pretending everything is normal."
            "Neither of them spoke for a while..."
            "........."

        "Tell her the relationship is over":
            a "I can't continue like this."
            s "Aarav, please..."
            a "I cared about you. That's why this hurt."
            "Sia looked down. Aarav stepped away."

        "Ask her to explain everything":
            a "I want to hear the whole truth. No more half answers."
            s "Rohan and I started talking after school. Then I started hiding our conversations."
            s "I knew it was wrong, but I kept doing it."
            a "And you let me believe everything was fine."
            s "I am sorry."
            a "I needed honesty, Sia."



    # Rohan's side
    scene bg hallway
    with fade

    "Later that day, Aarav found Rohan near the hallway."

    show aarav annoyed at left
    show rohan normal at right
    with dissolve

    r "Aarav."
    a "We need to talk."
    r "About Sia?"
    a "You already know."
    r "Look, I didn't plan for this to happen."
    a "But you knew I was with her."
    r "I know."
    a "Then why?"
    r "I started liking her. I should have stayed out of it."
    a "You could have been honest with me."
    r "You are right."

    menu:
        "Tell Rohan you need distance":
            a "I don't want to talk to you for a while."
            r "I understand."
            a "Don't make this harder than it already is."
            r "I won't."

        "Ask Rohan why he kept it secret":
            a "Why didn't you tell me?"
            r "I was scared of losing our friendship."
            a "So you risked it anyway?"
            r "I know. I handled it badly."

        "Hear him out, but don't forgive him yet":
            a "I am listening. But that doesn't mean everything is okay."
            a "Yes, you should have told me."


    # GRADE 10 Starts here:::::::::::::::::::
    scene bg school
    with fade

    "Grade 10 finally arrived. The school was full of exam schedules, revision notes and nervous conversations."
    "Aarav tried to focus on his studies, even though everything had changed."

    scene bg classroom
    with dissolve

    show aarav upset at left
    with dissolve

    a "I need to focus. Exams are too close."

    menu:
        "Study with your classmates":
            "Aarav joined the study group. For the first time in weeks, he thought about something else."
            show rohan normal at right
            r "Need help with this question?"
            a "I think I can solve it."
            r "Alright."
            "They kept the conversation polite and focused on school."

        "Study alone in the library":
            "Aarav chose a quiet corner of the library and worked through the questions one by one."

        "Ask Sia if she wants to study together":
            "Aarav sent Sia a short message."
            s "Are you sure?"
            a "Only if we can focus on the exam."
            s "Okay!! Thank you."
            "They studied together, but the old closeness was gone."

    scene bg examhall
    with fade

    "The exam day finally arrived. Aarav sat down and looked at the question paper."
    "For the next few hours, there was nothing except the sound of pens."

    show aarav normal
    with dissolve

    a "Okay, let's do this."

    scene bg school
    with fade

    "When the exam ended, everyone walked outside. Some students discussed answers. Others were already celebrating."

    show aarav happy at left
    show sia sad blush at right
    with dissolve

    s "How was the exam?"
    a "Better than I expected."
    s "That's good."
    a "How was yours?"
    s "It was okay."

    "There was an awkward silence."

    menu:
        "Wish Sia good luck for the remaining exams":
            a "Good luck for the next exam."
            s "Thank you, Aarav. You too."
            "They walked in different directions."

        "Keep the conversation short":
            a "I should go. See you."
            s "Yeah, see you."
            "Aarav left without looking back."

        "Ask if she is doing okay":
            a "Are you doing okay?"
            s "I am trying."
            a "I hope things work out for you."
            s "I hope the same for you."

            "For a moment, they spoke like the old friends they used to be."

    scene bg sunset
    with fade

    "The results were announced a few weeks later. Aarav had done well."

    show aarav happy
    with dissolve

    a "I made it."

    "As the school year came to an end, Aarav had one final decision to make."

    menu:
        "Choose yourself and move on":
            jump ending_move_on

        "Give Sia a chance to explain, but start over as friends":
            jump ending_friends

        "Meet Sia and Rohan together for one final conversation":
            jump ending_final_conversation


# Ending 1

label ending_move_on:

    scene bg schoolyard
    with fade

    show aarav normal at left
    show sia sad blush at right
    with dissolve

    s "So this is goodbye?"
    a "Not exactly. We might see each other around."
    s "But things won't be the same..."
    a "I know."
    s "I am sorry for everything."
    a "I hope you will learn from it."
    s "I will."

    "Aarav walked away. It was not the ending he once imagined."
    "But he understood that moving forward was sometimes the healthiest choice."

    scene bg sunset
    with fade

    "Years later, Aarav remembered the good moments without forgetting the lesson."
    "He made new friends, followed his interests, and built a life of his own."
    "The past remained part of his story. It did not have to decide his future."
    "ENDING 1: MOVING ON"
    return


# Ending 2

label ending_friends:

    scene bg school
    with fade

    show aarav normal at left
    show sia sad blush at right
    with dissolve

    s "Thank you for meeting me."
    a "I wanted to talk properly."
    s "I know I hurt you."
    a "You did."
    s "I don't expect things to go back to how they were."
    a "Good, because they won't."
    s "Can we at least be friends someday?"
    a "Maybe. But we need time."

    "They agreed to give each other space."
    "There was no promise that everything would return to normal."

    scene bg sunset
    with fade

    "Aarav learned that forgiving someone did not mean pretending nothing happened."
    "For now, friendship was enough."
    "ENDING 2: STARTING OVER"
    return


# Ending 3

label ending_final_conversation:

    scene bg schoolyard
    with fade

    show aarav normal at left
    show sia sad blush at right
    show rohan nervous at center
    with dissolve

    a "I wanted us to talk together."
    r "I know."
    s "We both owe you an apology."
    a "I don't want another excuse. I want honesty."
    r "I should have told you what was happening."
    s "And I should have been honest instead of avoiding the conversation."
    a "You both made your choices."
    s "I know."
    r "I am sorry, man."
    a "I hope you both understand why this hurt."

    menu:
        "End the conversation and leave":
            a "I think that's all I needed to say."
            s "Take care, Aarav."
            r "You too."
            "Aarav left the schoolyard with a clearer mind."

        "Tell them you need time":
            a "I need time. Please don't expect me to act like nothing happened."
            s "We understand."
            r "Take all the time you need."
            "For once, nobody tried to rush the conversation."

        "Wish them well and move forward":
            a "I hope things work out for both of you."
            s "Thank you."
            r "Thanks, Aarav."
            "Aarav turned toward the school gate. He was ready for whatever came next."

    scene bg sunset
    with fade

    "Some friendships survive difficult moments. Some relationships change forever."
    "Sometimes, the most important thing is learning when to walk forward."
    "Aarav's story was not over. It was simply entering a new chapter."
    "ENDING 3: THE LAST CONVERSATION"
    return
