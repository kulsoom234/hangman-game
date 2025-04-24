import random

# Word list
words = ['enum', 'python', 'colab', 'vscode', 'game', 'hangman', 'script']
word_to_guess = random.choice(words)

guessed_letters = []
attempts = 8

print("Welcome To Hangman Game - Project 8 (GIAIC Quarter 3)!")
print("_" * len(word_to_guess))

# Main game loop
while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter only ONE alphabet.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try a different one!")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Show current word progress
    displayed_word = "".join((letter if letter in guessed_letters else "_" for letter in word_to_guess))
    print("Word: " + displayed_word)

    # Check if the word is fully guessed
    if "_" not in displayed_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
        break
else:
    print(f"\n💀 Game Over! The correct word was: {word_to_guess}")
