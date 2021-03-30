t = (1,2,3,4,5,6,7,8,9,10)
new_t = tuple(x for x in t if not x % 2)
print(new_t)