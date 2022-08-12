# ELIF

amount = eval(input('Enter amount: '))

if amount < 1000:
    discount = amount * 0.05
    print('Amount below 1000\nDiscount:',discount)
elif amount < 5000:
    discount = amount * 0.10
    print('Amount is between 1000 and 5000\nDiscount:',discount)
else:
    discount = amount * 0.15
    print('Amount is 5000 or above\nDiscount:',discount)
print('Net payable:',amount - discount)

# NESTED IF

num = eval(input('Enter a number:'))

if num % 2 == 0:
    if num % 3 == 0:
        print(num,'is divisible by 3 and 2')
    else:
        print(num,'is divisible by 2 and not 3')
else:
    if num % 3 == 0:
        print(num,'is divisible by 3 but not 2')
    else:
        print(num,'is not divisible by both 3 and 2')

# Single Statements Suites
var = 100

if(var == 100): print('Value of expression is 100')
print('Goodbye!')


























