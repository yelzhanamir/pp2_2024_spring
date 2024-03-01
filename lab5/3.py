import re
txt =input("Enter your text: ")
x = re.findall(r"[a-z]+_[a-z]+", txt)
print(x)
