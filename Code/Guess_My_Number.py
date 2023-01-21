from random import *

# introduction
print("\033[1;34mHello, traveler! What brings you to my humble abode?\n"
      "Is there something I can help you with? \n"
      "Oh, I see you have an interest in games.\n"
      "Would you like to test your luck and play\n"
      "a game of 'guess my number' with me?")

# user input and making all the symbols in lower case for easier use in conditionals statements
user_answer = input("\033[1;32mPlay game? (yes/no):").lower()

# while loop to ask the player if he wants to quit and if the answer is positive terminates the program
while True:
    if user_answer != "yes":
        print("\033[1;32mAre you sure you want to quit?:")
        user_answer = input("\033[1;32m(yes/no):")
        if user_answer == "yes":
            exit()
        else:
            break
    else:
        break

# Rules
print("\033[1;34m'Guess my Number' is a game in which your opponent,\n"
      "'Albert', chooses a random number between\n"
      "'1 and 100', and your task is to guess this number.\n"
      "After each number you enter, he will give\n"  # Rules
      "you a hint of whether the number is greater or less\n"
      "than the number you selected until you guess the correct number\n"
      "or after 10 wrong attempts")

# Generates a random integer between 1 and 100
x = randint(1, 100)

# User first guess
user_number = int(input("\033[1;32mTake a guess!:"))

# Boolean to check if the game is a win or a loss
win = True

# Attempts counter
counter = 1

# while loop for guessing the number,giving hints,updating the counter and changing the Boolean to False(loss) if needed
while user_number != x:
    if counter == 10:
        win = False
        break
    if user_number > x:
        print("\033[1;34mMy number is less than yours!")
    elif user_number < x:
        print("\033[1;34mMy number is greater than yours!")
    user_number = int(input("\033[1;32mGuess again!:"))
    counter += 1

# prints a message depending on the result of the game (win/loss) using the boolean in conditional statements
if win:
    print(f"\033[1;34mGood job, traveler! You guessed my number in {counter} guesses!")
else:
    print("\033[1;34mWell fought, traveler. Though it seems fate was not in your favor this day,\n"
          "your skills and valor were not to be underestimated.")
