from itertools import permutations

# if input == one line of numbers spereated by comma
def readinput(file):    #returns list of numbers
    with open(file) as f:
        input = f.readlines()
    pos = input[0].split(',')
    pos = [int(i) for i in pos]


#return list of all permuations of a string
def permute(s : str):
    ret = [''.join(p) for p in permutations(s)]
    # print(ret)
    return ret

# print(permute('abc'))