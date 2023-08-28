##  Using 'format' method:  
> Primarily String formatting can be done in python  _using the_ __format__ _method_.

```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```


## Using f-strings:

- This is a new string formatting mechanism introduced by the PEP 498 under [[29 - Docstrings in python#PEP 8|PEP 8]]. 
- It is _also known as_ _Literal String Interpolation_ or _more commonly_ as __F-strings__ (f character preceding the string literal). 
>The primary focus of this mechanism is to make the interpolation easier.

- When we _prefix_ the string with _the letter 'f',_ the string becomes the f-string itself. 
- The f-string can be formatted in much _same as the str.format() method_. 


- Example:
```python
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  


# Output:
Hello, My name is Tushar and I'm 23 years old.
```

- We can also __use this in a single statement__ as well. _To do some math_:

```python
print(f"{2 * 30})"  

# Output:
60
```

---

## f-string Methods

### Print "f-strings" inside f-string:

- Print _literally_ the f-string
- if we wanna _give examples_ of **f-strings** _inside it,_ we have to do like this:-
```python
gender = male
age = 20

print("i am a {gender}, of {age} years old.") # this will print with gender and age values
print("i am a {{gender}}, of {{age}} years old.") # this will not print with values


#Output 
i am a male , of 20 years old.
i am {gender}, of {age} years old.
```


---
# [[29 - Docstrings in python|Next Lesson>>]]