import os
file = open(os.path.join('test/test1/test1_1', 'test1_1.txt'), 'r')
string = file.read()
lines = 0
if string != "":
    lines = 1
for i in string:
    if i == '\n':
        lines+=1
print("Number of lines:", lines)
