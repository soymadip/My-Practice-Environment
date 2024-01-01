# readlines() method

The readline() method **reads a single line from the file**. 
- If we want to read multiple lines, we can use a loop.

```python
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

```
The readlines() method reads all the lines of the file and returns them as a list of strings.

# writelines() method
The writelines() method in Python *writes a sequence of strings to a file*. The sequence can be _any iterable object_, such as a __list or a tuple__.

Here's an example of how to use the writelines() method:
```python
f = open('myfile.txt', 'w')
lines = ['line1', 'line2', 'line3']
f.writelines(lines)
f.close()

# output in myfiles.txt:

line1line2line3 # without any spaces
```

> [!example] info
>  if we wanna add space or write strings line by line, we have to add them right in the string.
>```python
>f = open('myfile.txt', 'w')
>lines = ['line1\n', 'line2\n', 'line3\n'] # The \n characters are used to add newline characters to the end of each string.
>f.writelines(lines)
>f.close()
>
> #output in myfiles.txt
>line 1
>line 2
>line 3
>
>```

>Keep in mind that the __writelines()__ method _does not add newline characters between the strings in the sequence_. 
>So this method _can't be used for long list or in case of unchangeable lists_.
> >In that case, you can _use a loop to write each string separately_:

```python
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
```

It is also a good practice to close the file after you are done with it.

## [[51 - seek() and tell() functions|Next Lesson>>]]