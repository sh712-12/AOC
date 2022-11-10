from xmlrpc.client import MAXINT


with open('input.txt') as f:
    inn = f.readline()

def sol(inn):
    ans=['']
    for i in inn:
        # print(ans)
        if i.islower():
            if ans[-1]==i.upper():
                ans.pop(-1)
                continue
        elif i.isupper():
            if ans[-1]==i.lower():
                ans.pop(-1)
                continue
        ans+=[i]
    return len(ans)-1

s='abcdefghijklmnopqrstuvwxyz'
l=MAXINT
k = ''
for i in s:
    # c = [k for k in inn if k!=i or k!=i.upper()]
    c = inn.replace(i, '')
    c = c.replace(i.upper(), '')

    # print(i, c)
    a = sol(c)
    if l>a:
        l = a
        k=i
#part 2:
print(l,k)
#part 1:
print(sol(inn))
