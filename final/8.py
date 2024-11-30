
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
action = input("Enter action [+-*/]: ")
while action not in ['-', '+', '/', '*']:
    action = input("Enter action [+-*/]: ")

if action == "-":
    print(number_1 - number_2)
elif action == "+":
    print(number_1 + number_2)
elif action == "*":
    print ( number_1 * number_2 )
elif action == "/":
    if number_2 == 0:
        print("Ділення на нуль")
    else:
        print(number_1 / number_2)
