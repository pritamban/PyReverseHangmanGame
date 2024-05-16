#Pritam Ban
#COSI 10a Spring 2023
#Programming Assignment 4
#Description: Reverse Hangman game where the computer tries to guess the letters in the word
#             User tells the computer how many letters the word contains
#             Uses psuedorandom functions to make guesses 

import random

guessed = []

def banner():
    """To create the banner of the game when the program first boots up"""

    print("This program plays a game of reverse hangman")
    print("You think up a word (by typing it on the computer) and I'll try to guess")
    print("the letters")
    print()

def hangmanArt(wrongGuess, guessedLetters, numLetters, guessLetter):
    """Prints different banner art depending on how many guesses the computer has gotten wrong"""

    if wrongGuess == 0:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  ")
        print(" |  ")
        print(" |  ")
        print(" |  ")
        print(" +-----")
        print()
        print()
    elif wrongGuess == 1:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" |  ")
        print(" |  ")
        print(" |  ")
        print(" +-----")
        print()
        print()
    elif wrongGuess == 2:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" |  |")
        print(" |  ")
        print(" |  ")
        print(" +-----")
        print()
        print()
    elif wrongGuess == 3:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" |  |")
        print(" |   \\")
        print(" |  ")
        print(" +-----")
        print()
        print()
    elif wrongGuess == 4:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" |  |")
        print(" | / \\")
        print(" |  ")
        print(" +-----")
        print()
        print()
    elif wrongGuess == 5:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" |  |\\")
        print(" | / \\")
        print(" |  ")
        print(" +-----")
        print()
        print()
    
    if wrongGuess != 6:
        print("I've got ", guessedLetters, " of the ", numLetters, " letters so far")
        print("I guess: ", guessLetter)

    if wrongGuess == 6:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" | /|\\")
        print(" | / \\")
        print(" |  ")
        print(" +-----")
        print()
        print()
        print("You beat me this time")
        
def guessLetterIV():
    """Validates the input of the 'is the letter in your word' prompt, makes sure it is yes or no """

    val = input("Is that the letter in the word? ")
    while val != "y" and val != "n":
        val = input("Please enter 'y' or 'n'")
    return val

def computerLetterGuess():
    """Function for the computer to guess a letter, provides a list and
    sends in a guess that does not include the letters it has already guessed"""

    alphabet = ['a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']

    i = random.randint(0, len(alphabet)-1)

    while i in guessed:
        i = random.randint(0, len(alphabet)-1)
    
    guessed.append(i)
    # print(guessed)

    return alphabet[i]

def main():
    """Main function, executes all the code and has a while true loop to keep the game going until the loop breaks"""

    computerWrongGuess = 0
    guessedLetters = 0
    string = ''
    
    banner()
    numLetters = int(input("How many letters are in your word? "))
    guessWord = input("Please enter the word for me to guess (letters only): ")
    dashList = [" - "] * numLetters
    wordStringList = [0] * numLetters

    for i in range(numLetters):
        wordStringList[i] = guessWord[i]
    print()
    print (string.join(dashList))

    dashList = [" - "] * numLetters

    while True:
        guessLetter = computerLetterGuess()

        hangmanArt(computerWrongGuess, guessedLetters, numLetters, guessLetter)

        val = guessLetterIV()
        if val == 'n':

            computerWrongGuess += 1
        elif val == 'y':

            numberOfLettersInTheWord = input("How many of that letter are in the word? ")
            guessedLetters += int(numberOfLettersInTheWord)
            for i in range(len(guessWord)-1):
                if str(wordStringList[i]) == guessLetter:
                    dashList[i] = guessLetter
        print()
        print (string.join(dashList))

        if guessedLetters == numLetters:
            print("YOU WIN!")
        
main()
