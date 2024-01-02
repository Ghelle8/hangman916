import random

def check_guess(secret_word, guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word.lower():
        # Step 4: If the guess is in the word, print a success message
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        # Step 5: If the guess is not in the word, print an error message
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    # Step 1: Generate a random secret word
    word_list = ["Apple", "Banana", "Mango", "Strawberry", "Pineapple"]
    secret_word = random.choice(word_list)

    while True:
        # Step 2: Move the code for getting user input into this function block
        guess = input("Please guess a letter: ")

        # Step 3: Call the check_guess function to check if the guess is in the word
        if check_guess(secret_word, guess):
            break

if __name__ == "__main__":
    # Step 4: Call the ask_for_input function to test your code
    ask_for_input()
