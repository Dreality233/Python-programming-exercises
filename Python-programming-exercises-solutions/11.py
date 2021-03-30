numbers = [ number for number in input().split(',') ]
result = []
for number in numbers:
    if int(number,base=2) % 5 == 0 :
        result.append(number)

print(','.join(result))

