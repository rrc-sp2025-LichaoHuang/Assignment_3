"""
Lichao_Huang
06/15/2025
"""

from pprint import pprint
data = {}
with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('|')
        data[key] = float(value)
print(data)
pprint(data)