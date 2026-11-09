
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

    a "I am Aarav."
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

    s "I can bet you can't finish this before me."
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
    a "Now I will be talking with myself."

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
    s "I got the highest marks in science"
    a "Seriously"
    s "Yep"
    a "I thought i was going to beat you"
    s "Your thinking is wrong aaravvv"
    a "Next exam"
    s "Deal"
    a "yeshhh"

    "Their competition became one of their favorite things"
    "Neither wanted the other to fail."
    "They simply wanna push each other"

    scene bg classroom
    "Class 10 arrived"
    "Everything suddenly felt more serious"
    "Board exam were getting closer"
    "Teacher gave more homework"
    "Everyone talked about the marks"

    show aarav upset at left
    show sia annoyed at right
    with dissolve

    a "I don't understand this chapter"
    s "You haven't even tried"
    a "I did"
    s "For 5 minutes"
    a "I am still trying"
    s "Give me your notebook"
    a "Whyy?"
    s "I will explain it"
    a "You are saving me again"
    s "Someone has to"

    "They studied together almost every day"
    "Sometimes they understood everything"
    "Sometime they understood nothing"
    "Sometimes they understood nothing"
    "Sometime they spent 20 minutes instead of studiyng"

    show sia mischievous
    with dissolve

    s "We have been studying for an hout"
    a "We studied for 10 minutes"
    s "The rest was discussion"
    a "About snacks"
    s "Important discussion"
    a "Very important"

    scene bg bedroom
    with fade

    "The night before the exams were different"
    "There were few jokes"
    "More books"
    "More Pressure"

    show aarav normal at left
    show sia norm smile at right
    with dissolve

    a "Are you still awake?"
    s "yeah"
    a "You should sleep"
    s "You too"
    a "This is time I mean it"
    s "Sure"
    a "Good Luck tomorrow"
    s "Good Luck"

    scene bg examhall
    show aarav normal at left
    with dissolve

    "the exam day finally arrives"
    "Aarav Sat Down"
    "Sia Set nearby"

    show sia confused at right
    with fade

    s "nervous"
    a "Ahh Little"
    s "You will do it fine"
    a "You too"
    "The teacher handed out the papers"
    "The room became silent"
    "Aarav looked into the first question"

    a "Okey Lets Do this"
    "for next three hours there was nothing except the sound of pens"
    "When The exam ended, everyone walked outside"
    "Like The Day The 7 exam passed"

    scene bg school
    with fade

    show aarav happy at left
    show sia playful smile at right
    with dissolve

    s "How were the exams?"
    a "Better than i expected.."
    s "Same"
    a "Think you will beat me"
    s "Definately"
    a "We will see"

    scene bg sunset
    with fade
    "The Result came"
    "Aarav had the first place"
    "Sia had the second place"


    show aarav happy at left
    show sia playful smile at right
    with dissolve

    s "Congratulations"
    a "Youu too"
    s "You finally beat me"
    a "Finally"
    s "Dont get too proud"
    a "too late"

    "Both knew that grade 10 was ending soon they would have to leave"

    scene bg schoolyard
    with fade

    show aarav normal at left
    show sia sad blush at right
    with dissolve

    s "I am going to miss this place"
    a "mee too"
    s "Even teachers?"
    a "Maybe not that much"
    s "I knew it"
    a "What about you"
    s "I will miss the people"
    a "me?"
    s "Specially you"
    a "Good Answer"
    s "Idiot"
    "They Smiled"

    "They Knew things were going to change "
    "But they didnot want change to mean goodbye"

    scene bg sunset
    with fade

    "After class 10 life became busier"
    "Different classes"
    "Different schedules"
    "Different responsibilities"
    "But aarav and sia stayed together"
    "They called each other"
    "They Studied together whenever they could"
    "They celebrated each others achievements"
    "They argued sometimes"
    "Then they made up"
    "They were growing up"
    "And they were doing together"

    scene bg school
    with fade

    "year passed"
    "School became college"
    "Their lives became bigger than the classroom where they first meet."
    "But whenever they talked about the past"
    "They would come back to class 8th."

    show aarav happy at left
    show sia norm smile at right
    with fade

    a "Do you remember the seat?"
    s "Which Seat?"
    a "The one you stole"
    s "It was mine"
    a "There wasnot name on it"
    s "There should have been"
    a "You still say that?"
    s "Forever"
    a "Fair enough"
    "Aarav Smiled"
    a "I am glad you stole"
    s "Why?"
    a "because otherwise"
    a "We might never talked"
    s "Maybe"
    a "And that would have been terrible"
    s "very"

    scene bg sunset
    with fade

    "Years Later"
    "aarav stood beside sia"

    show aarav happy at left
    show sia norm smile at right
    with dissolve

    a "Ready?"
    s "I have been ready for a long time"
    a "Nervous?"
    s "A Little"
    a "mee too"
    s "Then dont mess it up"
    a "I wont"

    "The two people who had met over a school chair years ago were now begginning another chapter of their lives."
    "They had grown together"
    "They had supported each other"
    "They had chosen each other"
    "And after all those years"
    "They are still choosing each other"

    scene bg sunset
    with fade

    "Sometimes the best stories arent about finding the perfect person."
    "They are about growing with someone"
    "Learning"
    "Forgiving"
    "Laughing"
    "And staying when the life becomes diffcult"
    "Aarav and sia started in a classroom"
    "But it didnot end there"
    "It became a lifetime"
    "The End!!"


    "Normal mode Finished"
    return

label cheating_mode:

    scene bg school
    with fade 

    "The classroom was louder than usual"
    show aarav normal at left 
    a "I should have stayed home"
    show sia norm smile at right
    s "Why?"
    a "Too many people "
    s "You are one of the people "
    a "Exactly"
    s "I am Sia"
    a "Aarav"
    s "I know "
    a "Everyone knows my name apprently"
    s "The teacher does"
    a "Thats Different"
    s "Not really"

    scene bg classroom 
    with dissolve 
    show aarav clueless at left 
    show sia norm smile at right 
    s "Did you understand today's lesson?"
    a "No"
    s "Honest"
    a "yesh"
    s "Want my notes"
    a "yes"
    s "Then you owe me"
    a "What do I owe you?"
    s "A snack"
    a "Thats Expensive"
    s "Then Study harder"
    a "Deal"

    scene bg schoolyard
    with dissolve 

    show aarav happy at right 
    show sia playful smile at left 
    a "here"
    s "whats that"
    a "your snack"
    s "you actually remembered"
    a "I remember the important things"
    a "Am I important"
    a "Maybe "
    s "Maybe?"
    a "Dont get excited"
    s "too late "

    "They laughed"
    

    menu: 
        "Spend the whole break talking with Sia":
            a "I don't have anywhere else to be"
            s "Good you are stuck with me."
            a "Sound dangerous"
            s "It is"

            "They spent the rest of the break talking about music, school, and random things."

        "Invite rohan and the others to join":
            a "Should we call other "    
            s "Sure more people more chaos"

            show rohan happy at center 
            r "What are you two talking about?"
            s "Nothing you would understand"
            r "That's rude"
            a "She's like that"
            "They all laughed"

            scene bg classroom 
            with fade 
            show aarav normal at left 
            show sia norm smile at right 
            with dissolve 
            s "Aarav"
            a "Yes Sia"
            s "Do you like anyone?"
            a "Maybee"
            s "Who?"
            a "Ahhhh"
            s "Whoo?"
            a "Ahhhhh"
            a "...."
            s "Why are you taking this long pause?"
            a "It's you Sia"
            show sia blushing cry at right 
            with dissolve 
            s "Ohh"
            a "Bad Answer?"
            s "Noo"
            s "I like you too"

            scene bg sunset
            with fade
            show aarav happy blush at left
            show sia playful smile
            with dissolve 

            s "So we are together?"
            a "Yes"
            s "Good"
            a "Thats it"
            s "What else you want me to say?"
            a "Something memorable"
            s "Kinda Three magical word"
            a "Yess"
            s "Youu say first "
            a "Ahhhh"
            a "....."
            s "Huhh Sayyy"
            a "I love you Sia"
            s "I love you too Aarav"
            
            scene bg sunset
            with fade

            "And just like that the classmate at the starting of Grade 8"
            "Became lover"
            "Class 8 was finally ended"
            "They were excited to join class 9 "
            "And making new memories"
            "But they didn't knew what was gonna be in class 9th"
            "They were happy Thats it"



            # Story of class 9
            #Rohan is gonna Join the story

            scene bg school
            with fade 

            "One year later.... Grade 9 began with new subjects , new classmates, and and few new problems."

            scene bg classroom 
            with dissolve 
            
            show aarav happy at left 
            show sia norm smile at right 
            with dissolve 
            a "Finally a new year"
            s "And More Homeworks"
            a "Don't ruin the moment"
            s "I am Just being realistic"

            show rohan normal talking at center
            with dissolve 
            r "heyy you two"
            a "oh, hey rohan"
            s "You are in our class this year?"
            r "Looks like it"
            a "Good Luck Surviving"
            r "I think i will be fine "
            s "That's what everyone says"
            
            "Rohan Quickly became the part of their group, everything felt normal."
            "Suddenly the group of 2 became the group of 3"
            "Aarav was afraid of loosing sia"


            scene bg schoolyard
            with fade
            show aarav normal at left 
            show sia playful smile at center 
            show rohan happy at right 
            with dissolve 
            r "You both always sit together"
            a "Preety Much"
            a "She is basically my permanent class patner."
            s "And he is my unpaid homework assistant"
            r "Sounds like a great deal"
            a "For her, Maybe"

            menu:
                "Joke about Rohan joining your group":
                    a "Don't worry, Rohan. We might let you sit you with us."
                    r "How generous"
                    s "Only if you bring snacks "
                    r "I knew there would be conditions."

                "Ask Rohan what he thinks of the class?":
                    a "So, what do you think of our class?"
                    r "It's alright. People are friendly."
                    s "And the teachers?"
                    r "I will need more time to judge them..."
                    a "Fair answer."

            scene bg classroom
            with fade    
            "As the week passed , Aarav Noticed that Sia and Rohan were talking more."
            "It did not seem strange at first. They were friends , after all."
            show aarav normal at left
            show sia norm smile at right 
            with dissolve 
            a "Are you coming to library after class?"
            s "Maybe. I have something to do"
            a "What thing?"
            s "Just Something...."
            a "Okey"

            "Sia Quickly Changed the topic"

            menu:
                "Ask sia if something was wrong":
                    a "You seem a little different lately. Is everything okey?"
                    s "Yeah Aarav. I am Just Busy"
                    a "If something is bothering you , you can tell me."
                    s "I know , Thankyou"
                    "She smiled but aarav felt that something was left unsaid."

                "Give her some space":
                    a "Okey. Message me when you are free."    
                    s "I will"

                    "Aarav Decides not to overthink it."

                "Ask of rohan is the reason":
                    a "Is this about Rohan?"    
                    s "What? No"
                    a "I was just asking.."
                    s "Please don't make this weird"

                    "The conversation ended earlier than Aarav Expected"

            scene bg hallway 
            with fade        
            "A few days later, Aarav came back to the classroom to collect his notebook."
            "He Heard Rohan and Sia Nearby"

            show sia norm smile at left 
            show rohan normal at right 
            with dissolve 
            r "You haven't told him?"
            s "Not yet."
            r "You should"
            s "I know. Just give me time"
            "Aarav Stopped near the doorway. He wasn't sure what they were talking about."

            menu:
                "Walk in and ask what they are discussing":
                    show aarav huh at center 
                    with dissolve 
                    a "What are you two talking about?"
                    s "Nothing Important"
                    r "Just class stuff"
                    a "Okey..."

                    "Their answer came too quickly. Aarav picked up his notebook and left."

                "Stay Quite and leave":
                    "Aarav quitely picked up his notebook and left. He decided to ask sia later."    

                "Wait Until rohan leaves and talk to sia":

                    show sia confused at left
                    show aarav upset at right
                    hide rohan normal
                    with dissolve 
                    a "Can I ask you something.."
                    s "Of course "
                    s "What haven't you told me?"
                    s "Aarav... Not here..."
                    a "Then When? Where?"
                    s "Aarav I will explain later...."
                    "Aarav Nooded, but the answer did not make him feel better."
                    










            


            



            


        





   






