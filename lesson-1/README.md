### Lesson 1 - Diving Into Python

Enough computer systems background for now, lets dive into the code.

### Contents

* [1.0 - Python Files](#10---python-files-and-text-editor)

## 1.0 - Python Files and Text Editor

Python files are typically named with the `.py` file extension. That is, python files are named as `file.py`.

Make your first python file with the Unix command to create a file:

```
$ touch hello-world.py
```

To edit the file you will need a text editor. For beginners learning python, I recommend [PyCharm](https://www.jetbrains.com/pycharm/).

> Note that text editors are no different than say, Microsoft Word. You can go ahead and write code there, but I wouldn't recommend it. Text editors are designed to help you write software by including common programming utilities like error checking, running code, formatting, etc.

You can download PyCharm with brew:

```
brew cask install pycharm
```

## 1.1 - Your First Python Program

Open, the file you've just created in your favorite text editor.

Type the following statement into the file:

```
print("Hello, World!")
```

Save the changes to the file, and run the code inside PyCharm -- you can figure that one out.

Alternatively, you can also run the python file from the command line (terminal) as follows:

```
$ python hello-world.py
```

Horray! You wrote (and ran) your first program! Throughout the rest of this lesson we will cover the very basics of Python.

 
## 1.2 - Literals 

In this section we will examine built-in types, also called literals. These are *things* that we use to define real world occurences when writing software.

For example, to represent 10 apples, the **integer** 10 can be used. To represent $15.99 dollars, the **floating-point** 15.99 can be used. To represent the name Adriano, the **string** "Adriano" can be used, and so on.

Later on we will look at more complex types such as lists and custom types.

### Boolean:

Booleans represent one of two values - True or False

Type the following lines into a new file - `booleans.py`:

```
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

What do you think will be printed when you run the program?
Try it out!

Soon you will realize that `True` is printed whenever the statement is true, and `False` whenever it is not.

These "booleans" will come in handy later on when we look at looping and conditional (if/else) statements.

### Numbers:

There are three numeric types in Python:

* **Int:** or integer, is a whole number, positive or negative, without decimals, of unlimited length.

* **Float:** or "floating point number" is a number, positive or negative, containing one or more decimals.

* **Complex:** are written with a "j" as the imaginary part:

Type the following lines into a new file - `numbers.py` and run it:

```
x = 1
y = 2.8
z = 1j

print(x)
print(y)
print(z)
```

Can you distinguish between integer, float, and complex numbers?

Note that you can find the type of a variable by using the ```type(variable)``` function as follows (output on right):

![](../.media/types.png)

### Strings:

String literals in python are surrounded by either single quotation marks, or double quotation marks.

```'hello'``` is the same as ```"hello"```.

Type the following lines into a new file - `strings.py` and run it:

```
a = "Hello"
print(a)
```