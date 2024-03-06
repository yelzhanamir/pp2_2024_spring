import os
def path_filename(path_to):
    if os.path.exists(path_to):
        print("The path exists")
    else:
        print("The path doesn't exist")
        return 0
    file = os.path.basename(path_to)
    direct = os.path.dirname(path_to)
    print("File name: " + file)
    print("Directory: " + direct)
    
path_to = "test/test2/test2_1"
path_filename(path_to)

