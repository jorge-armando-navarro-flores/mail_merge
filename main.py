PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_template = letter_file.read()

for name in names:
    new_name = name.strip()
    new_content = letter_template.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as new_letter:
        new_letter.write(new_content)



