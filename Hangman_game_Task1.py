## Hangman_Game

import random

print("Welcome to Hangman Game")
print("-----------------------------------------------------------------------------------------------------------------")

words = ["day","date", "homework", "apple", "joker","testy","blue", "good", "likehood","fig","grap", "playing"]

random_word = random.choice(words)

for x in random_word:
    print("_", end=" ")
def print_hangman_game(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1): 
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")

def printword(guess_letters):
    counter=0
    right_letters=0
    for char in random_word:
        if(char in guess_letters):
            print(random_word[counter], end=" ")
            right_letters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return right_letters

def printlines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
        
    letter_guess = input("\nGuess a letter: ")
    
    if(random_word[current_guess_index] == letter_guess):
        print_hangman_game(amount_of_times_wrong)
        
        current_guess_index+=1
        current_letters_guessed.append(letter_guess)
        current_letters_right = printword(current_letters_guessed)
        printlines()
        
        
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letter_guess)

        print_hangman_game(amount_of_times_wrong)

        current_letters_right = printword(current_letters_guessed)
        printlines()

print(end="\n")

print("Game is over! Thank you for playing...")