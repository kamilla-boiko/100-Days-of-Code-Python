# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    more_cards = True
    while more_cards:
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if calculate_score(user_cards) == 0:
            more_cards = False
        elif calculate_score(user_cards) > 21:
            more_cards = False
        else:
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == "y":
                user_cards.append(deal_card())
            else:
                more_cards = False

    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, "
          f"final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, "
          f"final score: {computer_score}")

    final_result = compare(
        user_score,
        computer_score
    )
    print(final_result)


play = True

want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if want_play == "y":
    while play:
        print(logo)
        game()
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_again == "y":
            clear()
        else:
            play = False
