with open('input.txt') as f:
    inn = [int(i.strip('\n')) for i in f.readlines()]

nums = [0] + sorted(inn) + [max(inn)+3]
print(nums)
def part1(nums):
    diffone , diffthree = 0,0
    for i in range(len(nums)-1):
        diff = nums[i+1]-nums[i]
        print(diff)
        if diff == 1:
            diffone+=1
        elif diff == 3:
            diffthree+=1
    return diffone*diffthree

#part2
count = {0:1} #count number of ways to get to each adapter
for adapter in nums[1:]:
    count[adapter] = count.get(adapter-1,0) + count.get(adapter-2,0) + count.get(adapter-3,0)
print(count[nums[-1]]) #print total ways to get to the last adapter
