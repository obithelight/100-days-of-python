# Type Error, Type Checking, and Type Conversions

When we happen to run a program like this:


```
len(1234)
```

We get an error:


```
len(1234)
TypeError: object of type 'int' has no len()
```

It gave us a TypeError because we gave the len function a number(integer) instead f a string.

# Data types and Functions

Data types and functions can be likened to a potato chip machine that takes in only potatoes and gives out fries(chips). Let's say we took the same machine that normally processes potatoes and gave it a rock; there would be problems(errors). That's what happened with the len() function we used earlier. We gave it an integer instead of a string, which is not used for processing, so it gave us an error.

let's treat another exampleí²ªíº€

> A program that reports on the length of your name

```python
num_char = len(input("What is your name? "))
print("Your name has " + num_char + " characters.")
```

That code is going to give us errors:

```
print("Your name has " + num_char + " characters.")
          ~~~~~~~~~~~~~~~~~^~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

As you can see from that error, we can only concatenate strings not concatenate strings to integers so we got a type error.

Let's check the data type of the num_char variable used in our function. We can check the type of a variable using the type() function.

```python
print(type(num_char))
```

**Result**

```
<class 'int'>
```

Adding a string to an integer does not make any sense and that is the reason for the TypeError.

> You can solve this error using type conversion(also called type casting)

# Type Conversion(Type casting)

This is the process of changing a piece of data from one data type to another. Building upon our existing program, we know that the num_char variable has the data type of int. We should convert it to string so our program does not break anymore

```
num_char = len(input("What is your name? "))
num_char = str(num_char)
print("Your name has " + num_char + " characters.")
```

> That program works perfectly well 

We took an integer data type and converted it into string using the str() function which takes an object and converts it into strings.


> We have good news !

You are not limited to converting numbers to strings. You can convert a whole bunch of data types. There are other functions like float(), and int() which convert any data type to float and integer respectively.

# Examples

**Code:**

```python
a = float(123)
print(type(a))
```

**Result:**

```
<class 'float'>
```

**Code:**
```
print(70 + float("100.5"))
```

**Result:**
```
170.5
```

**Code:**
```
print(str(70) + str(100))
```

**Result:**
```
70100
```
