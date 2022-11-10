#Part 2 doesn't work yet


with open('input.txt') as f:
    inn = [i.strip('\n') for i in f.readlines()]

def resolve(l, fix=False):
    visited = set()
    ind=0
    accmulator=0
    for i in range(len(l)):
        if ind==len(l): break
        if ind in visited and not fix: 
            print(f'infinite loop, accumulator before repetition = {accmulator}')
            return accmulator
            
        if ind in visited and fix:
            lastcmd = l[list(visited)[-1]]
            if 'jmp' in lastcmd:
               l[list(visited)[-1]] = l[list(visited)[-1]].replace('jmp','nop')
            else:
                l[list(visited)[-1]] = l[list(visited)[-1]].replace('nop','jmp')
            print(l)
            return resolve(l, True)

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

    return accmulator
#part 1
# print(resolve(inn))

#part 2
print(resolve(inn, fix=True))
