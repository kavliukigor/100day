import random

live = 5

print("Welcome to hangman")

words = ["crocodile", "giraffe", "hippopotamus"]

guess_word = random.choice(words)

placeholder = ""

dov = len(guess_word)

for let in range(0, dov):
    placeholder += "_ "
print(placeholder)

correct_letters = []
game_over = False

while game_over == False:
    guess = input("Guess your letter ").lower()
    correct_letters.append(guess)

    display = ""
    for letter in guess_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if "_" not in display:
        game_over = True
        print("Win")
    
    if guess not in guess_word:
        live -= 1
        print("-1 Hp")
    
    if live == 0:
        print("Lose")
        game_over = True