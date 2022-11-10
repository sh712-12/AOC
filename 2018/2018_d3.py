


with open('input.txt') as f:
    inn = f.read().split('\n')
dat=[]
for i in inn:
    a=i.split(' ')[2:]
    b=[a[0].strip(':').split(','), a[1].split('x')]
    c=[]
    for i in b:
        for j in i:
            c+=[int(j)]
    
    dat.append(c)

#part 1:
'''
covered=set()
common=set()

def cover(x,y,l,b):
    ycord = 1000-y
    topright = (x,ycord)
    for i in range(l):
        for j in range(b):
            point = (x+i, ycord-j)
            if point in covered: 
                common.add(point)
            covered.add(point)

for i in dat:
    cover(i[0],i[1],i[2],i[3])

print(len(common))
'''

#part 2:
'''
claimed = set()

def points(x,y,l,b, c=0):
    p=set()
    ycord=1000-y
    for i in range(l):
        for j in range(b):
            point = (x+i, ycord-j)
            if not c:
                claimed.add(point)
            p.add(point)
    return p

# make dictionary of every point covered : how many times covered
# if a point is covered only once, it has no overlap

for i in dat:
    points(i[0],i[1],i[2],i[3])  #add all claimed points to set claimed

p={}
for i in claimed:
    p[i] = 0 #set all points in dictionary to value 0

for i in dat:
    po = points(i[0],i[1],i[2],i[3], c=1)
    for j in po:
        p[j]+=1 #increment point value how many times it is occupied

ok=set()
for j in p:
    if p[j]==1:
        ok.add(j) #create set with points having values 1
j=1

for i in range(len(dat)):
    ps = points(dat[i][0],dat[i][1],dat[i][2],dat[i][3])
    if all([i in ok for i in ps]): print(i+1) # if all points if the claim have value 1 (i,e are in set ok), they are not overlapped but any other claim
'''