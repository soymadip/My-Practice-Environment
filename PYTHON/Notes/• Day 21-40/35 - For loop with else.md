# Python - else in Loop

- Python allows the `else` keyword to be used with the `for` and `while` loops too. The else block appears after the body of the loop.  
- The program exits the loop only after the else block is executed. 
- The statements in the else block will be `executed` **after** ***all iterations are completed***.

## Syntax
```python
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```

## Example:
```python
for x in range(5):
    print (f"iteration for {x+1} in for loop")
else:
    print ("else block in loop")
print ("Out of loop")
```

### Output:
```python
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

## Notes:-

- After **Breaking** loop, the <mark style="background: #5c5959;">else</mark> will not be printed.

### Example:-
```python
	for i in []: # creating empty list
	    print('nope')
	    break
	else:
	    print('this will not be printed as loop is broken')
```
#### Output:
```python
      # as loop is broken
```

## [[36 - Exception Handling|Next Lesson>>]]