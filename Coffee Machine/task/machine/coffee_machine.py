water = 400
milk = 540
bean = 120
cup = 9
money = 550


def info():
    print('The coffee machine has:')
    print(water, ' of water')
    print(milk, ' of milk')
    print(bean, ' of coffee beans')
    print(cup, ' of disposable cups')
    print(money, ' of money')


def choose_action():
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    return action


def buy_action():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - main menu:')
    b = input()
    if b == '1':
        if water >= 250 and bean >= 16 and cup >= 1:
            print('I have enough resources, making you a coffee!')
            buy_espresso()
        elif water < 250:
            print('Sorry, not enough water!')
            return
        elif bean < 16:
            print('Sorry, not enough bean!')
            return
        elif cup < 1:
            print('Sorry, not enough cup!')
            return
    elif b == '2':
        if water < 350 :
            print('Sorry, not enough water!')
            return
        elif milk < 75:
            print('Sorry, not enough milk!')
            return
        elif bean < 20:
            print('Sorry, not enough bean!')
            return
        elif cup < 1:
            print('Sorry, not enough cup!')
        else:
            buy_latte()
    elif b == '3':
        if water < 200 :
            print('Sorry, not enough water!')
            return
        elif milk < 100:
            print('Sorry, not enough milk!')
            return
        elif bean < 12:
            print('Sorry, not enough bean!')
            return
        elif cup < 1:
            print('Sorry, not enough cup!')
            return
        else:
            buy_cappuccino()
    elif b == 'back':
        return


def buy_espresso():
    espresso_water = 250
    espresso_bean = 16
    espresso_cost = 4
    global water
    global bean
    global money
    global cup
    water = water - espresso_water
    bean = bean - espresso_bean
    money = money + espresso_cost
    cup = cup - 1


def buy_latte():
    latte_water = 350
    latte_milk = 75
    latte_bean = 20
    latte_cost = 7
    global water
    global milk
    global bean
    global money
    global cup
    water = water - latte_water
    milk = milk - latte_milk
    bean = bean - latte_bean
    money = money + latte_cost
    cup = cup - 1


def buy_cappuccino():
    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_bean = 12
    cappuccino_cost = 6
    global water
    global milk
    global bean
    global money
    global cup
    water = water - cappuccino_water
    milk = milk - cappuccino_milk
    bean = bean - cappuccino_bean
    money = money + cappuccino_cost
    cup = cup - 1


def fill_action():
    global water
    global milk
    global bean
    global cup
    print('Write how many ml of water do you want to add:')
    x = int(input())
    water = water + x
    print('Write how many ml of milk do you want to add:')
    x = int(input())
    milk = milk + x
    print('Write how many grams of coffee beans do you want to add:')
    x = int(input())
    bean = bean + x
    print('Write how many disposable cups of coffee do you want to add:')
    x = int(input())
    cup = cup + x


def take_action():
    global money
    print('I gave you $', money)
    money = 0


def start():
    while True:
        action = choose_action()
        if action == 'buy':
            buy_action()
        elif action == 'fill':
            fill_action()
        elif action == 'take':
            take_action()
        elif action == 'remaining':
            info()
        elif action == 'exit':
            break

start()