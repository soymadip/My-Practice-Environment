## If ... Else in One Line

There is also a shorthand syntax for the if-else statement, that can be used when the condition is simple and the code blocks are short. 

Here's an example:
#### Normally:
```python
if(a>b):
    print("A")
elif(a==b):
    print("=")
else:
    pass
```
#### In shortHand:-
```python
a = 2
b = 330
print("A") if a > b else print("B") if a=b else "" # it's pronunced as this: print("A") if a > b,   else print("B") if a=b,  else ""
```

You can also have multiple else statements on the same line:

## Example:-
One line if else statement, with 3 conditions:
```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") # it's pronunced as this: print("A") if a > b,   else print("=")
```

## Syntax:- 
```python

result = value_if_true if condition, else value_if_false

```

This syntax is equivalent to the following if-else statement:
```python
if condition:
    result = value_if_true
else:
    result = value_if_false

```

--- 
## Conclusion:

The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition. 

However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.



## [[42 - Enumerate|Next Lesson>>]]