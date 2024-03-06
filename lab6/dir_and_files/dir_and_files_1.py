import os

def list_directories_files(path_to):
    print(os.listdir(path = path_to))

path_to = "test/test1/"

list_directories_files(path_to)
