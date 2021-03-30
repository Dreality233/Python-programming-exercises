input_str = input()
uppers = 0
lowers = 0
for char in input_str:
    if char.isupper():
        uppers += 1
    elif char.islower():
        lowers += 1
    else:
        pass
print(f"UPPER CASE {uppers} LOWER CASE {lowers}")