money = int(input())

tax = 0
percentage = 0
if 0 <= money <= 15527:
    percentage = 0
    tax = money * 0.0
elif 15528 <= money <= 42707:
    percentage = 15
    tax = money * 0.15
elif 42708 <= money <= 132406:
    percentage = 25
    tax = money * 0.25
elif money >= 132407:
    percentage = 28
    tax = money * 0.28

calculated_tax = round(tax)

print('The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.format(income = money, percent = percentage,calculated_tax = calculated_tax))