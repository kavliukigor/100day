# import turtle

# jora = turtle.Turtle()
# jora.shape("turtle")
# jora.color("DarkBlue")
# jora.forward(50)

# screen = turtle.Screen()


# screen.exitonclick()

from re import L
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Type', ['Electric', 'Fire', 'Water', 'Earth', 'Void'])
table.add_column('Name', ['Pickachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Rock'])
table.align = 'l'

print(table)