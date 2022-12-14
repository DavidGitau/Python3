import base64
import time
# import math

str1 = 'this is a string example... wow!!!'
print('str1.capitalize() :',str1.capitalize())       # Capitalize
print('str1.upper() :',str1.upper())                 # Upper
print('str1.lower() :',str1.lower())                 # Lower
print('str1.count(i) :',str1.count('i'))             # Count
print('Replace a with e',str1.replace('a', 'e'))     # Replace
print('str1.center(40, "a") :',str1.center(40, "a"))

# count() returns the number of occurrences of a substring sub in the range [start, end]
# str1.count(sub, start=0, end=len(string))
sub = 'i'
print('str1.count("i") :',str1.count(sub))
print('str1.count("exam", 10, 40) :', str1.count(sub, 40, 50))


# Encode() and Decode()
today = time.time()
enc = base64.b64encode(str(today).encode('utf-8', 'strict'))
print('Encoded String:',enc)
dec = base64.b64decode(enc.decode('utf-8','strict'))
print( 'Decoded String: ',dec)

# Endswith()
suffix = '!!'
print(str1.endswith(suffix))
print(str1.endswith(suffix,len(str1)))
print(str1.endswith(suffix, 10,len(str1)-1))

# Expandtabs()
str2 = 'This is\ta string example... wow!!!'
print('Original string:',str2)
print('Default expanded tab:',str2.expandtabs(16))
print('Double expanded tab:',str2.expandtabs(32))

# Find()
str2 = 'exam'
print(str1.find(str2),str1[17:21])
print(str1.find(str2,10))
print(str1.find(str2,10,15))

# Index() similar to find
print(str1.index(str2),str1[17:21])
# print(str1.index(str2,10,15))     # Returns error if not found

# Isalnum()
str2 = 'this2022'           # No space on string
print(str2.isalnum())
print(str1.isalnum())

# Isalpha()
str2 = 'this'
print(str2.isalpha())
print(str1.isalpha())

# Isdigit()
str2 = '2022'
print(str2.isdigit()) 
print(str1.isdigit())

# Format()
animal = 'cow'
item = 'moon'
number = 3.1415
num2 = 1000

print('The number pi is {:.2f}'.format(number))
print('The number is {:,}'.format(num2))
print('The number is {:b}'.format(num2))
print('The number is {:o}'.format(num2))
print('The number is {:x}'.format(num2))
print('The number is {:E}'.format(num2))


print('The {:10} jumped over the {:>10}'.format(animal,item))
print('The {0:^10} jumped over the {1:<10}'.format(animal,item))        # positional argument
# print('The {item} jumped {animal} over the {animal}'.format(animal='cow',item='moon'))        # keyword argument

























