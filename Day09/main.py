import replit


logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
should_continue = "yes"

while should_continue.lower() == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    replit.clear()  # to clear the output in the console

winner_name = ""
winner_bid = 0

for key, value in bidders.items():
    if value > winner_bid:
        winner_bid = value
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${winner_bid}")
