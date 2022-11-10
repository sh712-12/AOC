from os import linesep
from functions import *
from collections import defaultdict

with open('input.txt') as f:
    inn = f.readlines()
inn = [i.strip('\n') for i in inn]

step=0
flashes=0
lvls = []
for line in range(len(inn)):
    # print(inn[line])
    lvls.append([int(i) for i in inn[line].strip()])

ans=0
def flash(l,i,c):
    global ans
    ans+=1
    l[i][c]=-1
    for rr in [-1,0,1]:
        for jj in [-1,0,1]:
            ok = i+rr
            ko = c+jj
            if ok>=0 and ok<len(lvls) and ko<len(lvls[i]) and lvls[ok][ko]!=1:
                lvls[ok][ko]+=1
                if lvls[ok][ko]==10:
                    flash(lvls,ok,ko)


for t in range(100):
    for i in range(len(lvls)):
        for c in range(len(lvls[i])):
            lvls[i][c]+=1
        if lvls[i][c]==10:
            flash(lvls,i,c)
    for i in range(len(lvls)):
        for j in range(len(lvls[i])):
            if lvls[i]
        
print(ans)