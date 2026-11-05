
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
image sia blush angr = "images/sia/sia blush_angry.png"
image sia blushing cry = "images/sia/sia blushing_cry.png"
image sia confused = "images/sia/sia confused.png"
image sia dark distant = "images/sia/sia dark_distant.png"
image sia dark sad = "images/sia/sia dark_sad.png"
image sia mischievous = "images/sia/sia mischeievous.png"
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

    show sia sad blush
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

  