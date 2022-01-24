from email import feedparser
from random import randint

def user_guess(x):
    random_number = randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Please Guess Again! Too High")
        elif guess < random_number:
            print("Please Guess Again! Too Low")
    print(f"Very Well, You guessed it corrrectly! The number is {guess}")

# user_guess(10)

def computer_guess(x):
    feedback = ""
    low = 1
    while feedback != "c":
        guess = randint(low, x)
        print(f"I guessed {guess}, is it the correct number?")
        feedback = input("(Too Low : l, Too High: h, Correct: c): ").lower()
        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            x = guess - 1
    print(f"Finally I guessed it Right, the number is: {guess}")

computer_guess(10)
