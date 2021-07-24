i = 0
x = int(input('Please enter a number'))
while x != 1 and x != 2:
    x = int(input('Please enter a number'))
    i += 1
else:
    print('You are correct!','You have tried',i+1 , 'times')