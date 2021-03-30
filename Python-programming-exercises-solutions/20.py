def generator(n):
    x = 0
    while x < n:
        yield x
        x += 7


g = generator(100)
for i in g:
    print(i)
