from functions import *
from collections import defaultdict

with open('input.txt') as f:
    inn = f.read().split('\n')
# inn = [ int(i) for i in inn]
# print(inn)

r=0
bs=[0]*3
for i in range(len(inn)):
    for j in range(len(inn[i])):
        p = int(inn[i][j])
        # bs = []
        pright,pleft,pdown,pup = 9,9,9,9
        if j<len(inn[i])-1:
            pright = int(inn[i][j+1])
        if j>0:
            pleft = int(inn[i][j-1])
        if i<len(inn)-1:
            pdown = int(inn[i+1][j])
        if i>0:
            pup = int(inn[i-1][j])
        if p<pright and p<pleft and p<pup and p<pdown:
            lowpoint = p
            r+=(p+1)
            right,left,up,down = [],[],[],[]
            #down
            # down = [int(inn[k][j]) for k in range(i, len(inn)) if int(inn[k][j])!=9]
            for k in range(i, len(inn)):
                if int(inn[k][j])!=9 and int(inn[k][j])!=p:
                    down.append(int(inn[k][j]))
                elif int(inn[k][j])==9:
                    break
            #up
            # up = [int(inn[ok][j]) for ok in range(i,0,-1) if int(inn[ok][j])!=9]
            for ok in range(i,0,-1):
                if int(inn[ok][j])!=9 and int(inn[ok][j])!=p:
                    up.append(int(inn[ok][j]))
                elif int(inn[ok][j])==9:
                    break
            #right
            # right = [int(inn[ad][j]) for ad in range(j,len(inn[i])) if int(inn[ad][j])==9]
            for ad in range(j, len(inn[i])):
                if int(inn[i][ad])!=9 and int(inn[i][ad])!=p:
                    right.append(int(inn[i][ad]))
                elif int(inn[i][ad])==9:
                    break     
            #left
            # left = [int(inn[lad][j]) for lad in range(j,0,-1) if int(inn[lad][j]!=9)]
            for lad in range(j,0,-1):
                if int(inn[i][lad])!=9 and int(inn[i][lad])!=p:
                    left.append(int(inn[i][lad]))
                elif int(inn[i][lad])==9:
                    break 
            print(lowpoint)
            print(right)
            print(left)
            print(up)
            print(down)
            size = len(up) + len(down) + len(right) + len(left) +1
            print(size)
            for g in range(len(bs)):
                if size>bs[g]:
                    bs[g]=size
                    break

print(bs)
ans=1
for ok in bs:
    ans*=ok

print(ans)