


with open('input.txt') as f:
    inn = f.read().split('\n')

three,two=0,0

def count(s,c):
    ans=0
    for i in s:
        if i==c:
            ans+=1
    return ans

def check(str):
    twos=0
    threes=0
    for i in str:
        if count(str, i)==2: twos+=1
        if count(str, i)==3: threes+=1
    if twos>0 and threes>0: return 'both'
    if twos>0: return 'two'
    if threes>0: return 'three'

#part 2:
'''
for i in inn:

    s = check(i)
    if s=='both':
        two+=1
        three+=1
    elif s=='two':
        two+=1
    elif s=='three':
        three+=1

print(two*three)        
'''
#part2:
'''
ans=''
for i in range(len(inn)):
    for j in inn:
        c,k=0,0
        if j!=inn[i] and len(j)==len(inn[i]):
            for k in range(len(j)):
                if inn[i][k]!=j[k]:
                    c+=1
                    pos=k
        if c==1:
            ans = ans+j[:pos]+j[pos+1:]

print(ans)
'''