# Finally Clause

- `Finally` statement is used after try-except or loop to execute  a certain input.....

# Syntax:

```python
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation   
```

> [!question] Why not just a ==print== statement in the end? 

- Because if we are in a function and use `return` statement , the end `print` becomes invalidated as function has returned a vale....
	Example:-
	```python
	def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: ")) # takig an integer input
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  print('i am always executed')

  x = func1()	
	```

in above function, 0 to 3 is given as input(as index of the list is 4), it will return indexed value & 1 and if any if anything other than integer is given, `some error occured` will be printed. 
	 But the last print statement (i am always executed) will not be printed in any case....
```python
0 # if integer between 0 to 3 is given 

some error occued.
1 # if integer is not given
```

- so if we need to print certain statement  <mark style="background: #FF5582A6;">at any condition</mark>, we have to use `finally ` statement...
	```python
	def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  finally:
    print("I am always executeṇd")

   x = func1()
	```
- Output:-
```python
0
i am always executed # if integer between 0 to 3 is given

some eror occured
1
i am always executed # if integer is not given
```


---
## [[38 - Custom Errors|Next Lesson>>]]