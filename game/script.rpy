# Defination of the character

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
    
    scene bg school 
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

    scene bg schoolyard

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

menu:
    "Normal Mode":
        jump normal_mode

    "Cheating Mode":
        jump cheating_mode


label normal_mode:
    scene bg school
    with fade
    "Grade 8."
    "The first day of a new school year"
    "New Books"
    "Old Teachers Some Might be New too"
    "New Classmates"
    "And for aarav another year of trying not to get in trouble"

    show aarav normal
    with dissolve

    a "I really should have stayed in bed"
    "Aarav Looked around classroom"
    "Most of the student were already talking with their friends"
    "some were comparing the timetables"
    "some were complaining about new teachers."
    "and some topper were already disscusing about the homework"

    a "First day and people already talking about the homework"
    a "How am i supposed to fit with them????"

    scene bg classroom

    show sia playful_smile at left
    with dissolve

    show aarav normal blush at right
    with dissolve 

    s "Heyy"
    a "Heyyy"
    s "Is that seat taken?"
    a "Nahh"
    s "Good!!"

    "Sia Sat Down"
    a "You are new"
    s "Kind off"
    s "I was in other section last year"
    a "Ohhh"
    s "You are aarav right?"
    a "Ahh yep i am"
    s "I heard you are good at maths"
    a "Who told you that?"
    s "Someone"
    a "Thats Sus!!"
    s "Whyyyyy?"
    a "Because i am not"
    s "So you were lying to everyone"
    a "Apparently"

    show sia norm smile
    with dissolve

    "Sia Laughed"
    "Aarav smiled without realizing it"

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
    s "Really"
    a "Yeah"
    s "I thought you'd say maths"
    a "Why?"
    s "You look like someone who like maths..."
    a "What does a maths person look like?"
    s "I really don't know"
    a "Exactly"
    s "Okey Fine"
    a "What's yours?"
    s "English"
    a "That make a sense"
    s "Why?"
    a "You talk a lott"
    s "Thats not related , Aarav"
    a "Definately it is"
    s "You are annoying"
    a "You have said that before"
    s "yeahh I will keep saying this"


    scene bg schoolyard
    with fade 

    "During lunch breaks they often sat together"
    "Sometime their freinds joined them"
    "Sometime it was just two of them"

    show aarav happy 
    show sia mischievous at right 
    with dissolve 

    s "I can bet you can't finish this before me"
    a "Finish what?"
    s "Your food"
    a "That's not a competition."
    s "Everything is competition"
    a "You are weird"
    s "And you are slow"
    a "Watch me"

    "Aarav Started Eating lot faster than before"

    s "Wait Seriously"
    a "You challanged me"
    s "I didn't thought you will actually do this"
    s "Craxy mann"
    a "Tooo late"

    "sia started laughing"
    "Aarav laughed too"

    "They didnot noticed how quickly they were becoming soo close"

    scene bg classroom
    with fade

    "One afternoon, Sia stayed behind after class "

    show sia sad blush
    with disslove 

    a "You are still here"
    s "Yeah"
    a "Everythinh okey?"
    s "yeahhh"
    a "You donot look okey today"
    s "I am just tired"
    a "Want to talk?"
    s "maybeee"
    "Aarav Sit beside her"
    s "Sometime I feel like everyone excepts too much"
    a "School?"
    s "School. Parents Everything"
    a "Yeahhh"
    s "You ever feel like that"
    a "Sometimes"
    s "What do you do?"
    a "Usually?"
    s "yeah"
    a "I complain"
    s "Thats your solution"
    a "Actually it works"

    "Sia laughed silently"

    s "Thanksss"
    a "For what?"
    s "Just listening..."
    a "Anytime"

    scene bg sunset
    with fade
    "That evening. Aarav Realised Something"
    "He didn't just enjoy talking with sia"
    "He cared about her"
    "More than he expected"

    show aarav normal blush
    with dissolve

    a "I think I like her"
    "He immediately regretted saying it loud"
    a "Great"
    a "Now i will be talking with myself"

    

    

    









    

    




    










    
    
   








