from functions import *
from collections import defaultdict
# dictionary = defaultDict(list) makes dictionary with values of type list.

dat=[]
with open('ex.txt') as f:
    for line in f:
        dat.append([int(x) for x in line.strip()])
print(dat)
