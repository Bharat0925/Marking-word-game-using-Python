# -*- coding: utf-8 -*-
"""Marking words 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qwOgaO8UmpgebGi4oBaAD7Z6gNG9AFiT
"""

import random

def generate_word_grid(rows, cols):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    grid = [[random.choice(alphabet) for _ in range(cols)] for _ in range(rows)]
    return grid

def display_word_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def play_marking_words(rows, cols):
    word_grid = generate_word_grid(rows, cols)
    display_word_grid(word_grid)

    print("\nWelcome to the Marking Words game!")
    print("Mark words in the grid by entering their starting and ending coordinates.")

    while True:
        start_row, start_col = map(int, input("\nEnter starting coordinates (row col): ").split())
        end_row, end_col = map(int, input("Enter ending coordinates (row col): ").split())

        if 0 <= start_row < rows and 0 <= start_col < cols and \
           0 <= end_row < rows and 0 <= end_col < cols and \
           (start_row == end_row or start_col == end_col):
            # Valid coordinates
            marked_word = extract_word(word_grid, start_row, start_col, end_row, end_col)
            print(f"Marked word: {marked_word}\n")
        else:
            print("Invalid coordinates. Please enter valid starting and ending coordinates.")

def extract_word(grid, start_row, start_col, end_row, end_col):
    word = ""

    if start_row == end_row:  # Horizontal
        for col in range(min(start_col, end_col), max(start_col, end_col) + 1):
            word += grid[start_row][col]
    elif start_col == end_col:  # Vertical
        for row in range(min(start_row, end_row), max(start_row, end_row) + 1):
            word += grid[row][start_col]

    return word

# Example usage:
rows = 5
cols = 5
play_marking_words(rows, cols)