# Hangman

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation

## Usage
### Word Selection
The computer selects a random word from a predefined list of fruits:
```python
import random

word_list = ["Apple", "Banana", "Mango", "Strawberry", "Pineapple"]
word = random.choice(word_list)

```
### User Input and Validation

The user is prompted to enter a single letter, and the input is validated to ensure it is a valid single alphabetical character.
```python
# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Check if the input is a single letter and alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!:", guess)
else:
    print("Oops! That is not a valid input.")

# Display the entered letter
print("You entered:", guess)
```
### Game Logic

The game logic is encapsulated in functions. The check_guess function checks if the guessed letter is in the word, and the ask_for_input function handles the user input and game loop.

#### check_guess(secret_word, guess)
Describe the details of the game logic here...

#### ask_for_input()
Describe the details of the game loop here...
``` python
if __name__ == "__main__":
    # Call the ask_for_input function to start the game
    ask_for_input()
```

## File Structure
Two files currently used: 
- [milestone2.py]
- [milestone3.py]


## License
