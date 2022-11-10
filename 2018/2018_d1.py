from re import I


with open('input.txt') as f:
    inn = f.read().split('\n')
inn = [int(i)for i in inn]
#part 1: print(sum(inn))
#part 2:
d={}
s=0
i=0
while 1:
    s+=inn[i]
    if s in d:
        print(s)
        break
    d[s]=1
    i+=1
    if i==len(inn):
        i=0