with open('input.txt') as f:
    inn = [int(i.strip('\n')) for i in f.readlines()]


def allsums(nums):
    sums=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sums+=[nums[i]+nums[j]]
    return sums

def solve(nums, prelen=25):
    for i in range(prelen+1,len(nums)):
        if nums[i] not in allsums(nums[i-prelen:i]):
            return nums[i]

#part 1
print(solve(inn))

#part 2
invalid = solve(inn)
print(inn)
def setgen(nums):
    for i in range(len(nums)-1):
        for j in range(i+2, len(nums)):
            numset = nums[i:j]
            yield numset

sets = setgen(inn)
for i in sets:
    # print(i)
    if sum(i)==invalid:
        ans = min(i) + max(i)
        print(ans)
        break