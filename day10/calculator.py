def to_do1(num1):
    num2 = float(input("What is second number? "))
    print("""+
-
*
/""")
    sym = input("What do you want to do? ")
    n = to_do(num1, num2, sym)
    print(f"{num1} {sym} {num2} = {n}")
    cont = input('Continue calculating? "Yes" or "No" ')
    return num1, cont, sym, num2, n

def to_do(num1, num2, sym):
    if sym == "+":
        return num1 + num2
    elif sym == "-":
        return num1 - num2
    elif sym == "*":
        return num1 * num2
    elif sym == "/":
        return num1 / num2

cont = "Yes"
print("Calculator 2000")
num1 = float(input("What is first number? "))
while cont == "Yes":
    num1, cont, sym, num2, n = to_do1(num1)

print(f"{num1} {sym} {num2} = {n} is final")