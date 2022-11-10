with open('input.txt') as f:
    #separate on empty line
    inn = [i for i in f.read().split('\n\n')]
    print(inn)


s=0
#p1
for i in [i.replace('\n','') for i in inn]:
    s+= len(set(list(k for k in i)))
# print(s)

#p2
g = [i.split('\n')for i in inn]
s=0
for i in g:
    a = set.intersection(*map(set,i))
    # print(len(a))
    s+=len(a)
print(s)