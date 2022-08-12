from check import Check
import time

def dec1(f):
    return f


# Decorator Class 
class Dec2(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func
        self.cond = True

    def __call__(self, *args, **kwargs):
        while self.cond == True:
            res = self.func(*args, **kwargs)
            c = Check(res, self.cond)
            c.check()
            self.cond = c.cond
            time.sleep(2)
        return self.cond
        
