from functions import *
from collections import defaultdict

with open('input.txt') as f:
    inn = f.read().split('\n')
dat = [i.split('-') for i in inn]
# print(dat) 
visited = []
adj = defaultdict(list)

for a,b in dat:
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

ans=0
def s(cave : str):
    global ans
    # print(cave)
    if cave=='end':
        ans+=1
        return
    if cave.islower() and cave in visited:
        return
    
    if cave.islower():
        visited.append(cave)

    for nbr in adj[cave]:
        if nbr=='start':
            continue
        # print(nbr)
        s(nbr)
    if cave.islower():
        visited.remove(cave)

s('start')
print(ans)