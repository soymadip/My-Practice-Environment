# String formatting in python
>[!info]
String formatting can be done in python using the <mark class="hltr-grey2">format</mark> method.

##  Old Method: 

```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

---
# f-strings in python

It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

## Example
```python
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  
```

### Output:
```
Hello, My name is Tushar and I'm 23 years old.
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.
## Example
```python
print(f"{2 * 30})"  
```
### Output:

```
60
```

---

# f-string Methods

## use ==f-strings== inside f-string:

- Print <mark class="hltr-grey2">literally</mark> the f-string
- if we wanna <mark class="hltr-grey2">give examples</mark> of **f-strings** inside it, we have to do like this:-
```python
gender = male
age = 20

print("i am a {gender}, of {age} years old.") # this will print with gender and age values
print("i am a {{gender}}, of {{age}} years old.") # this will not print with values

```
- Output 
```python
i am a male , of 20 years old.

i am {gender}, of {age} years old.
```


## 

## [Next Lesson>>](29%20-%20Docstrings%20in%20python.md)