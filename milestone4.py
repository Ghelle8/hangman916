import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._get_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _get_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if self._is_guess_in_word(guess):
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self._handle_wrong_guess(guess)

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Please guess a letter: ")

            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self._has_already_tried(guess):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

        self._end_game()

    def _is_guess_in_word(self, guess):
        return guess in self.word.lower()

    def _update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def _handle_wrong_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    def _has_already_tried(self, guess):
        return guess in self.list_of_guesses

    def _end_game(self):
        if self.num_lives == 0:
            print("Sorry, you ran out of lives. Game over!")
        else:
            print("Congratulations! You guessed the word!")

# Testing the Hangman class
if __name__ == "__main__":
    words_to_guess = ["apple", "banana", "orange", "grape", "strawberry"]
    hangman_game = Hangman(words_to_guess)
    hangman_game.ask_for_input()
    print(f"Word to guess: {hangman_game.word_guessed}")
    print(f"Number of unique letters: {hangman_game.num_letters}")
