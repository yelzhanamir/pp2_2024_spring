import os

def check(path_to):
    if os.path.exists(path_to):
        print("The path exists")
    else:
        print("The path doesn't exist")
        return 0
    
    if os.access(path_to, os.R_OK):
        print(f"The path is readable.")
    else:
        print(f"The path isn't readable.")
    
    if os.access(path_to, os.W_OK):
        print(f"The path is writable.")
    else:
        print(f"The path isn't writable.")
    
    if os.access(path_to, os.X_OK):
        print(f"The path is executable.")
    else:
        print(f"The path isn't executable.")

path_to = "test/test2/test2_11"
check(path_to)
