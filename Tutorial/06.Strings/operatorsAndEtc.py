# Updating Strings
var1 = 'Hello David'
print('Updated String:-',var1[:6]+'Gitau')

# Escape Characters
print('This is an j\a "a" escape')       # Bell or alert
print('This is a backspace bs\bbs')      # Backspace
print('This is a \C-x control-x')       # Control-x
print('This is a escape bs \\e bs')      # Escape

print('This is a space bs \\s bs')
print('This is a tab bs \tbs')          # Tab
print('This is a vertical tab bs \v\v\vbs')          # Vertical Tab   
print('This is a newline bs \nbs')          # Newline

# Special Operators
a = 'Hello There'
b = 'David'
print(a+b)                  # Concatination
print(a*2)                  # Repetition

print(a[1])                 # Slice
print(a[1:4])               # Slice Range
print(a[:4])
print(a[4:9])
print(a[0:9:2])
print(a[::3])               # 3 steps
print(a[::-1])              # Reverse

web = 'http://google.com'
slic = slice(7,-4)          # Create slice object
print(web[slic])

print('H' in a)             # Membership- Returns True or 1
print('H' not in a)         # Membership - False
print(r'Hello \n David')    # Raw String - Suppresses Special Characters
