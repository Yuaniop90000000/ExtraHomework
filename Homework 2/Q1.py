#Homework 2
#Q2
count = int(input("Enter the number of times to repeat the symbol on the first line"))
symbol = input("Specify the symbol to for the pattern with")
x = 0
while x <= count:
    print(symbol * (int(count)-x))
    x += 1
