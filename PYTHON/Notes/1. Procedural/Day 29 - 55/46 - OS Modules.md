> `OS` Module in Python

> [!summary]
> The `os` module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. 
> It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.
>  - Official [documents](https://docs.python.org/3/library/os.html) for more details.

The os module in Python is a built-in library that provides functions for interacting with the *operating system*. 
It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

# Here are some common tasks you can perform with the os module:

## Interacting with the file system:-

The `os` module also provides functions for interacting with the file system.

### os.getcwd( ):-
> Get the current working directory.

```python
import os          

#directory (CWD)
cwd = os.getcwd()

print("Current working directory:", cwd)

------
# Output:-
Current working directory: /home/nikhil/Desktop/gfg

```

### os.chdir( )
> Changing the Current Working Directory

```python	
import os

os.chdir('../') # changing dir 

------
# Output:-

#Current working directory before
C:\Users\Nikhil Aggarwal\Desktop\gfg

#Current working directory now
C:\Users\Nikhil Aggarwal\Desktop

```
### os.listdir( ):-
> you can use the *os.listdir* function to **get a list of the files in a directory**:

```python
import os

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)   

------
# Output:-

['myfile.txt', 'otherfile.txt']

```

## Create directory :-
>There are different methods available in the OS module for creating a directory.

###  os.mkdir( ):-
>os.mkdir() method in Python is used to create a directory named path **with the specified numeric mode**. 
>This method *raises FileExistsError if the directory to be created already exists.*

```python
import os

# Create a new directory
os.mkdir("newdir")

------
# Output:-

Directory 'newdir' created

```

### os.makedirs( ):-
> os.makedirs() method in Python is used *to create a directory* ==recursively==. 
> That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
> os.makedirs() method can be used to create a directory tree.

```python
import os
	
# Leaf directory
directory = "Nikhil"	
# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
# Path
path = os.path.join(parent_dir, directory)
	
# Create the directory 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)
	
# Directory 'GeeksForGeeks' and 'Authors' will
# be created too
# if it does not exists

------
# Output:-

Directory 'Nikhil' created

```

### os.remove( ):-
> **This method is used to delete files.**
> This method can not **remove or delete a** *directory*.
>  If the specified path is a directory then *OS Error will be raised*.
```python
import os 


# File name 
file='file1.txt'
location="D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"

os.remove(file)

------
# Output:-

file.txt deleted
```

###  os.rmdir( ):-
> **This method is used to delete directories or folders.**
> This method *cann't delete non-empty directories*.
> OSError will be raised if the specified path is not an empty directory.
>
![[Pasted image 20230810162932.png]]
```python
# Python program to explain os.rmdir() method
	
# importing os module
import os
	
# Remove the Directory "Geeks"
os.rmdir(Geeks)

```


---
## Reading and writing files

The `os` module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:

### os.read( ) & os.RDONLY flag:-
> Read the contents of the file
> 
```python
import os

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)
```

### os.read & os.O_WRONLY flag:

```python
import os

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)
```

### OS.rename( ):-
> Rename *files/directories*.
> The file/directories have to exist.
> 
> ![[Pasted image 20230810191537.png|700]]
```python
import os

for i in range(0,11):
os.rename(f'data/Day{i+1}', f"data/Tutorial{i+1}") # rename directories with a loop 
#          input folders   ,   new names

```
- Output:-
>![[Pasted image 20230810191720.png|700]]

### OS.remove( ):-
>Using the Os module we can remove a file in our system using the remove() method.

```python
import os #importing os module.

os.remove("file_name.txt") #removing the file.
```

---
> [!info] 
> OS module has a sub-module named PATH by using which we can perform many more functions.
### OS.path.exists( ):-
>This method **will check whether a file exists or not** by passing the name of the file as a parameter
```python
import os

result = os.path.exists("file_name") #giving the name of the file as a parameter.
print(result)


# output:-
False
```

### OS.path.getsize( ):-
>In this method, python will **give us the size of the file in bytes**. To use this method we need to pass the name of the file as a parameter.

```python
import os

size = os.path.getsize("filename")
print("Size of the file is", size," bytes.")


# Output:-
Size of the file is 192 bytes.
```


---
## Running system commands

>Finally, the os module provides functions for running system commands. 

### OS.system("<Command_name>"):-
>You can use the os.system("<Command_name>") function **to run a command and get the output:**

```python
import os
# Run the "ls" command and print the output
output = os.system("ls")
print(output)  


# Output: ['myfile.txt', 'otherfile.txt']
```

### os.popen( ):-
>You can use the os.popen function to **run a command and get the output as a file-like object**:
>
```python
import os

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  
# Output: 
# ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()
```
---

## misc:-

### OS.name( ):- 
>This function **gives the name of the operating system dependent module imported**.
> The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’.

```python
import os

print(os.name)  # output: posix
```

## [[47 - Exercise 4~ Solution|Next Lesson>>]]