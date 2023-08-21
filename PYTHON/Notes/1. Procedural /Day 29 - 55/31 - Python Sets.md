# Python Sets

- Sets are **unordered** collection of data items.  
- in output it doesn't maintain set's order.
- Sets do not contain duplicate items.
- Set is enclosed within curly brackets {}, where Lists are with [] & Tuples are with () 
- Sets are unchangeable, so insert(),append(),extend(),count() are unusable.

#### Example:
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 19, 5.9, 'Carla'} # not in orignal set's order
 ```

Here we see that the items of set occur in random order and hence **they cannot be accessed using index numbers**. 

### **How to create empty set?** 
- To create empty set, we can not use '{ }' as it will create a ==dictionary==.
- so we have to use `set( )`
```python
	s = set()
	s1 = {}

    print(type(s))
    print(type(s1))
```
- Output:
```python
<class 'set'>  # set
<class 'dict'> # dictionary
```
---
## Accessing set items:
 
### Using a For loop
You can access items of set using a for loop. 

#### Example:
```python
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
  ```
#### Output:
```
False
Carla
19
5.9
```



## [Next Lesson>>](32%20-%20Set%20Methods.md)