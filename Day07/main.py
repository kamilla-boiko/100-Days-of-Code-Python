import random
import hangman_words
from hangman_art import logo, stages


chosen_dict = random.choice(hangman_words.words)
chosen_word = random.choice(chosen_dict)

end_of_game = False
lives = 6

print(logo)

if chosen_dict == hangman_words.fruits:
    print("You need to guess the word from the Fruits Topic")
elif chosen_dict == hangman_words.vegetables:
    print("You need to guess the word from the Vegetables Topic")
elif chosen_dict == hangman_words.sport:
    print("You need to guess the word from the Sport Topic")
elif chosen_dict == hangman_words.body:
    print("You need to guess the word from the Body Topic")
elif chosen_dict == hangman_words.animals:
    print("You need to guess the word from the Animals Topic")

display = ["_" for _ in range(len(chosen_word))]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
