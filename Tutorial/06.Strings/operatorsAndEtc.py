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
a = 'Hello'
b = 'David'
print(a+b)                  # Concatination
print(a*2)                  # Repetition
print(a[1])                 # Slice
print(a[1:4])               # Slice Range
print('H' in a)             # Membership- Returns True or 1
print('H' not in a)         # Membership - False
print(r'Hello \n David')    # Raw String - Suppresses Special Characters
