# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image alj surprise = im.FactorScale("alj/surprise.png", 0.2)
image bg altar = im.FactorScale("bg altar.jpg", 0.5)
define alj = Character("Alejandro")
define n = Character("Narrador")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg altar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alj surprise

    # These display lines of dialogue.

    n "Abuela (Océlotl) y su nieto (Alejandro) como cada año se disponían a colocar la ofrenda para el día de muertos. Cuando que el pequeño nieto se distraía y terminaba jugando con las flores"

    # This ends the game.

    return
