import math
values = input().split(',')
result = []
C = 50
H = 30
for D in values:
    result.append(str(round(math.sqrt(2*C*float(D)/H))))
print(','.join(result))