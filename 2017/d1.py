with open('../input.txt') as f:
    inn = f.readline()
    inn = [int(i) for i in inn]
#part 1: 
s=0
for i in range(len(inn)-1):
    if inn[i] == inn[i-1]:
        print(inn[i], inn[i-1])
        s+=(inn[i])
    
print(s)

#part 2: 
s=0
for i in range(len(inn)-1):
    if inn[i] == inn[i - len(inn)//2]:
        print(inn[i], inn[i-1])
        s+=(inn[i])
print(s)