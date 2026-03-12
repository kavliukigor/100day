import random

hp = 0
num = random.randint(1, 100)

difficult = input(f"Welcome to number guesser\n The number between 1 and 100\n Choose difficulty 'Easy' or 'Hard' ")
guess = int(input("What is your guess? "))

if difficult == "Hard":
    hp =5
elif difficult == "Easy":
    hp =10

def game(hp, guess, num):
    while hp !=0:
        if guess>num:
            hp -=1
            if hp == 0:
                print(f"You lose, guessed number is {num}")
                return
            print(f"Wrong! You have {hp} hp left")
            print("Guessed number is lower")
            print(f"Your guess is {guess}")
            guess = int(input("What is yout new guess? "))
        elif guess<num:
            hp -=1
            if hp == 0:
                print(f"You lose, guessed number is {num}")
                return
            print(f"Wrong! You have {hp} hp left")
            print(f"Your guess is {guess}")
            print("Guessed number is bigger")
            guess = int(input("What is yout new guess? "))
        if guess == num:
            print(f"You win number is {num}")
            return
        
game(hp, guess, num)    