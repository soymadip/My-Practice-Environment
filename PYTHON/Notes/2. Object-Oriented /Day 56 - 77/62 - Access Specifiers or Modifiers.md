Access specifiers or access modifiers in python programming are _used to limit the access of class variables and class methods outside of class_ while __implementing the concepts of inheritance__.

- Let us see the each one of access specifiers in details:

Types of access specifiers 
---
1.  Public access modifier
2. Private access modifier
3. Protected access modifier

# Public Access Specifier in Python

All the variables and methods (member functions) in python are _by default public_. 
	Any instance variable in a class followed by the ‘self’ keyword like `self.var_name` are public accessed.

## Example:

```python
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)


# Output:
21
Harry
```

# Private Access Modifier
>By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. 
>We cannot use private members outside of class.


In Python, there is _no strict concept of "private" access modifiers_ like in some other programming languages. 
However, a convention has been established to indicate that a variable or method should be considered private _by prefixing its name_ __with a double underscore(__)__. This is known as a _"weak internal use indicator"_ and it is a convention only, not a strict rule. 
Code outside the class can still access these "private" variables and methods with `name mangling`, but _it is generally understood that they should not be accessed or modified_.
## Example:
```python
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
    def __funName(self):  # An indication of private function
        self.y = 34
        print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())


# Output:
AttributeError: 'student' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
AttributeError: 'subject' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
```
Private members of a class cannot be accessed or inherited outside of class. 
If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

# Name mangling
Name mangling in Python is a technique used __to protect class-private and superclass-private attributes__ _from being accidentally overwritten_ __by subclasses__. 
Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

```python
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
```
In the example above, the attribute `_nonmangled_attribute` is marked as nonmangled by convention, but can still be accessed from outside the class. 

The attribute `__mangled_attribute` is private and its name is "mangled" to `_MyClass__mangled_attribute`, so it can't be accessed directly from outside the class, but you can access it by calling `_MyClass__mangled_attribute`


# `__dir__()`

`__dir__` is a method, used to print all available methods & attributes of a object.

### Example:
```python
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()
print(a.__dir__())

# Output:
['_nonmangled_attribute', '_MyClass__mangled_attribute', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

```

# Protected Access Modifier  
In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. 
In Python, the convention for indicating that a member is protected is to _prefix its name with a single underscore (_)_. 
For example, if a class has a method called` _my_method`, it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and _does not actually provide any protection or restrict access to the member_.
The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
## Example:
```python
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 


# Output:
Harry
CodeWithHarry

Harry
CodeWithHarry
```


---
# [[60 - Getters and Setters|Next Lesson>>]]