with open('input.txt') as f:
    inn = [i.strip('\n') for i in f.readlines()]
    rows = [list(map(int, i.split())) for i in inn]
ans=0
for i in rows:
    ans += max(i)-min(i)
print(ans)

#part2
ans2=0
for i in rows:
    for j in i:
        for k in i:
            if j!=k and k%j==0:
                ans2+=(k//j)
                break

print(ans2)