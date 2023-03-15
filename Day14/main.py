from os import system, name
from random import choice

from art import logo, vs
from game_data import data


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_answer() -> str:
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == "A" or answer == "a":
        return "A"
    elif answer == "B" or answer == "b":
        return "B"
    else:
        print("I can't understand your answer. Please, try again.")
        get_answer()


def more_followers(a: int, b: int) -> str:
    if a > b:
        return "A"
    else:
        return "B"


def game():
    print(logo)

    should_continue = True
    score = 0

    a = choice(data)
    b = choice(data)

    while should_continue:
        a = b
        b = choice(data)

        while a == b:
            b = choice(data)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        answer = get_answer()
        winner = more_followers(a["follower_count"], b["follower_count"])

        clear()
        print(logo)

        if answer == winner:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
