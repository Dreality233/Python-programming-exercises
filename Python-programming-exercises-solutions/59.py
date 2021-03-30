import re
email = input()
pat = "(\w+)@(\w+)\.com"
r = re.match(pat,email)
print(r.group(2))