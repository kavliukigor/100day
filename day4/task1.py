import random


print('Welcome to password generator')

num_let = input("How many lettersr do you want? ")
num_zif = input("How any numbers? ")
num_sym = input("How many symbols?") 

password_list = []

for leter in letters.range(0, num_let + 1):
    password_list += random.choice(letters)

for zifra in zifri.range(0, num_zif + 1):
    password_list += random.choice(zifri)

for symbol in symbols.range(0, num_sym + 1):
    password_list += random.chice(symbols)

random.shufle(password_list)

print(password_list)

