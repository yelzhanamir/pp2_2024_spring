import re
text =input('Enter your text ')
text = re.sub(r'[A-Z]', lambda x: f' {x.group(0)}', text)
print(text)