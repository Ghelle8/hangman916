# Hangman

## Table of Contents
 [Description](#description)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Navigate to the Project Directory](#navigate-to-the-project-directory)
  - [Create a Virtual Environment (Optional but Recommended)](#create-a-virtual-environment-optional-but-recommended)
  - [Run the Hangman game](#run-the-hangman-game)
- [Usage](#usage)
  - [Word Selection](#word-selection)
  - [User Input and Validation](#user-input-and-validation)
  - [Game Logic](#game-logic)
    - [check_guess(secret_word, guess)](#check_guesssecret_word-guess)
    - [ask_for_input()](#ask_for_input)
- [File Structure](#file-structure)
- [License](#license)

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation

### Prerequisites
Make sure you have the following installed on your system:

- Python (version 3.9.6)

### Clone the Repository
```bash
git clone https://github.com/Ghelle8/Hangman916.git
```
### Navigate to the Project Directory
```bash
cd YourHangmanRepository
```
### Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
```
On Windows:
```bash
.\venv\Scripts\activate
```
On MacOS/Linux:
```bash
source venv/bin/activate
```
### Run the Hangman game
Now you're all set! Start playing the Hangman game by following the instructions in the Usage section.

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
This function checks if the guessed letter is in the word. If the guess is correct, it updates the word_guessed list.
```python
def check_guess(secret_word, guess):
    # Game logic details...
```

#### ask_for_input()
This function contains the game loop, prompting the user for guesses until they run out of lives or successfully guess the word.
``` python
if __name__ == "__main__":
    # Call the ask_for_input function to start the game
    ask_for_input()
```

## File Structure
The files currently used: 
- [milestone5.py]


## License
Apache License
Version 2.0, January 2004

Copyright [year] [author]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
