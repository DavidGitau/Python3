# Openig a file
with open('foo.txt', 'wb') as fo:
    print('Name of the file:', fo.name)
    print('Closed or not:', fo.closed)
print('Opening mode:', fo.mode)

# Close opened file 
fo.close()

# Write()
fo = open('foo.txt', 'w')
fo.write('Dave is a great guy.\nTrust me!!')
fo.close()

# Read()
fo = open('foo.txt','r+')
str1 = fo.read(10)
print('Read String is:', str1)

# Check current position
position = fo.tell()
print('Current file position:',position)

# Reposition pointer at beginning of file 
position = fo.seek(0,2)
position = fo.tell()
print('Again the current file position:',position)

str1 = fo.read(-20)
print('Again read String is:',str1)

fo.close()