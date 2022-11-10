f = open('a.txt', 'r+')
#replace a with 69
data = f.read()
w = ''
print(data)
for i in data:
    if i!='a':
        w+=i
    else:
        w+='69'
f.close()
f = open('a.txt', 'w')
f.write(w)
f.close()
