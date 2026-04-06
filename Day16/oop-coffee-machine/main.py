from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

def main():
    is_on = True

    while is_on:
        choice = input(f"What would you like? ({Menu.get_items()}): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            CoffeeMaker.report()
            MoneyMachine.report()
        else:
            if Menu.find_drink(choice):
                drink = Menu.find_drink(choice)
                if CoffeeMaker.is_resource_sufficient(drink):
                    if MoneyMachine.make_payment(drink.cost):
                        CoffeeMaker.make_coffee(drink)






if __name__ == "__main__":
    main()