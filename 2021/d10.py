from functions import *
from collections import defaultdict

with open('input.txt') as f:
    inn = f.read().split('\n')

ans=0
scores = []
for i in inn:
    s=[]
    for j in i:
        if j in ['(','[','{','<']:
            s.append(j)
        else:
            if j==')':
                if s[-1]=='(':
                    s.pop()
            elif j==']':
                if s[-1]=='[':
                    s.pop()
            elif j=='}':
                if s[-1]=='{':
                    s.pop()
            elif j=='>':
                if s[-1]=='<':
                    s.pop()

    sc=0
    for k in s[::-1]:
        print(k)
        if k=='(':
            sc+=(5*sc+1)
        elif k=='[':
            sc+=(5*sc+2)
        elif k=='{':
            sc+=(5*sc+3)
        elif k=='<':
            sc+=(5*sc+4)

    print(sc)

