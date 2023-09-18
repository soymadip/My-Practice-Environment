>[!warning] Recommendation
> I recommend to watch [[62 - Access Specifiers or Modifiers|Day 62]] Before this lesson.
> And for this lesson, i say [this](https://www.youtube.com/watch?v=O3R_P5j41ns) video to understand this topic rather than original video.
>> Because i found the org video is kinda confusing & doesn't have enough clarity. 

>[!example] My understanding
> There is something called `encapsulation` & `private variables` in Python.
> - Getters are used to access these `private variables`.
> - where setters are used to add some logic to Getters.
> - Here is an example:
>> ```python
>>class Geeks:
>>	def __init__(self):
>>		self._age = 0
>>	
>>	# using property decorator to get a getter function
>>	@property
>>	def age(self):
>>		print("getter method called")
>>		return self._age
>>	
>>	# a setter function
>>	@age.setter
>>	def age(self, a):
>>		if(a < 18):
>>			raise ValueError("Sorry you age is below eligibility criteria")
>>		print("setter method called")                       # value error doesn't need `else`
>>		self._age = a
>>
>>mark = Geeks()
>>mark.age = 19
>>print(mark.age)
>>
>>
>> # Output: 
>>setter method called
>>getter method called
>>19
>>```
> - Getter method is used to overwrite the previously given value (here self.age).
> - setter adds logic to getter (here it will raise error if value is less than 18)

 
---
# Getter:
Getters in Python are methods that are used to access the values of an object's properties. 
They are used to return the value of a specific property, and are typically defined using the @property decorator.

Here is an example of a simple class with a getter method:
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
```

In this example, the `MyClass` class has a single property, `_value`, which is initialized in the `__init__` method. The value method is defined as a getter using the @property decorator, and is used to return the value of the` _value` property.

To use the getter, we can create an instance of the `MyClass` class, and then access the value property as if it were an attribute:
```python
>>> obj = MyClass(10)
>>> obj.value

# output:
10
```
---
# Setters

It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
For that we need setter method which can be added by decorating method with @property_name.setter

Here is an example of a class with both getter and setter:

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
```
We can use setter method like this:
```python
>>> obj = MyClass(10)
>>> obj.value = 20
>>> obj.value
20
```

In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.

## [[61 - Inheritance in Python|Next Lesson>>]]