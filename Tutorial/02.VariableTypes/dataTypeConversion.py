# Data Type Converssion
a, b, c, d, f, s = '101', 23, 90.43, 'david', 4, ['one', 43]

print(int(a, 2))        # Converts a to int, base 2 a = 5
print(float(b))         # Converts b to float
print(str(c))           # Converts c to string
y = repr(b)
print(type(y))
st = input("Input st:  ")
print(eval(st))        # Evaluates a string returns an object
print(tuple(s))         # Converts s to a tuple
print(list(s))          # Converts s to a list
print(set(s))           # Converts s to a set
# k = tuple(s)
# print(dict(k))          # Creates a dictionary D must be a sequence of (key, value ) tuples
print(frozenset(s))     # Converts s to a frozen set
print(chr(f))           # Converts an integer to a character
# print(unchr)        # Converts an interger to a unicode character
f = chr(f)
print(ord(f))           # Converts a single character to its integer value
print(hex(b))           # Converts b to a hexadecimal value
print(oct(b))           # Converts an integer to an octal string
