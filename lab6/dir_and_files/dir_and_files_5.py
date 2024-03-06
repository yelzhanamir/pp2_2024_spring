import os
file = open(os.path.join('test/test1/test1_2', 'test1_2.txt'), 'w')
string = ""
list = ["Hello", ",", "my", "friend", 467, 4345.1, ":("]
for i in list:
    string+=(str(i) + ' ')
file.write(string)




