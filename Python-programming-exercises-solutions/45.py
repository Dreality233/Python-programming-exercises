l1 = [ i for i in range(1,11)]
l2 = list(filter(lambda x: not x%2,l1))
print(l2)