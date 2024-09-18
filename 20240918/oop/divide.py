def find_quotient( d,n):
    if n == 0: 
        raise ZeroDivisionError()
    return d / n

try:
    number = int(input('enter  a number:'))
    result = find_quotient(10,number)
except ValueError:
    print('invalid input please enter the valid input')
except ZeroDivisionError:
    print('we cannot divided by zero!')
else:
    print(result)
finally:
    print('cleaning up')
    print('end of program')