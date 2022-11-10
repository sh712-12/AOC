from functions import *
from collections import defaultdict

with open('input.txt') as f:
    pos = f.read().split('\n')

#1 4 7 8
outs = []
for i in pos:
    out = i.split(' | ' )[1]
    outs.append(out)

x=0
outs = [outs[i].split() for i in range(len(outs))]


for i in range(len(outs)):
    # a=''
    for j in range(len(outs[i])):

        eight, one, four, seven = '','','',''
        if len(outs[i][j]) == 7:
            eight = permute(outs[i][j])
            top = outs[i][j][3]
            upleft = outs[i][j][2]
            upright = outs[i][j][0]
            middle = outs[i][j][-2]
            downleft = outs[i][j][-3]
            downright = outs[i][j][-1]
            bottom = outs[i][j][1]

        elif len(outs[i][j]) == 2:
            one = permute(outs[i][j])
        elif len(outs[i][j]) == 4:
            four = permute(outs[i][j])
        elif len(outs[i][j]) == 3:
            seven = permute(outs[i][j])



    x+=int(a)
    print(a)

print(x)