# FOR Loop
import sys


# for letter in 'Python':             # Traversal of a string sequence
#     print('Current Letter:',letter,'\n')

# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:                # Traversal of list Sequence
#     print('current fruit:',fruit)
# print('Goodbye!')

# # Iterating by sequence index
# for index in range(len(fruits)):
#     print('Current fruit:',fruits[index])
# print('Goodbye')

# # FOR Loop with ELSE
# numbers = [11, 33, 55, 75, 37, 21, 23, 41, 12, 13]

# for num in numbers:
#     if num % 2 == 0:
#         print('The list contains an even number -',num)
#         break
# else:
#     print('The list does not contain an even number!')

# for i in range(50, 100, 2):
#     print(i)

# # NESTED FOR LOOP
# for i in range(1, 15):
#     for j in range(1, 15):
#         k = i * j
#         if k > 9 < 100:
#             sp = '   '
#         if k > 99:
#             sp = '  '
#         if k < 10:
#             sp = '    '
#         print(k,end=sp)
#     print()


# # BREAK statement
# no = eval(input('Enter any number to look up in list:'))
# numbers = [11, 22, 33, 55, 39, 75, 37, 21, 23, 41, 13]
# for num in numbers:
#     if num == no:
#         print('Number found!')
#         break
# else:
#     print('Number not found!')


# Iterator 
# Iterator is an object, which allows a programmer to traverse through all the elements of 
# a collection, regardless of its specific implementation. String, List or Tuple objects can be used to create an Iterator.
list = [1, 2, 3, 4]
# list = 'name'
it = iter(list)             # This builds an iterator object
# print(next(it))             # Prints nest available element in iterator
# Iterator object can be traversed using regular for statement
# for x in it:
#     if x == 'a':
#         print('Name contains A')
#     print(x,end='')
# Or using next() function
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# GENERATORS
# A generator is a function that produces or yields a sequence of values using yield method.
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            break
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)        # F is iterator object

while True:
    try:
        print(next(f),end=' ')
    except StopIteration:
        sys.exit()