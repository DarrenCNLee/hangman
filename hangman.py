#!/usr/local/bin/python3

import random

words = []
debug = False

def main():
    wordsFile = open("words.txt", "r")
    
    while True:
        line = wordsFile.readline()
        
        if not line:
            break
        
        words.append(line)
        
    wordsFile.close()
    
    solutionWord = words[random.randint(0, len(words) - 1)].rstrip()
    solution = list(solutionWord)
    solLetters = set(solution)
    
    wrongLetters = set()
    wrongGuessesLeft = 6
    
    guessed = ["_" for _ in range(len(solution))]
    
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    if debug:
        print(solution)
    
    while wrongGuessesLeft > 0 and guessed != solution:    
        letter = input("Guess a letter: ").lower()
        
        if len(letter) != 1 or letter not in alphabet:
            print("Please enter one letter.\n")
            print()
            continue
        
        if letter in solLetters:
            for i in range(len(guessed)):
                if solution[i] == letter:
                    guessed[i] = letter
                    
                print(guessed[i] + " ", end = "")
                
            print()
            
        else:
            if letter not in wrongLetters:
                wrongGuessesLeft -= 1
                wrongLetters.add(letter)
            print("\"" + letter + "\" was not in the word.")
            print("Wrong guesses so far:", wrongLetters)
            print("Wrong guesses left: " + str(wrongGuessesLeft))
            
            for i in range(len(guessed)):
                print(guessed[i] + " ", end = "")
            
            print()
            
            match wrongGuessesLeft:
                case 5:
                    print("_____")
                    print("|   |")
                    print("|   O")
                    print("|")
                    print("|")
                case 4:
                    print("_____")
                    print("|   |")
                    print("|   O")
                    print("|   |")
                    print("|")
                case 3:
                    print("_____")
                    print("|   |")
                    print("|   O")
                    print("|  /|")
                    print("|")
                case 2:
                    print("_____")
                    print("|   |")
                    print("|   O")
                    print("|  /|\\")
                    print("|")
                case 1:
                    print("_____")
                    print("|   |")
                    print("|   O")
                    print("|  /|\\")
                    print("|  /")
        
        print("\n")
            
            
    if wrongGuessesLeft > 0:
        print("Congratulations, you guessed the word correctly!")
    else:
        print("Sorry, you took too many turns.")
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / \\")
        print("The word was: " + solutionWord)
            
if __name__ == "__main__":
    main()
