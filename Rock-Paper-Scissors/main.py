import random

user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

while True:
    # Get user's input
    users_play = input("Type Rock/Paper/Scissors (r/p/s) or q to quit: ").lower()
    if users_play == "q":
        break
    
    if users_play not in options:
        continue
    
    # Get computer's input (rock: 0, paper: 1, scissors: 2)
    random_number = random.randint(0,2)
    computers_play = options[random_number]
    print("Computer picked", computers_play + '.')

    # Compare the inputs to see who go the score
    if users_play == "r" and computers_play == "s":
        print("You won!")
        user_wins += 1
    elif users_play == "p" and computers_play == "r":
        print("You won!")
        user_wins += 1
    elif users_play == "s" and computers_play == "p":
      print("You won!")
      user_wins += 1
    else:
      print("You lost")
      computer_wins += 1
    
    print("User Score:", user_wins, "Computer Score:", computer_wins)
    
print("Goodbye!")
