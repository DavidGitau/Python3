

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('You cannot divide by zero! Idiot!!')
except ValueError as e:
    print(e)
    print('Enter only numbers plz')
except Exception as e:
    print(e)
    print('Something went wrong :(')
else:
    print(result)
finally:
    print('Will always execute')