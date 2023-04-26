import random

top_range = input("Type a number: ")

if top_range.isdigit():
  top_range = int(top_range)
  if top_range <= 0:
    print("Please type a number greater than zero")
    quit()
else:
  print("Please type a number")
  quit()

# Does not include the upper limit in the random number generator
random_number = random.randrange(0, top_range)
num_of_guesses = 0

while True:
  # Get the user's guess
  user_guess = input("Guess the random number: ")
  num_of_guesses += 1

  # Validate the input
  if user_guess.isdigit:
    user_guess = int(user_guess)
  else:
    print("Please type a number")
    continue

  # Compare it to the random number
  if user_guess == random_number:
    print("Hurrah, you've got it.")
    print("You've got it in", num_of_guesses, "guess" if (num_of_guesses == 1) else "guesses")
    break
  else:
    print("You guessed too high" if (user_guess > random_number) else "You guessed too low")
