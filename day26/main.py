import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
data ={row['letter']: row['code'] for (index,row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input('What is your name? ')
bukvi =[letter for letter in name.upper()]
rs = [data[letter] for letter in bukvi if letter in data]
print(rs)