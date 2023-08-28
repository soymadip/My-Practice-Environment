# Python Sets

- Sets are **unordered** collection of data items.  
- in output it doesn't maintain set's order.
- Sets do not contain duplicate items.
- Set is enclosed within curly brackets {}, where Lists are with [] & Tuples are with () 
- Sets are unchangeable, so insert(),append(),extend(),count() are unusable.

#### Example:
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 19, 5.9, 'Carla'} # not in orignal set's order
 ```

Here we see that the items of set occur in random order and hence **they cannot be accessed using index numbers**. 

### **How to create empty set?** 
- To create empty set, we can not use '{ }' as it will create a ==dictionary==.
- so we have to use `set( )`
```python
	s = set()
	s1 = {}

    print(type(s))
    print(type(s1))
```
- Output:
```python
<class 'set'>  # set
<class 'dict'> # dictionary
```
---
## Accessing set items:
 
### Using a For loop
You can access items of set using a for loop. 

#### Example:
```python
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
  ```
#### Output:
```
False
Carla
19
5.9
```


# Joining Sets

- Sets in python more or less work in the same way as sets in mathematics. 
- We can perform operations like union and intersection on the sets just like in mathematics.

## I. union():
The union() prints all items that are **present in the two sets**. 

![[Union.jpg|200]]
- The union() method returns a new set ^732c24


#### Example:
```python

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

```
##### Output:
```
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
 ```

---
## Update():

- update() method adds item into the existing set from another set.
### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2) # Updating 'cities' set
print(cities)
```
#### Output:
```
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'} 
 
```
---
## Intersection():
The intersection() prints only items **that are similar to both the sets**. 

![[Intersection.png|200]]

- The intersection() method ***returns*** a **new set**.
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
```
##### Output:
```
{'Madrid', 'Tokyo'}
 ```
---
## intersection_update():
- intersection_update() method updates into **the existing set from another set**.
#### Example :
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```
##### Output:
```
{'Tokyo', 'Madrid'}
```

---
## symmetric_difference():

- The symmetric_difference() prints only **items that are** ***not*** **similar to both the sets** & returns a new set. 
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```
#### Output:
```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
 ```
---
## symmetric_difference_update():
- symmetric_difference_update() method updates into the existing set from another set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```
#### Output:
```
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
 ```
---
## difference():
- The difference() prints **only items that are only present in the original set and not in both the sets**. 
-  This is ***setA - setB***
- The difference() method returns a new set 
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
 ```
---
## difference_update():
- difference_update() method updates **only items that are only present in the original set and not in both the sets** into the existing set from another set.
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```
#### Output:
```
{'Tokyo', 'Berlin', 'Madrid'}
```
---
# Set Methods
There are several in-built methods used for the manipulation of set.They are explained below

## <mark class="hltr-red">isdisjoint()</mark>:

- This method checks if there is **no item is** ***common*** in 2 sets. 
- This method returns **true** then.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```
#### Output:

```
False
```

---
## issuperset():

The issuperset() method checks if 1st set is SuperSet[^1] of 2nd set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
```
#### Output:

False

---
## issubset():

- The issubset() method checks if 2nd set is subset[^2] of  the particular set.
- It returns True if all the items are present, else it returns False.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```
#### Output:

True

---
## add()
If you want to add a ***single item*** to the set use the add() method.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```
#### Output:

{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

---
## Update()

If you want to add ***more than one item***, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
- This also can be described as ***union***(ing) two sets...
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```
#### Output:

{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}

---
## remove()/discard()
We can use remove() and discard() methods to remove items form list.

#### Example :
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
```
##### Output:

{'Delhi', 'Berlin', 'Madrid'}

>[!info] 
>- The ***main difference*** between remove and discard is that, 
>
>if we try to delete an item which is not present in set, then **remove() raises an error**, whereas **discard() does not raise any error & continues..**.
#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
```
##### Output:

KeyError: 'Seoul' 

---
## pop()

This method removes _the last item of the set_ but the **catch** is that we don’t know ***which item gets popped as sets are unordered***. 

However, you can access the popped item if you assign the pop() method to a variable.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
```
#### Output:

{'Tokyo', 'Delhi', 'Berlin'}
Madrid
 
---
## del
del is not a method, rather it is a keyword which deletes the set entirely.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```
#### Output:
```
NameError: name 'cities' is not defined 
```

>[!info] 
>We get an error because our **entire set** has been **deleted** and there is no variable called `cities` which contains a set.

 ---

## What if we don’t want to delete the entire set, we just want to delete all items within that set?

### clear():
This method clears all items in the set and prints an empty set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```
#### Output:
```
set()
```
 
## Check if item exists
You can also check if an item exists in the set or not.

##### Example
```python
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
  ```
#### Output:

Carla is present.

---
## Empty Set:-




------

##### Foot-Notes zone:-
`Not Important`

[^1]: Learn about superSet [HERE](https://en.m.wikipedia.org/wiki/Subset#:~:text=In%20mathematics%2C%20set%20A%20is,a%20proper%20subset%20of%20B) 
[^2]: Learn about subSet [HERE](https://en.m.wikipedia.org/wiki/Subset#:~:text=In%20mathematics%2C%20set%20A%20is,a%20proper%20subset%20of%20B)

-----

# [[33 - Dictionary in python|Next Lesson>>]]