import re
email = input()
# print(re.findall("(\w+)@\w+\.\w+",email)[0])
pat = "(\w+)@((\w+\.)+(com))"
r = re.match(pat,email)
print(r.group(1))