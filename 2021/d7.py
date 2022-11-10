from typing import DefaultDict

with open('input.txt') as f:
    pos = f.readlines()

pos = pos[0].split(',')
pos = [int(i) for i in pos]
print(pos)
fuels = [0]*len(pos)
print(fuels)
for i in range(len(pos)):
    final = pos[i]
    for j in pos:
        a=j
        if j!=final:
            if a>=final:
                diff = a-pos[i]
                fuels[i]+=(diff/2 *(2+(diff-1)))
            elif a<=final:
                diff = final-a
                fuels[i]+=(diff/2 *(2+(diff-1)))

print(min(fuels))


