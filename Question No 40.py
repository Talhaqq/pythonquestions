"""An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a
new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point =
I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from given list of
words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and
4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to
work with (say) colour words only. The interaction with the program may look like so:
>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
"""


import random

def choose_random_word():
    color_words = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
    return random.choice(color_words)

def generate_anagram(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_anagram_game():
    original_word = choose_random_word()
    anagram = generate_anagram(original_word)

    print("Welcome to the Word Anagram Game!")
    print("Try to guess the original word from its anagram.")
    print(f"Anagram: {anagram}")

    while True:
        user_guess = input("Your guess: ").lower()

        if user_guess == original_word:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            print("Incorrect. Try again!")

play_anagram_game()
