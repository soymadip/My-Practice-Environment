# Operators
Python has different types of operators for different operations. To create a calculator we require arithmetic operators.
# Arithmetic operators

| Operator | Operator Name  | Math sign & Example |
| -------- | -------------- | ------------------- |
| +        | Addition       | ``` 15+7 = 22 ```         |
| -        | Subtraction    | ``` 15-7 = 8 ```          |
| *        | Multiplication | ``` 5*7 = 35 ```          |
| /        | Division       | ``` 5/3 = 1.666666667 ``` |
| **       | Exponential    | ``` 5^3 = 125 ```         |
| %        | Mudulas        | ``` 15%7 = 1 ```          |
| //       | Floor Division | ``` 15//7 = 2 ```         |

## Ex:
```python
n = 15
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
```
### Explaination
Here 'n' and 'm' are two variables in which the integer value is being stored. Variables 'ans1' , 'ans2' ,'ans3', 'ans4','ans5' and 'ans6' contains the outputs corresponding to addition, subtraction,multiplication, division, modulus and floor division respectively.

---
# Exercise 1 - Create a Calculator
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!
Hitnt:
```python
print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(5%3)
print(2**4)
```
## Solution:

![[8 - Ex1 ~Solution]]

## [[9 - Typecasting in Python|Next Lesson>>]]
