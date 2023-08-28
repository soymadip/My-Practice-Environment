# String Slicing & Operations on String
# Length of a String
We can find the length of a string using len() function.

## Example:
```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# Output:
Mango is a 5 letter word.

```
# String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array. 

## Example:
```python
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

## Output:
Apple
Pie
pleP
ApplePie
```
 
>[!Note]
> This method of specifying the start and end index to specify a part of a string is called __slicing__. 

- <mark style="background: #D2B3FFA6;">There's another shorter method to slice a string:</mark>
```python
def from_string(string):
	name, age = string.split('-')
	return (name, int(age)) 
	
# This is shorter version of:
def from_string(string):
    name = string.split('-')[0]
    age = string.split('-')[1]
    return (name, int(age)) 

print(from_string("goofle-12"))


# output:
('goofle', 12) 
```


# Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.
## Example:
```python
alphabets = "ABCDE"
for i in alphabets:
    print(i)

# Output:
A
B
C
D
E
```

---
## [[13 - String methods|Next Lesson>>]]