l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = list(map(lambda x:x**2,filter(lambda x:not x%2,l1)))
print(l2)