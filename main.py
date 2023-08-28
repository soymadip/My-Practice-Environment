



class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def square(self):
    return(f'The square is {self.height * self.width} cm^2')

  @classmethod
  def square_inp(cls, size):
    return cls(size, size)

rectangle = Rectangle.square_inp(10)

print(rectangle.width)
print(rectangle.height)

rectangle1 = Rectangle.square_inp(344)
print(rectangle1.square())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print(p.__dict__)

