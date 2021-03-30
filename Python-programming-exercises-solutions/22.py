from collections import Counter
words = Counter(input().split(' '))
result = [ f"{word}:{count}" for word,count in words.items() ]
print(' '.join(sorted(result)))