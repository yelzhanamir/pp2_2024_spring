import os

for i in range(ord('A'), ord('Z')+1):
    filename = chr(i) + ".txt"
    file = open(os.path.join("dir_and_files_6", filename), 'w')
    file.close()
