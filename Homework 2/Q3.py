t = int(input('Enter the total number of integers you want to calculate'))
num = []
i = 0
while i < t:
    if int(str(i)[-1]) == 0:
        temp = int(input('Please enter the ' + str(i+1) + 'st number.'))
    elif int(str(i)[-1]) == 1:
        temp = int(input('Please enter the ' + str(i + 1) + 'nd number.'))
    elif int(str(i)[-1]) == 2:
        temp = int(input('Please enter the ' + str(i + 1) + 'rd number.'))
    else:
        temp = int(input('Please enter the ' + str(i + 1) + 'th number.'))
    num.append(temp)
    i+=1
print('Total number of samples is', len(num))
print('The sum is ', sum(num))
print('The mean is ', sum(num)/len(num))
print('The smallest value is ', min(num))
print('The largest value is ', max(num))
