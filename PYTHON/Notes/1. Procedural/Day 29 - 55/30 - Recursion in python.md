
# Recursion in python

Recursion is the process of defining something in terms of itself.

## Python Recursive Function
In Python, It is even possible for the function to call itself. These types of construct are termed as recursive functions.

#### Example:
```python
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))
 ```

##### Output:
```
number:  7
Factorial:  5040
```

---

## Quick Quiz:

### function to calculate Fibonassi number:

> [!info]
it works like this:
 f(0) = 0, f(1) = 1  |  f(n) = f(n-1) + f(n-2)
>>f(0) = 0,  f(1) = 1, f(2) = 1+0 = 1,  f(3) = 2+1 = 3,  f(4) = 3+2 = 5,  f(5) = 4+3 = 7
 

```python

def fibpnassi(number):
	if(number == 1):
	    return 1
	elif(number == 0):
	    return 0
	else:
	    return ((number-1) + (number-2))


number = int(input('enter your number: '))
print(fibpnassi(number))

```

## [Next Lesson>>](31%20-%20Python%20Sets.md)