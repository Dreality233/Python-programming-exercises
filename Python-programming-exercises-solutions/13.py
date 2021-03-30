input_str = input()
letters = 0
digits = 0
for char in input_str:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        pass
print(f"LETTERS {letters} DIGITS {digits}")