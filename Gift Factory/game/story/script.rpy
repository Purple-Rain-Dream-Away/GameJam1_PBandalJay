# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 = Character("Clara")  # First customer
define mic = Character("Michelle")  # Bouquet customer
define b = Character("Big Billy")  # Noir customer
define t = Character("Tall Lady")
define m = Character("Me")
define mg = Character("The Blessed Dragon of the Mount Hwa Sect") # murim guy
define mm = Character("Middle-aged Man")
define kg = Character("Anxious Girl")
define ah = Character("Creepy Customer")
define e = Character("Elf")
define ad = Character("Alien dude")
define s = Character('Skeleton')
define h = Character("Hand")
define cow = Character("Cow")
define u = Character("Enraged Customer")

# The game starts here.
define config.layers = [  "foreground", 'master', 'transient', 'screens','overlay' ]

# Standard gift giving
label start:
    jump chapter1

# moved stuff to indiviual chapter files