"""
Lichao_Huang
06/15/2025
"""
import random
Deposit = ['D','d']
Withdrow = ['W','w']
Quit = ['Q','q']
balacne = int(random.randint(-1000,10000))

a = "****************************************"
b = "PIXELL RIVER FINANCIAL"
c = "ATM Simulator"
d = " Your current balance is:$"
e = "Deposit: D"
f = "Withdraw: W"
g = "Quit: Q"

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
