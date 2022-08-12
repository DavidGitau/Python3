from secrets import choice
from tempConv import TempConv

class Check:
    def __init__(self, check, cond):
        self.choice = check
        self.cond = cond

    def check(self):
        if self.choice == 1:
            val = eval(input('Enter the value in degrees celcius: '))
            fah = TempConv(val).CtoF()
            print(val,'celcius =', fah,'Fahrenheit')

        elif self.choice == 2:
            val = eval(input('Enter the value in degrees Fahrenheit: '))
            cel = TempConv(val).CtoF()
            print(val,'Fahrenheit =', cel,'celcius')

        else:
            print('Option to terminate\nExiting.......')
            self.cond = False    