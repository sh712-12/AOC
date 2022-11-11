#Part 2 doesn't work yet


with open('input.txt') as f:
    inn = [i.strip('\n') for i in f.readlines()]

def resolve(l):
    visited = set()
    ind=0
    accmulator=0
    for i in range(len(l)):
        if ind==len(l): break
        
        if ind in visited: 
            print(f'infinite loop, accumulator before repetition = {accmulator}')
            return 1, accmulator

        print(l[ind], visited, ind, accmulator)
        visited.add(ind)

        cmd, arg = l[ind].split(' ')

        if cmd=='acc':
            accmulator+=int(arg)
            ind+=1
        elif cmd=='nop':
            ind+=1
        elif cmd=='jmp':
            ind+=int(arg) 

    return 0, accmulator
#part 1
# print(resolve(inn)[1])

#part 2
#replace nop with jmp and jmp with nop for each nop and jmp and check if code is fixed
fixed=[]
for i in range(len(inn)):
	cmd, arg = inn[i].split(' ')
	if cmd=='jmp':
		fixed = inn[:i] + [f'nop {arg}'] + inn[i+1:]
		x,acc = resolve(fixed)
		if not x:
			print(acc)
			break