# factorial & fibonacci number calculator

#----------------------------------------------------

# function to calculate factorial:

def factorial(n): # this thing has a limit of 999 though😁
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


# function to calculate fibonacci number:
# it works like this:
# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) # f represents fibonacci itself
# f(0) = 0, f(1) = 1, f(2) = 1+0 = 1, f(3) = 2+1 = 3, f(4) = 3+2 = 5, f(5) = 4+3 = 7 


def fibonacci(n):
    if(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# function to calculate both- 

def calculator(input_num, function):
    if(input_num > 999):
        return('sorry sir my limit is 999.\nI can not calculate from 4 digit numbers..')
    if(function == 1):
        return (f'fibonacci number of {input_num} is: {fibonacci(input_num)}')
    elif(function == 2):
        return (f'Factorial of {input_num} is {factorial(input_num)}')
    elif(function == 3):
        return (f'Factorial of {input_num} is {factorial(input_num)}\nfibonacci number of {input_num} is {fibonacci(input_num)}')
    else:
        return (f'your input {input_num} is not in my supported functions')

# Finally input_num & output:

function = int(input('''Here are the supported functions:
Press 1 to calculate the "Fibonacci Number".
Press 2 to calculate the "Factorial" of a number.
Press 3 to calculate both.
Enter your choice: '''))
input_num = int(input('Now give me the number you wanna calculate:'))

print(calculator(input_num, function))