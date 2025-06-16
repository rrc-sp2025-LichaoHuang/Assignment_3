"""
Lichao_Huang
06/15/2025
"""
import random
Command = ('D','d','W','w','Q','q')
Deposit = ('D','d')
Withdrow = ('W','w')
Quit = ('Q','q')
balacne = int(random.randint(-1000,10000))


a = "****************************************"
b = "PIXELL RIVER FINANCIAL"
c = "ATM Simulator"
d = " Your current balance is:$"
e = "Deposit: D"
f = "Withdraw: W"
g = "Quit: Q"
h = "Enter your selection:"
i = "INVALID SELECTION"
j = "INSUFFICIENT FUNDS"

print('{:^40}'.format(a))
print('{:^40}'.format(b))
print('{:^40}'.format(c))
print()
print('{:^40}'.format(f'{d}{balacne:,.2f}'))
print()
print('{:^40}'.format(e))
print('{:^40}'.format(f))
print('{:^40}'.format(g))
print('{:^40}'.format(a))

selection = input(h)
while selection in Command:
    if selection in Deposit:
        amount = float(input('Enter the transaction amount:'))
        balacne = balacne + amount
        print()
        print('{:^40}'.format(a))
        print(f'{d}{balacne:,.2f}')
        print('{:^40}'.format(a))
    if selection in Withdrow:
        if balacne > 0 :
            amount = float(input('Enter the transaction amount:'))
            if amount < balacne:
                balacne = balacne - amount
                print()
                print('{:^40}'.format(a))
                print(f'{d}{balacne:,.2f}')
                print('{:^40}'.format(a))
            else:
                print()
                print('{:^40}'.format(a))
                print('{:^40}'.format(j))
                print('{:^40}'.format(a))
        else:
            print()
            print('{:^40}'.format(a))
            print('{:^40}'.format(j))
            print('{:^40}'.format(a))
    if selection in Quit:
        break