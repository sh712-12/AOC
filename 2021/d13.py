from functions import *
from collections import defaultdict
# dictionary = defaultDict(list) makes dictionary with values of type list.


with open('input.txt') as f:
    inn = f.readlines()

inn = [i.strip('\n') for i in inn]

points = set()
lines = set()
for i in inn:
    if 'fold' not in i and i!='':
        # print(len(i.split(',')))
        a,b=i.split(',')
        point = (int(a),int(b))
        points.add(point)
    elif 'fold' in i:
        first_line = i.split('fold along ')[1]
        print(first_line)
        if 'x' in first_line:
            lines.add((int(first_line.strip('x=')),(0)))
        else:
            lines.add(((0),int(first_line.strip('y='))))

print(lines)
# print(points)


def reflect(point,line):
    if line[0]!=0:
        return (2*line[0]-point[0], point[1])
    return (point[0], 2*line[1]-point[1])

total = set()


for pt in points:

    
    # print(pt)
    if first_line[0]!=0:
        #verical line
        if pt[0]>first_line[0]:
            total.add(reflect(pt,first_line))
        else:
            total.add(pt)        

# print(new_points)
print(len(total))