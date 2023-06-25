
# function to calculate factorial:

def factorial(n): # this thing has a limit of 999 though😁
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


# function to calculate Fibonassi number:
# it works like this: 
# f(0) = 0, f(1) = 1, f(2) = 1+0 = 1, f(3) = 2+1 = 3, f(4) = 3+2 = 5, f(5) = 4+3 = 7 
# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

def fibonassi(n):
    if(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return ((n-1) + (n-2))

# function to calculate both- 

function = int(input('''Here is my supported functions:\nPress 1 to calculate "Fibonassi Number".\n Press 2 to calculate "Factorial" of a number.\n Press 3 to calculate Both.\nGimme input according to What you wanna calculate:'''))
input = int(input('Now give me the number you wanna calculate:'))

if(function == 1):
    print(fibonassi(input))
elif(function == 2):
    print(factorial(input))
elif(function == 3):
    print(f"Factorial of {input} is",factorial(input),f"\nFibonassi number of {input} is",fibonassi(input))
else:
    print(f'your input {input} is not in my supported functions')