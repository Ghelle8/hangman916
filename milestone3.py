import random

def display_success_message(letter):
    print(f"Good guess! {letter} is in the word.")

def display_error_message(letter):
    print(f"Sorry, {letter} is not in the word. Try again.")

def check_guess(secret_word, guess):
    guess = guess.lower()
    if guess in secret_word.lower():
        display_success_message(guess)
        return True
    else:
        display_error_message(guess)
        return False

def generate_secret_word():
    word_list = ["Apple", "Banana", "Mango", "Strawberry", "Pineapple"]
    return random.choice(word_list)

def ask_for_input():
    secret_word = generate_secret_word()

    while True:
        user_guess = input("Please guess a letter: ")
        if check_guess(secret_word, user_guess):
            break

if __name__ == "__main__":
    ask_for_input()
