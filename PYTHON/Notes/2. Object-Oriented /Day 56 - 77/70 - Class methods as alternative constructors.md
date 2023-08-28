>In object-oriented programming, the term "constructor" refers to  <mark style="background: #CACFD9A6;">a special type of method that is automatically executed when an object is created from a class.</mark>
The purpose of a constructor is to _initialize the object's attributes_, allowing the object to be fully functional and ready to use.

However, there are times when we may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. 
This is where class methods can be used as alternative constructors.

A class method belongs to the class rather than to an instance of the class. 
- One common use case for class methods __as alternative constructors__ is _when you want to create an object from data that is stored in a different format_, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age". 
- The default constructor for the class might look like this:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- <mark style="background: #FF5582A6;">But</mark> what if you want to _create a Person object from a _ __string__ _that contains the person's name and age, separated by a_ __comma(`,`)__?
- in that case, You can _define a class method_ named "`from_string`" to do this:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))   #creating an instance of Person class

#Now you can create a Person object from a string like this:
person = Person.from_string("John Doe, 30")
```

__Another common use case__ for class methods as alternative constructors is _when you want to create an object that needs a different set of default values than what is provided by the default constructor_. 
- For example, consider a class named `"Rectangle"` that has two attributes: `"width"` and `"height"`. 
- The default constructor for the class has `"height"` & `"width"` parameters.
	- To create another `"square"` object that's height & width are same, we can use a class-Method `"square_inp"` to return the size twice as `"height"` & `"width"` parameters.

```python
class Rectangle:
  def __init__(self, width, height):
    self.width = width   #parameters
    self.height = height
  def square(self):
	return(f'The square is {self.height * self.width} cm^2')
	
  @classmethod
  def square_inp(cls, size):
    return cls(size, size) # returning 2 size values 

rectangle = Rectangle.square_inp(10)
print(rectangle.square())
#Output:
The square is 100 cm^2
```

---
# [[71 - dir(), __dict__ & help()  methods|Next Lesson>>]]