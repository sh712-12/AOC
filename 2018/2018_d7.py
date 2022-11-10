
with open('../input.txt') as f:
    inn = f.readlines()
    steps = [(i.split(' ')[1], i.split(' ')[-3]) for i in inn]
ans=''
s='abcdefghijklmnopqrstuvwxyz'.upper()
print(steps)
for i in range(len(steps)):
    ans+=steps[i][0]
    ok=[]
    for j in steps[i:]:
        if steps[i][0] is j[0]:
            ok+=[j[1]]
    ok = sorted(ok)
    for k in ok:
        if k not in ans:
            ans+=k
            break
    print(steps[i], ok, ans)
print(ans)