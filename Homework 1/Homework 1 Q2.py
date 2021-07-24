try:
    x = int(input('Please enter a number'))
    if x == 0:
        print('x is 0')
    elif x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')
except ValueError:
    print('Error: enter a number')
