def f(n):
    x = 0
    while x <= n:
        yield x
        x += 2

n = int(input())
l = [ str(i) for i in f(n) ]
print(','.join(l))