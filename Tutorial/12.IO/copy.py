import shutil
import os
 
# copyfile()    copies the contents of a file
# copy()        copyfile() + permission mode + destination can be a directory
# copy2()       copy() + copies metadata(file's creation and modification times)

# shutil.copyfile('foo.txt','copy.txt')
# shutil.copy2('foo.txt','C:\\Users\\LioN\\Desktop\\test\\copy.txt')

# # Moving files and folders
# source = "test.txt"
# destination = "D:\\test\\test-move.txt"

# try:
#     if os.path.exists(destination):
#         print('There is already a file there')
#     else:
#         os.replace(source,destination)
#         print(f"{source} was moved")
# except FileNotFoundError:
#     print(f"{source} was not found")

# Delete files
path = "copy.txt"
try:
    os.remove(path)               # Does not delete empty dir
    # os.rmdir(path)                  # empty dir only
    # shutil.rmtree(path)             # del dirs 
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('No permission to delete')
except OSError:
    print('You cannot delete')
else:
    print(f"{path} was deleted")
