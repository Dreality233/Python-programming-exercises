x = []
for i in range(2000, 3001):
    if (i % 7 == 0) and (i % 5 != 0):
        x.append(str(i))
print(','.join(x))
