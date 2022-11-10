with open('input.txt') as f:
    con = f.read()

input = con.split('\n')
# number_ones = {1:len([i[0] for i in range(len(input)) if i=='1'])}

def most_common(input_):
    number_ones, number_zero={},{}
    for i in range(1,len(input[0])+1):
        one=0
        zero=0
        for j in input_:
            # print(j)
            if j[i-1]=='0':
                zero+=1
            else:
                one+=1
        number_ones[i] = one
        number_zero[i] = zero
    return number_ones, number_zero

o2=input
co2=input
for i in range(1,len(input[0])+1):
    res = most_common(o2)
    ones,zero = res[0], res[1]
    # print(ones, zero)
    if ones[i]>=zero[i]:
        most_common_=1
    else:
        most_common_=0
    # print(most_common_)
    for j in o2:
        if o2.count(j) == len(o2):
            break
        # print(j[0])
        if int(j[i-1]) == most_common_:
           o2.append(j)
        else:
            o2 = [i for i in o2 if i!=j]
        # print(o2)

for i in range(1,len(input[0])+1):
    res = most_common(co2)
    ones,zero = res[0], res[1]
    # print(ones, zero)
    if ones[i]>=zero[i]:
        most_common_=1
    else:
        most_common_=0
    # print(most_common_)
    for j in co2:
        if co2.count(j) == len(co2):
            break

        # print(j[0])
        if int(j[i-1]) != most_common_:
           co2.append(j)
        else:
            co2 = [i for i in co2 if i!=j]
# /        print(co2)

a=int(o2[0], 2)
b=int(co2[0], 2)
print(a*b)