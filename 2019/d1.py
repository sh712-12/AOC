with open('input.txt') as f:
    inn = [int(i)for i in f.readlines()]
    f.seek(0)
    p1 = [(int(i)//3)-2 for i in f.readlines()]
    ans1 = sum(p1)
print(ans1)

def fuel(n):
    s=0
    while n//3>2:
        n = n//3 - 2
        s+=n
    return s
print(fuel(14))

s = sum([fuel(i) for i in inn])
print(s)