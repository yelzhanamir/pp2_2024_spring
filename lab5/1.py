import re
with open('row.txt', 'r', encoding='utf-8') as file:
    s = file.read()

x = re.findall(r"a+b*", s)
print(x)
