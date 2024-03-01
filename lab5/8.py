import re
txt =input("Enter your text: ")
x = re.findall(r"[A-Z][^A-Z]*", txt)
print(x)
