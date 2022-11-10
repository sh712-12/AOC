from functions import *
from collections import defaultdict
# dictionary = defaultDict(list) makes dictionary with values of type list.


with open('input.txt') as f:
    main = f.readline()
    ins = f.readlines()

ins = [i.strip('\n') for i in ins][1:]
# print(main, ins)
pairs = defaultdict(str)

for i in ins:
    pairs[i[0:2]] = i[-1]
    
def insert(a : str,b : str):
    key = a+b
    jk = pairs[key]
    # ok=''
    return jk

# print(insert('S','O'))


final=main
# final.insert(1,'ok')
# print(final)

for i in range(40):
    A=''
    for j in range(len(final)):
        A+=final[j]
        if j+1<len(final):
            A+=insert(final[j],final[j+1])
    final=A



# print(final)
string = ''.join([i for i in final])
string = string.strip('\n')
print(string)


most=0
least=len(string)
for j in string:

    if string.count(j)>most:
        most=string.count(j)
    if string.count(j)<least:
        least=string.count(j)
print(most-least)
