import random

def get_random_fruit():
    """Return a random fruit from the list."""
    fruit_list = ["Apple", "Banana", "Mango", "Strawberry", "Pineapple"]
    return random.choice(fruit_list)

def get_user_guess():
    """Prompt the user for a single letter and validate the input."""
    guess = input("Please enter a single letter: ")
    return guess if len(guess) == 1 and guess.isalpha() else None

def display_guess_result(guess):
    """Display whether the user's guess is valid or not."""
    if guess:
        print("Good Guess!:", guess)
    else:
        print("Oops! That is not a valid input.")

def main():
    random_fruit = get_random_fruit()
    user_guess = get_user_guess()

    display_guess_result(user_guess)

    # Display the entered letter
    print("You entered:", user_guess)

    # Display randomly selected fruit
    print("Randomly selected fruit:", random_fruit)

if __name__ == "__main__":
    main()
