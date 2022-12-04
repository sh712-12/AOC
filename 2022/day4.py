with open('input.txt') as f:
    inn = [i.strip('\n')for i in f.readlines()]

def fulloverlap(x,y):
    x = x.split('-')
    y = y.split('-')
    if int(x[0])>=int(y[0]) and int(x[1])<=int(y[1]):
        return True

def overlap(x,y):
    x = [int(i) for i in x.split('-')]
    y = [int(i) for i in y.split('-')]
    for i in range(x[0], x[1]+1):
        if i in range(y[0],y[0]+1):
            return True

ans=0
ans2=0

for i in inn:
    n = i.split(',')
    x,y = n[0],n[1]
    if overlap(x,y) or overlap(y,x):
        ans2+=1
    if fulloverlap(x,y) or fulloverlap(y,x):
        ans+=1

#part1
print(ans)
#part2
print(ans2)