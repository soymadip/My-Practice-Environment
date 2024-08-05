## What is a variable?
Variable is like a **container that holds data.** Very similar to how our containers in kitchen holds sugar, salt etc
Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
```python
a = 1
b = True
c = "Harry"
d = None
	```

These are four variables of different data types.

## What is a Data Type?
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. \
In python, we can print the type of any operator using type function:
```python
a = 1
print(type(a))
b = "1"
print(type(b))
```



<big>By default, python provides the following built-in data types:</big>


## 1. Text data: string

```python
"Hello World!!!", "Python Programming"
```


> [!info] Why "" is required?
> because if we create a variable of same name, "" will indicate that we are refering to the variable without quote.


## 2. Numeric data: int, float, complex

### Integer:
All real numbers.
- *Example*: 1-100, 10000-333333  .......
  
### Float:
All numbers with `.` value.
- *Example*: 10.2, 232.32323 ............
   
### Complex:
All unreal numbers.
- *Example*: 6 + 2i 

## 3. Boolean data:

Boolean data *consists of values* **True** or **False**.

## 4. Sequenced data

### **list:**
A list is *an ordered[^ord] collection of data with elements separated by a comma and enclosed within square brackets*. 
- Lists are *mutable* and can be modified after creation.

- **Example:**

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

- Output:

```python
[8, 2.3, [-4, 5], ['apple', 'banana']]
```

>[!Danger]  Note
As shown in example, Lists *Can contain other lists*


### **Tuple:**  
A tuple is an *ordered[^ord] collection of data with elements separated by a comma and enclosed within parentheses*.
- Tuples are *immutable* and can not be modified after creation. 

- **Example:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

- Output:

```python
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```


## 5. Mapped data: 
### **dictionary:** 
A dictionary is an *unordered[^uord] collection of data containing a key:value pair.* 
- The key:value pairs are enclosed within curly brackets.

- **Example:**

```python
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
```

- Output:

```python
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```



---
## [[7 - Operators|Next Lesson>>]]


---
[^ord]: Ordered data types are a *type of data type that has a natural ordering or ranking*. In other words, the values in an ordered data type can be put in a one-to-one correspondence with the positive integers. This means that each value can be assigned a unique position or ranking, and the values can be compared to determine their relative order. **In other terms, they have an index number.**
[^uord]: Types of data that doesn't have index numbers.