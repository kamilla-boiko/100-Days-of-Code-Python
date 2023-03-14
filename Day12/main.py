from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ | |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("You answer is not clear, sorry!")
        return

    chosen_number = randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))

        if number < chosen_number:
            print("Too low.")
        elif number > chosen_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {chosen_number}.")
            return

        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


game()
