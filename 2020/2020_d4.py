from functions import *
from collections import defaultdict

with open('input.txt') as f:
    inn = f.read().split('\n\n')
inn = [i for i in inn]
print(inn)
passes=[]
for i in inn:
    a=i.split()
    print(a)
    passes.append(a)

n=0
for k in passes:
    # byr,iyr,eyr,hgt,hcl,ecl,pid=False,False,False,False,False,False,False
    valids = {}
    valids.fromkeys(['byr','iyr','eyr','hgt','hcl','ecl','pid'], [False]*7)
    valid=0
    for j in k:
        if j.split(':')[0]!='cid':
            valids[j.split(':')[0]] = True
    
    # if len(valid)==7:
    #     if (valid['byr'] in [str(i) for i in range(1920,2003)]) and (valid['iyr'] in [str(i) for i in range(2010,2021)]) and (valid['eyr'] in [str(i) for i in range(2020,2031)]) and ()



    else:
        valid=0

    if valid:
        n+=1
print(n)