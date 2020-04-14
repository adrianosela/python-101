### Lesson 2 - Conditional Statements and Boolean Operators

Often in programming, we want to be able to conditionally run our code. That is, we dont always the same code to run. Programming languages like python provide a built-in way for code to run based on conditions -- conditional statements.

### Contents

* [2.0 - The `if()` Statement](#20---the-if-statement)
* [2.1 - The `else` Statement](#21---the-else-statement)
* [2.2 - The `elif()` Statement](#22---the-elif-statement)
* [2.3 - Logical (Boolean) Operators](#23---logical-operators)
* [2.4 - A Tangible Exercise](#24---a-tangible-exercise)

## 2.0 - The if() Statement

The `if()` statement is the basis of conditional programming. It takes a condition in, and the portion of code that it wraps will only be executed if the condition is true.

For example:

```
if (5 < 10):
	print("hey there!")
```

Will output, but:

```
if (5 < 4):
	print("hey there!")
```

will not!

Take a look at the file `if.py`, understand the code and run it.

## 2.1 - The else Statement

The `else` statement is always paired with an `if()` statement and encapsulates the portion of code to be executed when the condition in the `if()` is not true.

For example:

```
if (5 < 4):
	print("hey there!")
else:
	print("number too large :(")
```

Take a look at the file `else.py`, understand the code and run it.

## 2.2 - The elif() Statement

The `elif()` statement is used when we with to chain `if()` statements and check multiple conditions.

For example:

```
if (a > 0):
    print("your number is larger than 0")
elif(a < 0):
    print("your number is smaller than 0")
else:
    print("your number is exactly 0")
```

Take a look at the file `elif.py`, understand the code and run it.

## 2.3 - Logical Operators

Conditions can be combined using boolean operations in python.

For example consider two boolean variables `a`, and `b`.
Let `a` and `b` represent the statements `today is sunny`, and `today is warm` respectively.

Then an expression `c = a and b` reads as a single statement: `today is sunny and today is warm`

In the example above, we only look at the `and` operator. We also have an `or` operator, and a `not` operator, which behave exactly as you'd expect.

Take a look at the file `bools.py`, understand the code and run it. Get familiar with the logical operators in python.

## 2.4 - A Tangible Exercise:

> Note that this is entirely fictional

The government has claimed that if a given person has 4/8 of the following symptoms, they are very likely to have a new novel virus.

Write a program to do the following:

Ask the user their name, and age, as well as the following 8 questions:

* Do you have a cough?
* Do you have a fever?
* Do you have excessive fatigue?
* Do you have a shortness of breath?
* Do you have a phlegm?
* Do you have bodyaches?
* Do you have sore throat?
* Do you have a lack of appetite?

If the user reponds with the exact phrase 'yes', to at least four of the questions, print a phrase recommending they seek medical attention.

Otherwise, print a phrase to let them know that they are most likely OK.

In both cases, before printing the phrase, print the name and age of the user.

The solution can be found in `solution.py` to check your answers, don't cheat!

Note that there are many better ways to write this program than the solution, but this solution uses only the constructs we have learned thus far in this course.

