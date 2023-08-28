## Introduction

- In Python, _classes are a way to define custom data types that can store data and define functions that can manipulate that data_. 
- One type of _function that can be defined within a class is called a "method"_. 
- In this Lesson, we will explore what Python class methods are, why they are useful, and how to use them.

## What are Python Class Methods?

A __class method__ is _a type of method that is bound to the class and not the instance of the class_. 
- In other words, it operates _on the class as a whole_, rather than on a specific instance of the class. 
- Class methods are defined using the `"@classmethod"` decorator, followed by a function definition. The first argument of the function is always <mark style="background: #CACFD9A6;">"cls",</mark> which _represents the class itself_.

## Why Use Python Class Methods?

Class methods are useful in several situations.
- In general, _if we wanna overwrite a class variable for whole class_, we can use Class Method.
- If you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. 
- Another common use case is to provide _alternative constructors_ for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

## How to Use Python Class Methods

To define a class method, you simply use the <mark style="background: #CACFD9A6;">"@classmethod"</mark> decorator before the method definition. 
- The _first argument_ of the method _should always be_ <mark style="background: #CACFD9A6;">"cls,"</mark> which represents the class itself. 
- Here is an example of how to define a class method:

```python
class student:
  grade = 4                # default value for class variable 'grade'
  def __init__(self,name,age):  #setting __init__ & parameters
    self.name= name     
    self.age= age
  def get_data(self):
    print(f'{self.name} is a {self.age} years old student in grade {self.grade}')
  @classmethod               #classMethod decorator
  def update_grade(cls,grade): 
    cls.grade = grade

#creating instances:
st1= student('Rahul', 12)
st2= student('Harry', 12)
st3= student('Amol', 13)
st4= student('sohili', 13)
#getting student data:
st1.get_data()
st2.get_data()

student.update_grade(5)  # changing value for rest of the students(instances)
st3.get_data()
st4.get_data()

# Output:
Rahul is a 12 years old student in grade 4
Harry is a 12 years old student in grade 4
Amol is a 13 years old student in grade 5
Sohili is a 13 years old student in grade 5
```

In this example, the <mark style="background: #CACFD9A6;">"update_grade"</mark> is a class method that takes 1 argument, "grade". 
- It creates a new instance of the class <mark style="background: #CACFD9A6;">"student"</mark> using the <mark style="background: #CACFD9A6;">"cls"</mark> keyword, and returns the new instance to the caller.

It's important to note that class methods cannot modify the class in any way, they change a class variable's value. 
- If you need to modify the class, you should use a class level variable instead.

## Conclusion

Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.

---

# [[70 - Class methods as alternative constructors|Next Lesson>>]]