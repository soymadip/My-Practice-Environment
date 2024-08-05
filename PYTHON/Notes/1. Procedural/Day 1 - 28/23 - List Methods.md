
## list.sort()
This method sorts the list in ascending order. The original list is updated

### Example 1:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```
### Output:
```
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
 
```

> [!info]
>What if you want to *print the list in descending order*?
>We must give *reverse=True* as a parameter in the sort method.

### Example 2:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```
### Output:
```
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
 ```

> [!info]
>The reverse parameter is set to `False` by default.

> [! warning] Note
>Do not mistake the reverse parameter with the reverse method.

 

## reverse()
This method reverses the order of the list. 

#### Example:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```
#### Output:
```
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
 ```

## index()
This method returns the index of the first occurrence( দুটো থাকলেও ১ম টাই বলবে ) of the list item.
#### Example:
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
Output:
```
1
3
 ```

## count()
Returns the count of the number of items with the given value.

#### Example:
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
```
#### Output:
```
2
3
 ```

## copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list. 

#### Example:
```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']
```
## append():
This method appends items to the ==end== of the existing list & **changes** the list.

#### Example:
```python
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green']
 ```
## <mark class="hltr-red">insert():</mark>

This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method & **changes** the list.

#### Example:
```python
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
 ```
## extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#### Example 1:
```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
 ```

## ==pop():==
- pop() is used to remove an item from list.
### Example
```python
countries = ["Spain", "Italy", "India", "England", "Germany"]  
contries.pop(3)
print(contries)
```

### Output:
```
['Spain', 'Italy', 'Finland', 'Germany', 'Russia']
```

---
## Difference between ==insert(),append() & extend( )==:-

> [!info] **insert()** is used to insert only one item in given index:-

```python
colors.insert(1, "green")   #inserts item at index 1
```

>[! Danger] append() is used to insert only one item at the ==end== of the list:-

```python
colors.append("green")   #inserts "green" at the end.
```

>[!info] extend() is used to insert a ==list== at the ==end==:-

```python
n = [1,2,3,4]
colors.extend(n)   #inserts n list at the end of colours list
```

---
## Concatenating two lists:
You can simply concatenate two lists to join two lists. 
- This metod <mark style="background: #d36d00;">doesn't change the list</mark> like <mark style="background: #5c5959;">insert(),extend( ) & append(),</mark> ==it creates a new list==..

#### Example:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

## ==Change a value of list:-==

To change a value of list use list[INDEX_NUMBER] : 

```python
colors = ["voilet", "indigo", "blue", "green"]
colors[1] = 9 # change item in index 1 with integer 9
print(colors)
```
- Output:-
```
colors = ["voilet", 9, "blue", "green"]
```
## 

---
## [Next Lesson>>](24%20-%20Tuples%20in%20Python.md)
