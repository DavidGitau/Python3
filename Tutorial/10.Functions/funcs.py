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