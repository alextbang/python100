
### Hangman game

import random

word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from list and assign to variable "chosen_word"
chosen_word = random.choice(word_list)


#Testing code
print(f'Pssst, the solution is "{chosen_word}".')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


# Ask user to guess a letter and assign to varible "guess"
guess = input("Guess a leter: ")

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Check if the lettter the user guessed i son eof the letter in "chosen_word"
for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.