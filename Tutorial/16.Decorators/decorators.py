from types import MethodType
# This is the simplest decorator does nothing to the function being decorated.


def super_secret_function(f):
    return f

# @super_secret_function
def my_function():
    print('This is my secret function')

# The @-notation is equivalent to the following
# my_function = super_secret_function(my_function)

def disabled(f):
    """This function returns nothing, and hence removes the decorated function
    from local scope
    """
    pass

# @disabled
def my_func():
    print('This function can no longer be called...')

my_func()

# This is the decorator 
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b

print(multiply(3,5))


# Decorator Class 
class Decorator(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function')

testfunc()


# Decorator Class decorating methods 
class Decorator(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the decorator.')
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        # Return a Method if it is called on an instance
        return self if instance is None else MethodType(self, instance)


class Test(object):
    @Decorator
    def __init__(self):
        pass

a = Test()



class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0         # Number of calls of this method

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)


class Test1(object):
    def __init__(self):
        pass
    
    @CountCallsDecorator
    def do_something(self):
        return 'Something was done'


b = Test1()
b.do_something()
print(b.do_something.ncalls)

c = Test1()
c.do_something()
print(c.do_something.ncalls)

'Nothing'       # Nothing
# Decorator with argument (Decorator Factory) 
def decoratorfactory(message):
    def decorator(func):
        def wraped_funct(*args, **kwargs):
            print('The decorator wants to tell you : {}'.format(message))
            return func(*args, **kwargs)
        return wraped_funct
    return decorator

@decoratorfactory('Hello David')
def test3():
    pass

test3()