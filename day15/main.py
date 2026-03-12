inside = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0
}
from menu import menu

play = True

while play:
    choice1 = input(f'What would you like to order "Espresso" "Latte" "Cappuccino" ')
    
    if choice1 == "report":
        print(f"Water: {inside['Water']}ml\nMilk: {inside['Milk']}ml\nCoffee: {inside['Coffee']}g\nMoney: ${inside['Money']}")
        continue
    elif choice1 not in menu:
        print("Unknown drink. Try again.")
        continue
    
    order = choice1
    price = menu[order]['Price']
    water_use = menu[order]['Water']
    coffee_use = menu[order]['Coffee']
    milk_use = menu[order]['Milk']
    
    if inside['Water'] < water_use:
        print("Sorry, not enough water.")
        continue
    elif inside['Coffee'] < coffee_use:
        print("Sorry, not enough coffee.")
        continue
    elif inside['Milk'] < milk_use:
        print("Sorry, not enough milk.")
        continue
    
    print(f"You should pay ${price}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    penny = int(input("How many pennies? "))
    insert = round(quarters*0.25 + dimes*0.10 + nickles*0.05 + penny*0.01, 2)
    print(f"You inserted: ${insert}")
    
    if insert >= price:
        change = round(insert - price, 2)
        
        inside['Water'] -= water_use
        inside['Coffee'] -= coffee_use
        inside['Milk'] -= milk_use
        inside['Money'] += price
        
        print(f"Here is your {order} and your change: ${change}")
    else:
        print(f"Not enough money. Money refunded: ${insert}")