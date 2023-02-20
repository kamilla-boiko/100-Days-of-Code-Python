import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_choices = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(possible_choices[your_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(possible_choices[computer_choice])

    if your_choice >= 3 or your_choice < 0:
        print("You typed an invalid number, you lose!")
    elif your_choice == 1 and computer_choice == 0:
        print("You win!")
    elif your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif your_choice == 2 and computer_choice == 1:
        print("You win!")
    elif your_choice == computer_choice:
        print("It's a draw")
    else:
        print("You lose")
