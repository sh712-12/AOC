from functions import *
from collections import defaultdict
# dictionary = defaultDict(list) makes dictionary with values of type list.

# dat=[]
# with open('ex.txt') as f:
#     for line in f:
#         dat.append(line.strip('\n'))


xtar = [i for i in range(248,286)]
ytar = [i for i in range(-85,-56)]

def step(x,y,xv,yv):
    x+=xv
    y+=yv
    if x>=0: x-=1
    if x<=0: x+=1
    y-=1
    return x,y

def is_past(x,y):
    if x in xtar and y in ytar:
        return True
    return False

def launch(xv,yv):
    x=0
    y=0
    while x



