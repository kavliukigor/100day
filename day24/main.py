with open('Input/Names/invited_names.txt', 'r')as file:
    names = file.readlines()

with open('Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()

for name in names:
    clean_name = name.strip()
    new_letter = letter.replace('[name]',clean_name)
    with open(f'Output/ReadyToSend/letter_for_{clean_name}.txt', 'w')as file:
        file.write(new_letter)



