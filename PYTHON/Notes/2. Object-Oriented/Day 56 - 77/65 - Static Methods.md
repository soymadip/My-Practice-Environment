Static methods in Python are methods that belong to a class rather than an [instance/object](https://chat.openai.com/share/e985b140-1ce5-4cb5-83b9-c0c538b289b5) of the class. 
They are defined using the `@staticmethod` decorator and do not have access to the instance of the class _(i.e. self)_. 
They are called on the class itself, not on an instance of the class. 

Static methods are often used to create utility functions that don't need access to instance data but we wanna share it with the class.

```python
class Math:
	def __init__(self,name,age):
		self.name= name
		self.age= age
		
    @staticmethod
    def add(a, b):      # doesn't need self argument
        return a + b

# calling with object:
o1= Math(1,2)
print(o1.add(1, 2))
#calling without object
print(Math.add(1, 2))

# Output
3
```

In this example, the `add` method is a static method of the `Math` class. 
It takes two parameters a & b and returns their sum. 

The method can be called on the _class itself_, without the need to create an instance of the class.

---
# [[66 - Instance vs class variables|Next Lesson>>]]