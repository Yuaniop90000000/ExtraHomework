try:
    i = int(input('Please enter a three-digit integer: '))
    if len(str(i)) == 3:
        print(str(i)[0],str(i)[1],str(i)[2])
    else:
        print('Incorrect digits')
except ValueError:
    print('Error: enter an integer')