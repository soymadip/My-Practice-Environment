## Raising Custom errors 

In python, we can raise custom errors by using the `raise`  keyword. 
```python
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
```

sometimes we may need to create our own custom exceptions that serve our purpose.
like if we wanna stop function in an error.

---
## Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
```python
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.


---
## [[39 - Exercise 3~ Solution|Next Lesson>>]]