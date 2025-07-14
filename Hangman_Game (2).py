import random

# Step 1: Define the list of words
words = ['cherry', 'dog', 'elephant', 'fish', 'grape', 'horse','hangman','CodeAlpha', 'jacket']
word_to_guess = random.choice(words)

# Step 2: Game state variables
guessed_letters = []
tries = 6
display_word = ['_'] * len(word_to_guess)

# Step 3: Game Loop
print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while tries > 0 and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    print(f"Remaining tries: {tries}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("️You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess")
        tries -= 1

# Step 4: Result
if '_' not in display_word:
    print("\n Congratulations! You have guessed the word:", word_to_guess)
else:
    print("\n Game over! The word was:", word_to_guess)
    print("""
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|___
    """)