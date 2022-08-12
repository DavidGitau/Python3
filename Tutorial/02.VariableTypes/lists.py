# Lists
list = ['abcd', 787, 2.23, 'David', 70.2]
tinyList = [123, 'David']

print(list)             # Prints complete list
print(list[0])          # First element of list
print(list[-1])         # Last element
print(list[1:3])        # From second till third
print(list[2:])         # Elements from third element
print(list[-3:])        # From the last third element
print(list[:-2])        # Up to the second last
print(tinyList * 2)     # List two times
print(list + tinyList)  # Concatination


# Tuples
# A tuple is another sequence data type that is similar to the list. A tuple consists of a 
# number of values separated by commas. Unlike lists, however, tuples are enclosed within 
# parenthesis.
# The main difference between lists and tuples is- Lists are enclosed in brackets ( [ ] ) and 
# their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) 
# and cannot be updated. Tuples can be thought of as read-only lists. 

tuple = ('abcd', 787, 2.23, 'David', 70.2)
tinyTuple = (123, 'David')

print(tuple)             # Prints complete tuple
print(tuple[0])          # First element of tuple
print(tuple[-1])         # Last element
print(tuple[1:3])        # From second till third
print(tuple[2:])         # Elements from third element
print(tuple[-3:])        # From the last third element
print(tuple[:-2])        # Up to the second last
print(tinyList * 2)     # List two times
print(tuple + tinyTuple)  # Concatination

# tuple[2] = 1000 # Invalid syntax with tuple
list[2] = 1000 # Valid syntax with list
