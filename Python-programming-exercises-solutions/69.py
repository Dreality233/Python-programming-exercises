def f(n):
    x = 0
    while x <= n:
        if x % 5 == 0 and x % 7 == 0:
            yield x
        x += 1

n = int(input())
l = [ str(i) for i in f(n) ]
print(','.join(l))