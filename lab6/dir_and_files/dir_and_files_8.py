import os
def delete_file(path_to):
    if os.path.exists(path_to):
        os.remove(os.path.join(os.path.dirname(path_to), os.path.basename(path_to)))
        print("File " + os.path.basename(path_to) + " in " + os.path.dirname(path_to) + " deleted successfully")
    else:
        print("Directory doesn't exist")
path_to = 'dir_and_files_8/file_to_delete.txt'
delete_file(path_to)

