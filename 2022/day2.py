with open('input.txt') as f:
    inn = [i.strip('\n').split(' ') for i in f.readlines()]

def outcome(p1, p2):
    n = {'A':'X', 'B':'Y', 'C':'Z'}
    if n[p2]==p1: return 3,'draw'
    if p2=='A':
        if p1=='Y': return 6,'win'
    elif p2=='B':
        if p1=='Z': return 6,'win'
    elif p2=='C':
        if p1=='X': return 6,'win'
    return 0,'lose'
def calcpart1(moves):
    d = {'X':1, 'Y':2, 'Z':3}
    score=0
    for i in moves:
        out = outcome(i[1],i[0])
        score+=(d[i[1]]+out[0])
    return score
#part1
print(calcpart1(inn))

#part2
def new_outcome(p2,result):
    d = {'A':1, 'B':2, 'C':3}
    x = ['A','B','C']
    p1=''
    if result=='Y':#draw
        p1=d[p2]
    elif result=='X':#lose
        p1 = d[x[x.index(p2)-1]]
    elif result=='Z':#win
        x=x[::-1]
        p1 = d[x[x.index(p2)-1]]
    return p1

def calcpart2(moves):
    score=0
    d = {'X':0, 'Y':3, 'Z':6}
    for i in moves:
        your_move = new_outcome(i[0], i[1])
        score+=(d[i[1]]+your_move)
    return score
print(calcpart2(inn))