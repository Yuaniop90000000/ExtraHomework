try:
    i = input('Please enter an integer: ')
    for element in i:
        print(element, end = " ")
except ValueError:
    print('Error: enter an integer')