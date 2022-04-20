from PIL import Image
#FUNCTION CONTAINING CODE - "QUIZ GAME."
def quiz():
    print("We shall now start the game! ")
    score = 0

    answer = input("What are the big three anime? ")
    if answer.lower() == "bleach, naruto, one piece":
        print("Correct!")
        score += 1   
    else:
        print("That is not correct!")


    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing units":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")



    answer = input("What is the number one anime? ")
    if answer.lower() == "fullmetal alchemist: brotherhood":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")
    image1 = Image.open('fullmetal alchemist.jpg')
    image1.show('fullmetal alchemist.jpg')


    answer = input("How much money has the movie Avatar made? ")
    if answer.lower() == "2.84 billion":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")



    answer = input("How many call of duty games are there in the main series? ")
    if answer.lower() == "19":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")



    answer = input("Is Luxembourg the capital city of Luxembourg? ")
    if answer.lower() == "yes":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")


    answer = input("Which champion has the most bought skins in league? ")
    if answer.lower() == "lux":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")



    answer = input("how many favourites does lelouch vi Britannia have according to Mal? A: 159840, B: 152780, C: 124580, D: 151190 ")
    if answer.upper() == "B":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")
    image1 = Image.open('lelouch.jpg')
    image1.show('lelouch.jpg')


    answer = input("Name a body part that is spelled the same forward, and backward? ")
    if answer.lower() == "eye":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")


    answer = input("How many pokemon are there currently? A: 900, B:899, C: 898, D:897 ")
    if answer.upper() == "C":
        print("Correct!")
        score += 1 
    else:
        print("That is not correct!")

    print("You have gotten " + str(score) + " questions right dude! ")
    print("You have gotten " + str((score / 10) *100) + "%. ")



#CODE PROLOGUE
print("Welcome to my quiz game! ")
player = input("Do you want to play this game? ")

if player.lower() != "yes": 
    quit()

quiz()

intr = input("Would you like to play again: ")
if intr.lower() == "yes":
    quiz()
else:
    print("Thanks for playing! ")
"""
player = input("would you like to play again? ")
if player == "Yes":
    print("We shall now start the game! ")
elif player == "No":
    print("Thanks for playing well see you again soon ")
"""



