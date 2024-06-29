from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
# menuitemm = MenuItem()
resources = CoffeeMaker()
money = MoneyMachine()

resources.report()
money.report()

while 1<2:
    # print("What would you like? (" + items.get_items() + ")")
    userchoice = input(f"What would you like? ({items.get_items()})")
    if userchoice == "report":
        print("Here are the current resources: ")
        print(resources.report())
        print(money.report())
    elif userchoice == "off":
        break
    else:
        drink =  items.find_drink(userchoice)
        if resources.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                resources.make_coffee(drink)







