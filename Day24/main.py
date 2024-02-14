with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()


with open("Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()

    for name in names:
        new_letter = content.replace("[name]", name.strip())

        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as named_letter:
            named_letter.write(new_letter)
