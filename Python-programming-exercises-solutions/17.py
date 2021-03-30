sums = 0
while True:
    log = input()
    if log:
        log = log.split(' ')
        if log[0]=='D':
            sums += int(log[1])
        elif log[0]=='W':
            sums -= int(log[1])
    else:
        break
print(sums)