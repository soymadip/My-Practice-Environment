# Python Lists

- Lists are ordered collection of data items.
- List items are separated by commas and enclosed within square brackets <mark style="background: #5c5959;">[ ]</mark>. 
- Lists are changeable meaning we can alter them after creation.

Example 1:
```python
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```
Output:
```
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```

Example 2:
```python
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```
Output:# List Index
Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
 ```

---
# Accessing list items
 We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

## Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```
#### Output:
```
Blue
Green
Red
 ```

## Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```
#### Output:
```
Green
Blue
Red
```

## Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the `in` keyword.
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
  ```
#### Output:

```
Yellow is present.
```
 
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")
```
#### Output:
```
Orange is absent.
```

---
## Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range. 

Syntax:
```python
listName[start : end : jumpIndex]
```
Note: jump Index is optional. We will see this in later examples.

 

### Example: printing elements within a particular range:
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
```
#### Output:
```
['mouse', 'pig', 'horse', 'donkey']
['bat', 'mouse', 'pig', 'horse', 'donkey']
```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

Note: The element of the end index provided will not be included. 

### Example: printing all element from a given index till the end
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
```
### Output:
```
['pig', 'horse', 'donkey', 'goat', 'cow']
['horse', 'donkey', 'goat', 'cow']
```
>When no end index is provided, the interpreter prints all the values till the end.
 

### Example: printing all elements from start to a given index
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
```
#### Output:
```
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
```

>When no start index is provided, the interpreter prints all the values from start up to the end index provided. 

 
### Example: ==Printing alternate values==

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]

print(animals[::2])		#using positive indexes
```
### Output:
```
['cat', 'bat', 'pig', 'donkey', 'cow']
```

>Here, python jumps from __start to end with__ ==2== _jump index_.

 
### Example: printing every 3rd consecutive value withing a given range
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
```
### Output:
```
['dog', 'pig', 'goat
```
Here, jump index is 3. Hence it prints every 3rd element within given index.
```
['Abhijeet', 18, 'FYBScIT', 9.8]
```
As we can see, a single list can contain items of different data types.

----
# List Comprehension

List comprehensions are used for creating <u>new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.</u>

>Quick Tip: <mark style="background: #FFB86CA6;">This is made with a loop</mark>... 

## Syntax:

List = [Expression(item) for item in iterable if Condition]

- **Expression**: It is the item which is being iterated.

- **Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

- **Condition**: Condition checks if the item should be added to the new list or not. 

### Example 1: Accepts items with the small letter “o” in the new list

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]      

namesWith_O = [i for i in names if "o" in item]  
print(namesWith_O)
```
### Understanding:
>  The `[i for i in names if "o" in item]` part is actually <mark style="background: #FFB86CA6;">a for loop</mark>:

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

for i in names:
    if "o" in i:
        print(i)
```

### Output:
```
['Milo', 'Bruno', 'Rosa']
 ```

## [[23 - List Methods|Next Lesson>>]]