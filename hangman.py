# Codigo para juego del Ahorcado, proyecto final del curso de Python intermedio de Platzi.

import random
import os

# Abrimos y leemos el archivo 
def read():
    words = []
    with open("/Users/valenzandoli/Desktop/Data Science/Python intermedio/code/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word.strip().upper())
    return words

def run():
    data = read()
    word = random.choice(data)
    letters = [x for x in word]
    empty_letters = ["_" for x in letters]
    letter_index_dict = {}
    # El enumerate te da las letras y un numero para cada una de las letras que la contiene
    for idx, letter in enumerate(word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("clear")
        print("Adivina la palabra ")
        for element in empty_letters:
            print(element +" ", end = "")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper() # Con strip se le sacan los espacios en blanco y upper la hace mayuscula a la string
        assert letter.isalpha(), "Solo puedes ingresar letras" # El assert se asegura que solo se ingresen letras 

        if letter in letters:
            for idx in letter_index_dict[letter]:
                empty_letters[idx] = letter
        
        if "_" not in empty_letters:
            os.system("clear")
            print("Ganaste, la palabra era", word)
            break




if __name__ == "__main__":
    run()