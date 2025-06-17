"""
Lichao_Huang
06/15/2025
"""
import random
import os
import time
Command = ('D','d','W','w','Q','q')
Deposit = ('D','d')
Withdrow = ('W','w')
Quit = ('Q','q')
balacne = int(random.randint(-1000,10000))
selection = "D"

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

while selection in Command:
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
    newselection = input(h)
    if newselection in Command:
        selection = newselection
        if selection in Deposit:
            amount = float(input('Enter the transaction amount:'))
            balacne = balacne + amount
            print()
            print('{:^40}'.format(a))
            print(f'{d}{balacne:,.2f}')
            print('{:^40}'.format(a))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        if selection in Withdrow:
            if balacne > 0 :
                amount = float(input('Enter the transaction amount:'))
                if amount < balacne:
                    balacne = balacne - amount
                    print()
                    print('{:^40}'.format(a))
                    print(f'{d}{balacne:,.2f}')
                    print('{:^40}'.format(a))
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print()
                    print('{:^40}'.format(a))
                    print('{:^40}'.format(j))
                    print('{:^40}'.format(a))
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print()
                print('{:^40}'.format(a))
                print('{:^40}'.format(j))
                print('{:^40}'.format(a))
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
        if selection in Quit:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    else:
        print()
        print('{:^40}'.format(a))
        print('{:^40}'.format(i))
        print('{:^40}'.format(a))

