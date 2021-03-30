import re
pwds = input().split(',')
valid_pwds = []
for pwd in pwds:
    if re.search("[a-z]",pwd):
        if re.search("[0-9]",pwd):
            if re.search("[A-Z]", pwd):
                if re.search("[$#@]", pwd):
                    if 6 <= len(pwd) <= 12:
                        valid_pwds.append(pwd)
print(','.join(valid_pwds))
