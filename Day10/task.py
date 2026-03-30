#def add():
    


def to_continue():
    while True:
        to_continue = input(f"Type 'y' to continue calculating with output, or type 'n' to start a new calculation: ").lower()
        if to_continue == 'y':
            return True
        elif to_continue == 'n':
            return False
        else:
            print("Invalid option, please try again.\n")

session = True

while session:
    try:
        first_number = int(input("What's the first number?: "))
        operation = input("+\n-\n*\n/\nPick and operation: ")
        if operation in ['+', '-', '*', '/']:
            next_number = int(input("What's the next number?: "))
            session = to_continue()
        else:
            print("Invalid input for operation, please try again.\n")
    except ValueError:
        print("Input not a valid number, please try again.\n")
