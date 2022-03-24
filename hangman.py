# Hangman game code for the Intermediate Python Platzi's course.

import random
import os

# Opening and reading the file
def read():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word.strip().upper())
    return words

def run():
    data = read()
    word = random.choice(data)
    letters = [x for x in word]
    empty_letters = ["_" for x in letters]
    letter_index_dict = {}
    # enumerate gives you the letters and a number for each letter that contains it
    for idx, letter in enumerate(word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("clear")
        print("Guess the word! ")
        for element in empty_letters:
            print(element +" ", end = "")
        print("\n")

        letter = input("Enter a letter: ").strip().upper() # strip takes the gaps out, upper makes every letter uppercase
        assert letter.isalpha(), "You can only enter letters" # The assert statement makes sure that you only enter letters 

        if letter in letters:
            for idx in letter_index_dict[letter]:
                empty_letters[idx] = letter
        
        if "_" not in empty_letters:
            os.system("clear")
            print("Congratulations! You won, the word was: ", word)
            break




if __name__ == "__main__":
    run()
