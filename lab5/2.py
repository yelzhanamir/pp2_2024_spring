import re
txt =input("Enter your text: ")
x = re.findall(r"ab{2,3}", txt)
print(x)
