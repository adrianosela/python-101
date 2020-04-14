### Lesson 3 - Lists, Loops, and Comments

Often in programming, we want to be able to run a portion of our code multiple times such that a given portion of code does not have to be rewritten. Loops such as `for` and `while` loops allow us to run a given portion of code for as long as the condition in the loop definition is true.

Our programs are getting somewhat complex and may be hard to understand. In this lesson we introduce comments and how to comment out your code for others and yourself to read. The best code is often not the fastest or smallest, but the most readable.

### Contents

* [3.0 - Lists](#30---lists)
* [3.1 - Indexing](#31---indexing)
* [3.2 - The `for` loop](#32---the-for-loop)
* [3.3 - The `range` function](#33---the-range-function)
* [3.4 - The `while` loop](#34---the-while-loop)
* [3.5 - Comments](#35---comments)

## 3.0 - Lists:

Lists are one of the collection data types in the Python programming language. Lists are ordered, and changeable (formally: mutable). In Python, lists are written with square brackets:

```
my_list = ["apple", "orange", "grapefruit", "banana", "cherry"]
```

Take a look at the file `lists.py`, understand the code and run it.

Lists in python can contain any type, or combination of types, in them:

```
my_list = ["apple", False, 47.653, 4]
```

Take a look at the file `lists2.py`, understand the code and run it.

## 3.1 - Indexing:

We have seen how to create lists, but what if we want to access specific things inside them?

Most programming languages (i.e. NOT math languages such as MATLAB), start indexing from zero (0), that is, the first element in the list is accessed with index 0.

For example:

For the list `my_list = ["apple, "orange", "banana", "cherry"]`, if we wanted to access the first element, `"apple"`, we use the following notation:

```
my_list[0]
```

To access the second element, `"orange"`:

```
my_list[1]
```

... and so on.

Before looking at a code example, it is worth mentioning that Python allows us to index from the end of the list using negative indices. 

For example:

For the list `my_list = ["apple, "orange", "banana", "cherry"]`, if we wanted to access the last element, `"cherry"`, we use the following notation:

```
my_list[-1]
```

Take a look at the file `indexing.py`. Understand the code, get familiar with python's indexing syntax. Run the code.

### **IndexError: list index out of range**

Note that accessing lists haphazardly is dangerous and can result in your program/application shutting down (stopping).

Take a look at the file `index_error.py`. Notice that we are indexing an element that does not exist (index is out of the range/size of the list). Run the code and take a look at the output.

It is also worth mentioning that you should not be afraid of errors; you should be grateful for them! Catching an error early on while writing code is better than catching them when they are released to users!

I encourage you to take a good read at the error message every single time you encounter an error. You will get acquainted with a lot of types of errors and you will become proficient at understanding what needs fixing.

Error messages, or `exceptions` as they are called in Python, will give you the line number where the program went wrong, so you can easily go back to that line and fix any syntax error or other errors.

## 3.1 - The `for` Loop:

In software we rarely ever access list elements with explicit indices as shown above. Python provides syntax for performing an operation for every item on a list, the `for` loop.

Imagine you wanted to count how many times, the string "apples" occurs in a list. A naive implementation would try to explicitly index every element in a list as follows:

```
my_list = ["apples", "oranges", "bananas", "apples", "apples", "lemon"]

appleCount = 0

if my_list[0] == "apples":
    appleCount = appleCount + 1

if my_list[1] == "apples":
    appleCount = appleCount + 1

if my_list[2] == "apples":
    appleCount = appleCount + 1

if my_list[3] == "apples":
    appleCount = appleCount + 1

if my_list[4] == "apples":
    appleCount = appleCount + 1

if my_list[5] == "apples":
    appleCount = appleCount + 1

print(appleCount)
```

An shorter way to do this using a for loop would look as follows:

```
my_list = ["apples", "oranges", "bananas", "apples", "apples", "lemon"]

appleCount = 0

for fruit in my_list:
    if fruit == "apples":
        appleCount = appleCount + 1

print(appleCount)
``` 

Note that this syntax is better than explicit indexing because we don't need to know the size of the list in advance, we will never encounter a `"list index out of range"` error.

Run the files `apples_bad.py` and `apples_good.py` and see for yourself that they are functionally equivalent. Convince yourself that `apples_good.py` is a better implementation.

## 3.2 - The `range` function:


