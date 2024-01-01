# Python Dictionaries

Dictionaries are _ordered collection of data items_. 
- They store multiple items in a single variable. 
- __Dictionary items__ _are key-value pairs_ that are _separated by_ __commas__ _and enclosed within_ __curly brackets `{ }`__.

-  Example-
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)


#Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
```

>[!example] Info
>- we can also write dictionaries like this:
>```python
>  info = {
>    'name': 'Karan',
>    'age': 19,
>    'eligible': True
>}
>```
>- This can be used to make code more user-friendly.


 
## Accessing Dictionary items

### get():

_Values in a dictionary can be accessed_ using keys by mentioning keys either in square brackets or _by using_ __get method__.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}

print(info['name'])
print(info.get('eligible')) # i use this one


#Output:
Karan
True
 ```


### values():
>We can __print__ _all of the values in the dictionary_ using __values()__ method.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

#Output:
dict_values(['Karan', 19, True])
 ```


### keys():
>We can _print all the keys_ in the dictionary using __keys()__ method.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


#Output:
dict_keys(['name', 'age', 'eligible'])
 ```

### items():
>We can _print all the key-value pairs_ in the dictionary using __items()__ method.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())


#Output:
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```


## Removing items from dictionary

### clear():
The clear() method _Removes all the items_ from the dictionary. 
#### Ex:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# Output:
{}
 ```

### pop():

The pop() method __removes__ the *key-value pair* whose key is passed as a parameter.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)


#Output:
{'name': 'Karan', 'age': 19}
 ```

### del:
we can ==also== use the del keyword to _remove a dictionary item_. 
- If key is not provided, then the del keyword will ***delete*** _the dictionary entirely_.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

del info
print(info)


#Output:
{'name': 'Karan', 'eligible': True, 'DOB': 2003}

NameError: name 'info' is not defined
```

### popitem(): 

The popitem() method __removes__ ***the last key-value pair*** from the dictionary.
#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


#Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
 ```

## Others

### update() 

The update() method __updates__ _the value of the key provided to it_,
- If the item already _exists_ in the dictionary, 
- Else it creates a new key-value pair.

#### Ex:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info.update({'age':20})
print(info)


#Output:
{'name': 'Karan', 'age': 19, 'eligible': True}

{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
 ```

### Copy():
> Using this method, we can __copy a dictionary__.

#### Ex
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}
n_info = info.copy()
print(n_info)

# Output:
{'name': 'Karan', 'age': 19, 'eligible': True}

```


## Loops in Dictionary
> We can use loop with Dictionaries with __.item()__ 

### Ex:
```python
Dict = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}

for k,v in Dict.items():  # k,v represents keys, values.
	print(f'{k}:',v)


# Output:
name: Karan
age: 19
eligible: True
DOB: 2003

```

---

# [[35 - For loop with else|Next Lesson>>]]