# 'is' vs '= =' :
>In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two of them.

- The `is` operator compares _the identity of two objects_, while
	- This will return True if the objects  are __the exact same object in memory__
- The `==` operator compares _the values of the objects_.  
	-  This will return True if the objects __have the same value__.

### For example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```
- In this case, a and b are two separate lists that have the same values, so `==` returns True. 
- However, a and b are not the same object in memory, so `is` returns False.

One important thing to note is that, in Python, _strings and integers are immutable_, which means that once they are created, their value cannot be changed. 
This means that, for strings and integers, is and `==` will always return the same result:

```python
a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True
```
In these cases, a and b are both pointing to the same object in memory, so is and == both return True.
For _mutable objects_ such as __lists & dictionaries__, `is` and `==` can behave differently. 


In general: 
	- Use `==` when you want to ==compare the values of two objects,== and 
	- Use `is` when you want to ==check if two objects are the same object in memory==.


---
# [[55 -Exercise 5 (Snake Water Gun)|Next Lesson>>]]