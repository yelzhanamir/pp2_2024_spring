import re
txt =input("Enter your text: ")
x = re.findall(r"[A-Z][a-z]+", txt)
print(x)
