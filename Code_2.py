init_water = 400
init_money = 550
init_beans = 120
init_milk = 540
init_cups = 9

print("The coffee machine has:")
print(f"{init_water} of water")
print(f"{init_milk} of milk")
print(f"{init_beans} of coffee beans")
print(f"{init_cups} of disposable cups")
print(f"{init_money} of money")

a = input("Write action (buy, fill, take): ")

def b():
    global init_money
    print(f'I gave you ${init_money}')
    init_money = 0

def c():
    global init_water
    global init_beans
    global init_milk
    global init_cups
    water = int(input("Write how many ml of water do you want to add: "))
    milk = int(input("Write how many ml of milk do you want to add: "))
    beans = int(input("Write how many grams of coffee beans do you want to add: "))
    cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    init_water += water
    init_milk += milk
    init_beans += beans
    init_cups += cups

def d():
    global init_water
    global init_beans
    global init_milk
    global init_cups
    global init_money
    coffee_num = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if coffee_num == 1:
        init_water -= 250
        init_beans -= 16
        init_money += 4
        init_cups -= 1
    elif coffee_num == 2:
        init_water -= 350
        init_milk -= 75
        init_beans -= 20
        init_money += 7
        init_cups -= 1
    elif coffee_num == 3:
        init_water -= 200
        init_milk -= 100
        init_beans -= 12
        init_money += 6
        init_cups -= 1
 
if a == 'take':
    b()
elif a == 'fill':
    c()
elif a == 'buy':
    d()
print("The coffee machine has:")
print(f"{init_water} of water")
print(f"{init_milk} of milk")
print(f"{init_beans} of coffee beans")
print(f"{init_cups} of disposable cups")
print(f"{init_money} of money")
