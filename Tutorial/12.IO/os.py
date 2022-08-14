from genericpath import isfile
import os

path = "C:\\Users\\LioN\\Desktop\\test"

if os.path.exists(path):
    print('That location exists!')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is a directory!')
    else:
        print('That location is not a file')
else:
    print('That location does not exist!')