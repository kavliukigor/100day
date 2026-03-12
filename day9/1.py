bidders = {}
print("Welcome to the secret auction")

def bidd():
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders[name] = bid
    return input("Any other bidders? 'Yes' or 'No' ")
next_bid = 'Yes'

while next_bid == 'Yes':
    next_bid = bidd()

win = max(bidders, key=bidders.get)

print(f"The winner is {win} with bet {bidders[win]}")