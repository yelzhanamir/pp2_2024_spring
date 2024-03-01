import re
text =input('Enter your camel text ')
text=text[0].lower()+text[1:]
text = re.sub(r'[A-Z]', lambda x: f'_{x.group(0)}', text)
text=text.lower()

print(text)