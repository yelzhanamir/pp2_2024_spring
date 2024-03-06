import os
file = open(os.path.join('test/test2/test2_1', 'test2_1.txt'), 'r')
string = file.read()
file.close()
file = open(os.path.join('test/test2/test2_2', 'test2_2.txt'), 'w')
file.write(string)
file.close()
