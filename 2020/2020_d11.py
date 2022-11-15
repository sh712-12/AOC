with open('input.txt') as f:
    inn = [i.strip('\n') for i in f.readlines()]
# print(inn)
def get_adjacent(col, row, data):
    adj=[]
    if row>0:
        adj.append(data[row-1][col]) #up
    if row+1 < len(data):
        adj.append(data[row+1][col]) #down
    if col>0:
        adj.append(data[row][col-1]) #left
    if col+1<len(data[0]):
        adj.append(data[row][col+1]) #right
    
    if row>0 and col>0:
        adj.append(data[row-1][col-1]) #up left
    
    if row+1<len(data) and col+1<len(data[0]):
        adj.append(data[row+1][col+1]) #down right
    
    if row>0 and col+1<len(data[0]):
        adj.append(data[row-1][col+1]) #up right
    
    if row+1 < len(data) and col>0:
        adj.append(data[row+1][col-1]) #down left

    #adj = ['up', 'down', 'left', 'right', 'up left', 'down right', 'up right', 'down left']
    return adj

def resolve(data, adjacentFunction, tolerance):
    old = data
    new = []
    for i in range(len(old)):
        newrow = ''
        for j in range(len(old[i])):
            adj = get_adjacent(j, i, old)
            if old[i][j]=='L' and '#' not in adj:
                newrow+='#'
            elif old[i][j]=='#' and adj.count('#')>=tolerance:
                newrow+='L'
            else:
                newrow+=old[i][j]
        new.append(newrow)

    return new

old = inn
new = resolve(old, get_adjacent, tolerance=4)
while old!=new:
    old = new
    new = resolve(old, get_adjacent, tolerance=4)
#part 1:
print(len([i for j in new for i in j  if i=='#']))

#part 2:
def first_seats(col, row, data):
    pass 
