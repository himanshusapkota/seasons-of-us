# Defination of the character

define a = Character("Aarav", color="#5DADE2")
define s = Character("Sia", color="#FF69B4")
define r = Character("Rohan", color="#58D68D")


# Importing the background images

image bg bedroom = "images/backgrounds/bedroom.jpg"
image bg classroom = "images/backgrounds/classroom.jpg"
image bg examhall= "images/backgrounds/examhall.jpg"
image bg school = "images/backgrounds/school.jpg"
image bg schoolyard = "images/backgrounds/schoolyard.jpg"
image bg hallway = "images/backgrounds/school_hallway_night.jpg"
image bg sunset = "images/backgrounds/sunset.jpg"


# Importing the character images of AARAV the goat who is gonna be heartbroken in cheating mode

image aarav angr y= "images/aarav/aarav_school_angry.png"
image aarav angry talk = "images/aarav/aarav_school_angrytalk.png"
image aarav clueless = "images/aarav/aarav_school_clueless.png"
image aarav happy = "images/aarav/aarav_school_happy.png"
image aarav happy blush = "images/aarav/aarav_school_happyblush.png"
image aarav huh = "images/aarav/aarav_school_huh.png"
image aarav normal = "images/aarav/aarav_school_normal.png"
image aarav normal blush= "images/aarav/aarav_school_normalblush.png"
image aarav tears = "images/aarav/aarav_school_tears.png"
image aarav upset = "images/aarav/aarav_school_upset.png"

# Importing the character image of SIA who becomes cheater in cheating mode

image sia angr y= "images/sia/sia angry.png"
image sia annoyed = "images/sia/sia annoyed.png"
image sia blush angr = "images/sia/sia blush_angry.png"
image sia blushing_cry = "images/sia/sia blushing_cry.png"
image sia confused = "images/sia/sia confused.png"
image sia dark distant = "images/sia/sia dark_distant.png"
image sia dark sad = "images/sia/sia dark_sad.png"
image sia mischievous = "images/sia/sia mischeievous.png"
image sia norm smile = "images/sia/sia norm_smile.png "
image sia oh = "images/sia/sia oh.png"
image sia playful smile = "images/sia/sia playful_smile.png"
image sia sad blush = "images/sia/sia sad_blush.png"

# Importing the character image of ROHAN who is the third person (kebab mey haddi)

image rohan evil = "images/rohan/rohan evil.png"
image rohan fear = "images/rohan/rohan fear.png"
image rohan happy = "images/rohan/rohan happy.png"
image rohan nervous = "images/rohan/rohan nervous.png"
image rohan normal  = "images/rohan/rohan normaltalking.png"
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
    
    scene school 
    with fade

    pause 1.0

    "Some stories begin with something big."
    "A special day"
    "A big decision"
    "Something that changes everything"

    "But some stories begin normally."
    "Just another school morning."
    "Another classroom"

    # Intro of AARAV tha GOAT
    
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

    # Intro of SIA tha what to say

    show sia norm smile 
    with dissolve 

    s "I am Sia."
    s "I am probably more talkative than Aarav."
    s "I like joking around, annoying my friends, and making boring days a little more interesting."
    s "Sometimes I make decisions without thinking too much."
    s "But I always care about the people close to me."

    hide sia
    with dissolve

    # Intro of ROHAN tha kebab mey haddi

    show rohan normal
    with dissolve

    r "I am rohan."
    r "I joined the school little later than the others"
    r "I am preety confident, so making new friends wasnot really problem"
    r "I like competition"
    r "And Honestly"
    r "I do not mind getting involved in other people's story"

    hide rohann
    with dissolve

    scene schoolyard

    show aarav normal at left 
    show sia norm smile at center
    show rohan normal at right
    with dissolve 

    "Three people"
    "Theree different personalities"
    "And a lot of moments they haven't experienced yet.."

    a "So... this is going to be a normal school year, right?"
    s "Definitely."
    r "You really think so?"
    a "Why wouldn't it be?"
    s "I don't know."
    s "Something tells me things are going to get interesting."
  
    "And she was right"
    "Before the story begins, choose how you want to play"

   








