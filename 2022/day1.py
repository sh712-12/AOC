with open('input.txt') as f:
    inn = [i.replace('\n',' ') for i in f.read().split('\n\n')]
    nums =[]
    # print(inn)
    for i in inn:
        l=[]
        for j in i.split(' '):
            # print(j)
            l.append(int(j))
        nums.append(l)


def findmax(l: list):
    smax=0
    index=0
    for i in range(len(l)):
        summ = sum(l[i])
        if summ>smax: smax, index=summ,i
    
    #remove largest element
    l.pop(index)
    return smax

#part1
print(findmax(nums))

#part2
s=0
s+=findmax(nums)+findmax(nums)+findmax(nums)
print(s)
