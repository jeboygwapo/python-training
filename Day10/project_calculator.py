def process_output(first_number, next_number, output, operation):
    if operation == 'add':
        return print(f"{first_number} + {next_number} = {output}")
    elif operation == 'subtract':
        return print(f"{first_number} - {next_number} = {output}")
    elif operation == 'multiply':
        return print(f"{first_number} * {next_number} = {output}")
    else:
        return print(f"{first_number} / {next_number} = {output}")
def add(first_number, next_number):
    output = first_number + next_number
    process_output(first_number, next_number, output, "add")
    return output

def subtract(first_number, next_number):
    output = first_number - next_number
    process_output(first_number, next_number, output, "subtract")
    return output

def multiply(first_number, next_number):
    output = first_number * next_number
    process_output(first_number, next_number, output, "multiply")
    return output

def divide(first_number, next_number):
    output = first_number / next_number
    process_output(first_number, next_number, output, "divide")
    return output

def to_continue(first_number):
    while True:
        to_continue = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ").lower()
        if to_continue == 'y':
            return True
        elif to_continue == 'n':
            return False
        else:
            print("Invalid option, please try again.\n")
def process_output(first_number, next_number, output, operation):
    if operation == 'add':
        return print(f"{first_number} + {next_number} = {output}")
    elif operation == 'subtract':
        return print(f"{first_number} - {next_number} = {output}")
    elif operation == 'multiply':
        return print(f"{first_number} * {next_number} = {output}")
    else:
        return print(f"{first_number} / {next_number} = {output}")
def add(first_number, next_number):
    output = first_number + next_number
    process_output(first_number, next_number, output, "add")
    return output

def subtract(first_number, next_number):
    output = first_number - next_number
    process_output(first_number, next_number, output, "subtract")
    return output

def multiply(first_number, next_number):
    output = first_number * next_number
    process_output(first_number, next_number, output, "multiply")
    return output

def divide(first_number, next_number):
    output = first_number / next_number
    process_output(first_number, next_number, output, "divide")
    return output

def to_continue(first_number):
    while True:
        to_continue = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ").lower()
        if to_continue == 'y':
            return True
        elif to_continue == 'n':
            return False
        else:
            print("Invalid option, please try again.\n")

session = True

while True:
    try:
        first_number = int(input("What's the first number?: "))
        break
    except ValueError:
        print("Input not a valid number, please try again.\n")

while session:
    operation = input("+\n-\n*\n/\nPick and operation: ")
    if operation in ['+', '-', '*', '/']:
        while True:
            try:
                next_number = int(input("What's the next number?: "))
                break
            except ValueError:
                print("Input not a valid number, please try again.\n")
        if operation == '+':
            first_number = add(first_number, next_number)
        elif operation == '-':
            first_number = subtract(first_number, next_number)
        elif operation == '*':
            first_number = multiply(first_number, next_number)
        else:
            first_number = divide(first_number, next_number)
        session = to_continue(first_number)
    else:
        print("Invalid input for operation, please try again.\n")
session = True

while True:
    try:
        first_number = int(input("What's the first number?: "))
        break
    except ValueError:
        print("Input not a valid number, please try again.\n")

while session:
    operation = input("+\n-\n*\n/\nPick and operation: ")
    if operation in ['+', '-', '*', '/']:
        while True:
            try:
                next_number = int(input("What's the next number?: "))
                break
            except ValueError:
                print("Input not a valid number, please try again.\n")
        if operation == '+':
            first_number = add(first_number, next_number)
        elif operation == '-':
            first_number = subtract(first_number, next_number)
        elif operation == '*':
            first_number = multiply(first_number, next_number)
        else:
            first_number = divide(first_number, next_number)
        session = to_continue(first_number)
    else:
        print("Invalid input for operation, please try again.\n")
