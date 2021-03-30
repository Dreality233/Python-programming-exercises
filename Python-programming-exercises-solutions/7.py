input_str = input()
dimensions = input_str.split(',')
row = int(dimensions[0])
col = int(dimensions[1])
multilist = [[0 for c in range(col)] for r in range(row)]
for r in range(row):
    for c in range(col):
        multilist[r][c] = r * c
print(multilist)

