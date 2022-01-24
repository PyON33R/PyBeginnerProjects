from random import choice
from string import ascii_lowercase
hangman_steps = [  
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

def get_word(datafile):
    with open(datafile, 'r') as file:
        words = [word.strip() for word in file.readlines() if not ("-" in word or " " in word)]
    return choice(words)

def play():
    alphabets = list(ascii_lowercase)
    the_word = list(get_word('words.txt'))
    save_word = the_word.copy()
    guess_word = list('_' * len(the_word))
    num = 0
    hang_step = 0
    print("We have taken a word, Your turn => Guess it! ** 7 Wrong Guesses and You Die ** ")
    while guess_word != save_word:

        guess_letter = input(f"Your Guess No {num + 1}: ")
        if guess_letter in alphabets and guess_letter in the_word:
            guess_word[the_word.index(guess_letter)] = guess_letter
            the_word[the_word.index(guess_letter)] = "_"
            print(f"The Word After Your Guess No {num + 1}: {''.join(guess_word)}")
        else:
            if hang_step < len(hangman_steps) - 1:
                print(hangman_steps[hang_step])
                hang_step += 1
            else:
                print("You are Hanged")
                print(hangman_steps[hang_step])
                return

        num += 1
    print(f"You Won. The Word Is: {''.join(guess_word)}")

play()

