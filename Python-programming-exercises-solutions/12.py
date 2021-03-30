result = []
for i in range(1000,3001):
    flag = 1
    for j in str(i):
        if int(j)%2 == 0:
            flag = False
            break
    if flag:
        result.append(str(i))
print(','.join(result))