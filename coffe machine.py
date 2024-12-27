# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
import time

userinput = ""
suminserted = 0
report = {
    "Water": 5000,
    "Milk": 1000,
    "Coffee": 500,
    "Money": 0
}
def order():
    return input("What would you like? Every coffee is $2.5 (espresso/latte/cappuccino): ")

def check(water, milk, coffee):
    for i in report.keys():
        if i == "Water" and report[i] < water:
            return False
        if i == "Coffee" and report[i] < coffee:
            return False
        if i == "Milk" and report[i] < milk:
            return False
    return True

def money():
    return  float(input("enter some money: "))

def coffeemaker():
    print("making your coffee")
    time.sleep(5)
    print("you can take your coffee out")

while True:
    userinput = order()
    if userinput.lower() == "off":
        break
    elif userinput.lower() == "report":
        print(report)
    elif userinput.lower() == "espresso" or userinput.lower() == "latte" or userinput.lower() == "cappuccino":
        print(f"your order is: {userinput}")
    else:
        print("invalid prompt")
    if userinput.lower() == "espresso" and check(15,10,8)==True:
        moneyentered = money()
        if moneyentered == 2.5:
            coffeemaker()
            report["Water"] -= 15
            report["Milk"] -=10
            report["Coffee"] -= 8
            report["Money"] += 2.5
        elif moneyentered > 2.5:
            coffeemaker()
            print(f"here is the change ${moneyentered-2.5}")
            report["Water"] -= 15
            report["Milk"] -=10
            report["Coffee"] -= 8
            report["Money"] += 2.5
        else:
            print("you dont have enough money your money has been refunded")
    elif check(15,10,8)==False:
        print("there aren't enough recources please try again later")
    if userinput.lower() == "latte" and check(0,150,23) == True:
        moneyentered = money()
        if moneyentered == 2.5:
            coffeemaker()
            report["Water"] -= 15
            report["Milk"] -=10
            report["Coffee"] -= 8
            report["Money"] += 2.5
        elif moneyentered > 2.5:
            coffeemaker()
            print(f"here is the change ${moneyentered-2.5}")
            report["Water"] -= 0
            report["Milk"] -=150
            report["Coffee"] -= 23
            report["Money"] += 2.5
        else:
            print("you dont have enough money your money has been refunded")

    elif check(15,10,8)==False:
        print("there aren't enough recources please try again later")
    if userinput.lower() == "cappuccino" and check(15,20,65) == True:
        moneyentered = money()
        if moneyentered == 2.5:
            coffeemaker()
            report["Water"] -= 15
            report["Milk"] -=10
            report["Coffee"] -= 8
            report["Money"] += 2.5
        elif moneyentered > 2.5:
            coffeemaker()
            print(f"here is the change ${moneyentered-2.5}")
            report["Water"] -= 15
            report["Milk"] -=20
            report["Coffee"] -= 65
            report["Money"] += 2.5
        else:
            print("you dont have enough money your money has been refunded")
    elif check(15,10,8)==False:
        print("there aren't enough recources please try again later")