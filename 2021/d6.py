from typing import DefaultDict

with open('input.txt') as f:
    fish = list(f.readline().strip(','))

fish = [int(i) for i in fish if i!=',']
print(fish)
fishage_number = {}

for i in fish:
    if i not in fishage_number:
        fishage_number[i]=0
    fishage_number[i]+=1
print(fishage_number)

for day in range(80):
    x = DefaultDict(int)
    for age in fishage_number.keys():
        number = fishage_number[age]
        if age==0:
            x[6]+=number
            x[8]+=number
        else:
            x[age-1]+=number
    fishage_number = x
print(sum(fishage_number.values()))

    