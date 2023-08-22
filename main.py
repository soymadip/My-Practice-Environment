# from Projects.PYTHON.Functions import greeting


# def greet(fx):
#     def mgreet(*args,**kwargs):
#         result = fx(*args,**kwargs)
#         print('shgshgdhasg')
#         greeting()
#         return result
#     return mgreet

# @greet
# def add(a,b):
#     return(a+b)


# print(f'your answer is: {add(12,12)}')



class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'Value is {self._value}')





obj = MyClass(10)
print(obj._value)
obj.show()

