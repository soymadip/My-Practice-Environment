# Info methods: 
In Python, there are _3 built-in functions_ that are commonly _used to get information about objects_: 
- `dir()`
- `__dict__`  
- `help()`


Let's take a look at each of them:
## The `dir()` method:
> The `dir()` function _returns a list of all the attributes and methods (including dunder methods) available for an object._ 
> It is a useful tool for discovering what you can do with an object.
- Example:

```python
x = [1, 2, 3]
print(dir(x))

#Output
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## The `__dict__` attribute:
>The `__dict__` _attribute_ _returns a dictionary representation of an object's attributes_. 
>- It is a useful tool for introspection.

- Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print(p.__dict__)

#Output:
{'name': 'John', 'age': 30}
```
## The help() method
>The __help()__ function is _used to_ __get help documentation for an object__, including a description of its attributes and methods.

- Example:- 

```python
print(help(str))

#output:
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
   ```

>[!example] In conclusion
>`dir()`, `__dict__`, and `help()` are useful _built-in functions_ in Python _that can be used to get information about objects_. They are valuable tools for introspection and discovery.

---

# [[72 - super keyword|Next Lesson>>]]