# Variables in Python:
>In Python, variables can be defined _at the class level_ or _at the instance level_. 
>>Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

## Class Variables
Class variables are defined at the class level and are shared among all instances of the class. 
They are defined _outside of any method_ and are usually used to store information that is _common to all instances of the class_. 
For example, a class variable can be used to store the number of instances of a class that have been created.

```python
class Employee:
	companyname='corruption'    # class variable (valid for all objects/instances)
	mem_num = 0
	def __init__(self,name):
		self.name = name
		Employee.mem_num += 1
	def showdetails(self):      # creating showdetails() method
		print(f"{self.name} is {self.mem_num} no. employee in the companny '{self.companyname}'")


Employee1 = Emoloyee('Mammutta')
Employee1.showdetails()

Employee2 = Emoloyee('Guandhie')
Employee3 = Employee('Rattim')
Employee3.companyname = 'unity'    # changing the class variable's value only for this instance.

Employee2.showdetails()
Employee3.showdetails()


# output
Mammutta is 1 no. employee in the companny 'corruption'.
Guandhie is 3 no. employee in the companny 'corruption'.
Rattim is 3 no. employee in the companny 'unity'.
```

- In the example above, the `companyname` is shared among all instances of the class `MyClass`. 
- When we create new instances of `MyClass`, also the value of `mem_num` is incremented. 
	 When we call the `showdetails` method on 'Employee1' and 'Employee2', we get the value of `mem_num`.
- The `mem_num` class variable is updated after creating instances. 
	So the `showdetails` method will display the value as where it's placed, like `Employee3` & `Employee2` gives the same output in `.showdetails` method.

## Instance Variables
Instance variables are defined _at the instance level_ and are _unique to each instance of the class_. They are defined inside the `__init__` method and are usually used to store information that is specific to each instance of the class. 
- For example, an instance variable can be used to store the name of an employee in a class that represents an employee.

```python
class MyClass:
    def __init__(self, name):
        self.name = name    # Instance Variable
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane
```

>In the example above, each instance of the class `MyClass` has its own value for the _name_ variable. 
>When we call the `print_name` method on obj1 and obj2, we get different values for _name_.


# Summary
In summary, 
- __class variables__ _are shared among all instances of a class_ and are used to store information that is _common to all instances_. 
- __Instance variables__ _are unique to each instance of a class_ and are used to store _information that is specific to each instance_.

Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in Python.

It's also worth noting that, in python, _class variables are defined outside of any methods_ and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via `classname.varibale_name` or `self.class.variable_name`. 
But instance variables are defined _inside the methods_ and need to be explicitly declared as instance variable by using `self.variable_name`.

---
# [[67 - Ex6 ~ solution|Next Lesson>>]]