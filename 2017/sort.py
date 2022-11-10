L = [9,2,3,4,10,0,1,34]
for i in range(1,len(L)):
    j = i
    while L[j-1]>L[j] and j>0:
        L[j-1], L[j] = L[j], L[j-1]
        j-=1
print(L)
