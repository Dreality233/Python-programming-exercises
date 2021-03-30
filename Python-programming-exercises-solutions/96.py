from collections import Counter
s = input()
result = Counter(s)
print(" ".join([ f"{ch},{count}" for ch,count in result.items()]))