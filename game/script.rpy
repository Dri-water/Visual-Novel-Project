# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define m = Character("player_name", dynamic = True)
define j = Character("Javier", color = "#1056e2")
define k = Character("Kaiyuan", color = "#ead40c")
define n = Character("Nisha", color = "#ef0a0a")
define h = Character("Huile", color = "#ed0db5")
define a = Character("Ansh", color = "#6d0cec")
define s = Character("Samir", color = "#1fe611")
define t = Character("Timothy", color = "#e77511")
define l = Character("Leon", color = "#0dc7ec")
define z = Character("Zelong", color = "#0de994")
define x = Character("???")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by defaults, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bunk_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kaiyuan happy1 with dissolve

    k "Good morning recruits! I'm 3SG Kaiyuan, your section commander!"

    k "how about you, recruit?"

    $ player_name = renpy.input("NAME:")
    if player_name == "":
        $ player_name = "Bob"
        k "knn can't even remember your own name?"


    k "alrighty, hi [player_name]!" 

    hide kaiyuan happy1 with dissolve


    "The sergeant goes around asking everyone else the same question... "
    "It's hard to remember faces when everyone all botak sia"

    show kaiyuan happy1 with dissolve
        

    k "Alright, now that introductions are out of the way,"

    show kaiyuan happy1:
        linear 0.5 xalign 0.0



    k "This will be your bunk for the next 9 weeks or so"

    "Actually ah, this doesn't seem as bad as I thought it would be"

    k "Since there is no \"Maria\" in Pulau Tekan, I expect you all to take ownership of the cleanliness of your own bunk"

    x "YES SERGEANT!!!"

    "knn this fucker so siao onz ah... "


    show kaiyuan happy1:
        linear 0.5 xalign 0.5

    k "Very good, recruit... the rest of you no mouth ah?!?! drop and carry on 20!"

    k "and each time i want to hear you all shout \"YES SERGEANT\" is that clear?!?!"

    m "YES SERGEANT"

    hide kaiyuan happy1 with dissolve

    "fk la"


    # This ends the game.

    return
