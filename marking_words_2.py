# -*- coding: utf-8 -*-
"""Marking words 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qwOgaO8UmpgebGi4oBaAD7Z6gNG9AFiT
"""

import random
from google.colab import files
files.upload()
def read_words():
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    return words

def start_game():
    words = read_words()
    correct_answers = 0
    incorrect_answers = 0

    while True:
        word = random.choice(words)
        print(f"Word: {word}")
        answer = input("Is it a marking word? (y/n): ")

        if answer.lower() == 'y':
            if word in marking_words:
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect.")
                incorrect_answers += 1
        elif answer.lower() == 'n':
            if word not in marking_words:
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect.")
                incorrect_answers += 1
        else:
            print("Invalid input. Please enter y or n.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print(f"Final score: {correct_answers}/{correct_answers+incorrect_answers}")

if __name__ == "__main__":
    marking_words = ["the", "a", "an", "in", "on", "at", "to", "from", "by", "with"]
    start_game()