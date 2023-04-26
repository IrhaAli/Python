# Ask user a bunch of questions and tally their score based on the answer
print("Welcome to my computer quiz!")

# Initial settings
score = 0
playing = input("Do you want to play (y/n)? ")

if playing != "y":
    quit()

print("Okay, let's play :)")

# Question 1
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Score: " + str(score))

# Question 2
answer = input("What does GPU stand for? ")

if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Score: " + str(score))

# Question 3
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Score: " + str(score))
