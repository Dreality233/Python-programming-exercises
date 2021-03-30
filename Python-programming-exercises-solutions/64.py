n = int(input())
item = [ i/(i+1) for i in range(1,n+1)]
print(round(sum(item),2))