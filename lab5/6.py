import re
txt =input("Enter your text: ")
x = re.sub(r'[ ,.]', ":", txt)
print(x)
