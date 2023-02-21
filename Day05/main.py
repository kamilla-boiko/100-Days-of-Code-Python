import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
eazy_password = ""
for _ in range(nr_letters):
    eazy_password += random.choice(letters)
for _ in range(nr_symbols):
    eazy_password += random.choice(symbols)
for _ in range(nr_numbers):
    eazy_password += random.choice(numbers)
print(f"Your easy password is: {eazy_password}")

# Hard Level - Order of characters randomised by shuffle
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for _ in range(nr_letters):
    password_list += random.choice(letters)
for _ in range(nr_symbols):
    password_list += random.choice(symbols)
for _ in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

print(f"Your hard password is: {''.join(password_list)}")

# Hard Level - Order of characters randomised while create
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_length = nr_letters + nr_symbols + nr_numbers
count_letters = 0
count_symbols = 0
count_numbers = 0
hard_password = ""
possible_choice = ["letter", "number", "symbol"]

for _ in range(password_length):

    if count_letters >= nr_letters and "letter" in possible_choice:
        possible_choice.remove("letter")
    elif count_numbers >= nr_numbers and "number" in possible_choice:
        possible_choice.remove("number")
    elif count_symbols >= nr_symbols and "symbol" in possible_choice:
        possible_choice.remove("symbol")

    chr = random.choice(possible_choice)

    if chr == "letter":
        count_letters += 1
        hard_password += random.choice(letters)
    elif chr == "number":
        count_numbers += 1
        hard_password += random.choice(numbers)
    elif chr == "symbol":
        count_symbols += 1
        hard_password += random.choice(symbols)

print(f"Your extra hard password is: {hard_password}")
