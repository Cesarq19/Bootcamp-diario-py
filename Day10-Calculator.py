import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Add
def add(n1,n2):
    return n1+n2
# Substract
def substract(n1,n2):
    return n1 - n2
# Multiply
def multiply(n1,n2):
    return n1 * n2
# Division
def division(n1,n2):
    return n1 / n2

# Create a dictionary called operations with keys (+,-,/,*) and values the operations
operations = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':division
}

op_seguida = True
resultado = 0

while True:
    print(logo)
    first_number = int(input("What's the first number?: "))
    for symbol in operations:
            print(symbol)
    operation_symbol = input("Pick an operation: ")
    next_number = int(input("What's the next number?: "))
    operation = operations[operation_symbol]
    resultado = operation(first_number,next_number)
    print(f"{first_number} {operation_symbol} {next_number} = {resultado}")
    option = input(f"Type 'y' to continue calculating with {resultado}, or type 'n' to start a new calculation: ")
    if option == 'y':
        op_seguida = True
    else:
        op_seguida = False
        os.system("cls")
    while op_seguida:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        next_number2 = int(input("What's the next number?: "))
        number_one = resultado
        operation2 = operations[operation_symbol]
        resultado_nuevo = operation2(resultado,next_number2)
        print(f"{resultado} {operation_symbol} {next_number2} = {resultado_nuevo}")
        option = input(f"Type 'y' to continue calculating with {resultado_nuevo}, or type 'n' to start a new calculation: ")
        if option == 'y':
            op_seguida = True
        else:
            op_seguida = False
            os.system("cls")

