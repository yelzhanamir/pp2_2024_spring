import re
txt =input("Enter your text: ")
x = re.findall(r"a+b*", txt)
print(x)
