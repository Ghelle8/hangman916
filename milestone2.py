import random 
word_list = ["Apple", "Banana", "Mango", "Strawberry", "Pineapple"]

word = random.choice(word_list)
# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Check if the input is a single letter and alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!:", guess)
else:
    print("Oops! That is not a vaild input.")

# Display the entered letter
print("You entered:", guess)

print("Randomly selected word:", word)