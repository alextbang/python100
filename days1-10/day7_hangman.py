
### Hangman game

import random

word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from list and assign to variable "chosen_word"
chosen_word = random.choice(word_list)

# Testing code
# print(f'Pssst, the solution is "{chosen_word}".')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a leter: ").lower()

    # Check if the lettter the user guessed is one of the letter in "chosen_word"
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    print(display)

    if "_" not in display:
        end_of_game =True
        print("You win!")