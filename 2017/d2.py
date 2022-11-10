with open('../input.txt') as f:
    inn = f.readlines()
    rows = [i.split() for i in inn]
    for i in rows:
        i = [int(j)for j in i]
    print(rows)

