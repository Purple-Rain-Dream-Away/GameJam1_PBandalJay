# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 = Character("Clara")  # First customer
define mic = Character("Michelle")  # Bouquet customer
define b = Character("Big Billy")  # Noir customer
define t = Character("Tall Lady")
define m = Character("Me")
define mg = Character("The Blessed Dragon of the Mount Hwa Sect") # murim guy

# The game starts here.


# Standard gift giving
label start:
    jump chapter1

# moved stuff to indiviual chapter files