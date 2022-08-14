def hello(fname, lname):
    print(f'Hello {fname} {lname}', end=' - ')
    print(f'Have a nice day!')

hello('Dave','Gitau')
hello('Mary','Wanjiku')

# Return statement
def multiply(a,b):
    return a * b

print(multiply(2,8))

"""
Keyword arguments 
Preceeded by an identifier when we pass them to a function 
The order of the arguments does not matter, unlike positional arguments
Python knows the names of the arguments that the function receives

"""
hello(lname='John', fname='Jones')


"""
*args
parameter that will pack all arguments into a tuple
useful so that a function can accept a varying amount of arguments
"""
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5))

"""
**kwargs
parameter that will pack all arguments into a dictionary
useful so that a function can accept a varying amount of keyword arguments
"""
def hello2(**kwargs):
    print('Hello',end=' ')
    for key, value in kwargs.items(): print(f'{value}',end=' ')

hello2(title='Mr',f='Dave',m='Lyon',l='Gitau')

# Higher order function - accepts or returns a function
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    print(func('hello'))

hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

# lambda - 1 line function, accepts any no of arguments but only one expression
double = lambda x : x * 2
multiply = lambda x, y : x * y
add = lambda x, y, z : x + y + z
full_name = lambda f_name, l_name: f"{f_name} {l_name}"
age_check = lambda age: True if age >= 18 else False
print(double(5))
print('David', 'Gitau')
print(age_check(18))