name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (l/r)?").lower()

if answer == 'l':
    answer = input(
        "You come to a river, you can walk around it or swim across. Will you walk or swim (w/s)?")
    if answer == 'w':
        print("You made a smart more and reached your destination")
    elif answer == 's':
        print("The stream was too fast and you were swept away and drowned")
    else:
        print("Not a valid option. You lose")
        quit()
elif answer == 'r':
    print("You encountered a bear who ate you mwahahaha")
else:
    print("Not a valid option. You lose")
    quit()

print("Thank you for playing the Adventure Game", name)