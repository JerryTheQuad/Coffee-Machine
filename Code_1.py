water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
coffee = int(input('Write how many grams of coffee beans the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))

if (water // 200 == cups) or (milk // 50 == cups) or (coffee // 15 == cups):
    print('Yes, I can make that amount of coffee')
elif (water // 200 > cups) and (milk // 50 > cups) and (coffee // 15 > cups):
    a = water // 200
    b = milk // 50
    c = coffee // 15
    d = min(a, b, c)
    print('Yes, I can make that amount of coffee (and even {number} more than that)'.format(number=d - cups))
else:
    a = water // 200
    b = milk // 50
    c = coffee // 15
    d = min(a, b, c)
    print('No, I can make only {number} cup(s) of coffee'.format(number =d))
