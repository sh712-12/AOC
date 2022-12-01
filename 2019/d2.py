with open('input.txt') as f:
    data =[int(i)for i in f.read().split(',')]
    # print(l)
#corrections:
def correct(n, noun, verb):
    n[1]=noun
    n[2]=verb 

def runcode(n):
    for i in range(0,len(n),4):
        if n[i]==1:
            i1,i2,i3 = n[i+1],n[i+2], n[i+3]
            n[i3] = n[i1]+n[i2]
        elif n[i]==2:
            i1,i2,i3 = n[i+1],n[i+2], n[i+3]
            n[i3] = n[i1]*n[i2] 
        elif n[i]==99:
            return n[0]
#part1
nums=list(data)
correct(nums,12,2)
print(runcode(nums))

#part2
ans=0
for noun in range(100):
    for verb in range(100):
        n = list(data)
        n[1] = noun
        n[2] = verb
        if runcode(n)==19690720:
            ans = 100*noun + verb
            break
print(ans)