from functions import *
from collections import defaultdict
# dictionary = defaultDict(list) makes dictionary with values of type list.

dat=[]
with open('ex.txt') as f:
    for line in f:
        dat.append(line.strip('\n'))

# print(dat)

ok = {'0000':'0', '0001':'1', '0010':'2', '0011':'3','0100':'4','0101':'5', '0110':'6', '0111':'7',
    '1000':'8',
    '1001':'9',
    '1010':'A',
    '1011':'B',
    '1100':'C',
    '1101':'D',
    '1110':'E',
    '1111':'F'}

hex = {'0':'0000', '1':'0001', '2':'0010', '3':'0011','4':'0100','5':'0101', '6':'0110', '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'}

H = ''
for i in dat[0]:
    H+=hex[i]
print(H)

v=0

def decode(a:str):
    
    global v
    ver = '0'+a[0:3]
    v+=int(ok[ver])
    type = int(ok['0'+a[3:6]])
    print(ver)
    
    if type==4:
    
        b=a[6:11]
        # print(b)
        for i in range(6,len(a[6:]),5):
            if b[0]=='0':
                break
            else:
                b=a[i:i+5]
                next = a[i+5:]
                letter = ok[b[1:5]]
                # print(letter)
        return decode(next)
    
    else:
    
        lID = a[6]
        if lID=='0':
            packet = a[7:22]
            L = int(packet,2)
            # print(L)
            next = a[22+L:]
        # print(next.lstrip('0'))
            return decode(next.lstrip('0'))
        if lID=='1':
            packet = a[7:18]


decode(H)
print(v)








