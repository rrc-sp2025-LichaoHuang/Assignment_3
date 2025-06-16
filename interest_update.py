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
pprint(data)

for key,value in data.items():
    if value < 0:
        value = (value*1.1/12) + value
        print(value)
        data[key] = value
    if value == 0:
        data[key] = value
    if 0 < value < 1000:
        value = (value*1.01/12) + value
        data[key] = value
    if 1000 <= value < 5000:
        value = (value*1.025/12) + value
        data[key] = value
    if 5000 <= value:
        value = (value*1.05/12) + value
        data[key] = value


data["Account"] = ["Balance"]
pprint(data)
