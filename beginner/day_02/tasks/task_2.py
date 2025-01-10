# Type Error, Checking, and Conversion
'''
TypeError
These errors occur when you are using the wrong data type. e.g. len(12345)

Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).
'''
# 1. Fix the len() function so it has no more warnings or errors.
# print(len(1234))

print(len("1234"))

'''
Type Checking
You can check the data type of any value or variable in python using the type() function.

print(type("abc")) #will give you <class 'str'>
'''
# 2. Write out 4 type checks to print all 4 data types
print(type("obi"))
print(type(123))
print(type(5.8))
print(type(True))

'''
Type Conversion
You can convert data into different data types using special functions. e.g.

float()

int()

str()
'''
# 3. Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name: ")))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))
