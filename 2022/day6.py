with open('input.txt') as f:
    inn = f.read()

def repetition(x):
    for i in x:
        if x.count(i)>1: return True
    return False

for i in range(3,len(inn)):
    if not repetition(inn[i-3:i+1]):
        #part1
        print(i+1)
        break


for i in range(12, len(inn)):
    if not repetition(inn[i-13:i+1]):
        #part2
        print(i+1)
        break