from PIL import Image 

#def bob():
name = input("Enter your name please: ")
while not(name.isalpha()):
        
    name = input("Enter your name please: ")
else:
    print("Nice to meet you " + name + " welcome to my game!")
            
#bob()


# your first story encountered.
answer = input(
    "you have just gotten out of work after a very long day, and one of your co-workers asks you if you want to go get a drink with them. Do you go get a drink with them or just walk home? (get a drink/walk home) ").lower()
# first scenario

if answer == "get a drink":
    image1 = Image.open('beer.jpg')
    image1.show('beer.jpg')
    answer = input("So you go out for drinks with some of your co-workers and out of no where you are getting rob. \n what should you do? give them your money or fight them ")

    if answer == "give them your money":
        image1 = Image.open('give your money.webp')
        image1.show('give your money.webp')
        print("You and your co-workers give them your money but one of them resists and so one of your co-workers dies from the robber and they leave. YOU LOST! ")
    elif answer == "fight them":
        image1 = Image.open('fighting.jpg')
        image1.show('fighting.jpg')
        print("You and your co-workers fight them with what's around them and you guys were able to fend the robbers away with no casualities from your co-workers. \n After that you and your co-workers happily are drinking. YOU WIN! ")
    else:
        print("invalid option and you died that's unfortunate! ")
        image1 = Image.open('game over.jpg')
        image1.show('game over.jpg')

#second scenario
elif answer == "walk home":
    image1 = Image.open('walking.jpg')
    image1.show('walking.jpg')
    answer = input("You are walking home and as your walking home you meet a strange man and he gives you a strange object. Do you take the object, (yes/no) ")
    
    if answer == "yes":
        image1 = Image.open('strange item.jpg')
        image1.show('strange item.jpg')
        print("Once you take the strange object and you are still walking to your house, you randomly saved a starnger from getting \
    run over by a drunk driver. The stranger thanks you and changes your life, as this person is the ceo of a popular company and you are set for life. YOU WIN ")
    elif answer == "no":
        image1 = Image.open('car hits you.jpg')
        image1.show('car hits you.jpg')
        print("You ignore the strange man and walk away, as you are almost at your house a car in the far distance drives very fast and loses control and hit you. YOU LOSE ")
    else:
        print("invalid option, you lost dude! ")
        image1 = Image.open('game over.jpg')
        image1.show('game over.jpg')

else:
        print("invalid option, you lost dude! ")
        image1 = Image.open('game over.jpg')
        image1.show('game over.jpg')



print(f"Thanks for playing we hope to see you again {name} We will see you again :) ")
image1 = Image.open('thanks for playing.jpg')
image1.show('thanks for playing.jpg')
