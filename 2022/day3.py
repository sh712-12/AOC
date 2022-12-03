with open('input.txt') as f:
    inn = [i.strip('\n') for i in f.readlines()]
    inn1 = [[i[:len(i)//2], i[len(i)//2:]] for i in inn]
    inn2 = [inn[i:i+3] for i in range(0,len(inn), 3)]


def common(x):
    common = ''
    for i in x[0]:
        for j in i:
            flag=0
            for k in x[1:]:
                if j in k:
                    flag=1
                else:
                    flag=0
                    break
            if flag: common = j
    return common

def priority(x:str):
    s = 'abcdefghijklmnopqrstuvwxyz'
    prio = {s[i]:i+1 for i in range(len(s))}
    s = s.upper()
    prio.update({s[i]:i+27 for i in range(len(s))})
    return prio[x]


ans=0
for i in inn1:
    ans+=priority(common(i))
#part1:
print(ans)

ans=0
for i in inn2:
    ans+=priority(common(i))
#part2:
print(ans)