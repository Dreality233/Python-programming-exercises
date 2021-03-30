from functools import reduce
n = int(input())
result = reduce(lambda x,y:x*y,range(1,n+1))
print(result)