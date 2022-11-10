with open('input.txt', 'r') as f:
    inn = [i.strip('\n') for i in f.readlines()]


def down(l): return l[0:len(l)//2]
def up(l): return l[len(l)//2:]
idd = []
for i in inn:
    row = list(range(0,128))
    col = list(range(0,8))
    for j in i[:-3]:
        if j=='F': row = down(row)
        else: row = up(row)
    row = row[0]
    for j in i[-3:]:
        if j=='R': col = up(col)
        else: col = down(col)
    col = col[0]
    print(row, col)
    idd.append(row*8 + col)

print(max(idd))

#p2
sortedIDs = sorted(idd)
print(list(set(range(sortedIDs[0], sortedIDs[-1]))-set(sortedIDs)))