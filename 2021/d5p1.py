with open('input.txt') as f:
    con = f.read()

input = con.split('\n')
input = [input[i][0]+input[i][2]+input[i][7]+input[i][9] for i in range(len(input))]
startx = [int(input[i][0]) for i in range(len(input))]
starty = [int(input[i][1]) for i in range(len(input))]
endx = [int(input[i][-2]) for i in range(len(input))]
endy = [int(input[i][-1]) for i in range(len(input))]

xcords = max(max(startx), max(endx))
ycords = max(max(starty), max(endy))
# print(xcords,ycords)
grid = [(i,j) for i in range(xcords+1) for j in range(ycords+1)]
# print(grid)
# print(startx)
p=0
pcoverd=[]
for i in range(10):
    if startx[i]==endx[i] or starty[i]==endy[i]:
        if startx[i]==endx[i]:
            pcoverd.append(tuple((startx[i],j) for j in range(min(starty[i],endy[i]),max(starty[i],endy[i])+1)))
        else:
            pcoverd.append(tuple((j,starty[i]) for j in range(min(startx[i],endx[i]),max(startx[i],endx[i])+1)))