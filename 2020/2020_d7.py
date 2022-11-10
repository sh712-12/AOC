with open('input.txt') as f:
    data = f.readlines()
    d = {i.split('contain')[0].rstrip('bags ') : i.split('contain')[1] for i in data }
    # d2 = {i.split('contain')[0].rstrip('bags ') : i.split('contain')[1].strip('bags\n').strip(' bag.').split(',') for i in data }
# print(d)
def search(s):
    f=[]
    # print(f,s)
    for i in d:
        if s in ''.join(j for j in d[i]):
            f.append(i)
    # print(f)
    for i in list(set(f)):
        f+=search(i)
    
    return f
print(len(set(search('shiny gold'))))
