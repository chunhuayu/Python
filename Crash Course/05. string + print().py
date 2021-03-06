# String

>>> "Hello, world!"
'Hello, world!'

>>> "Let's go"
"Let's go"

>>> 'Let\'s go'
"Let's go"

>>> "\"Hello, world!\" She said "
' "Hello, world!" She said'


>>> x = 'Hello, '
>>> x
'Hello, '

>>> y = 'world!'
>>> y
'world!'

# To combine both text and a variable, Python uses the + character:
>>> x+y
'Hello, world!'

# \n represents to print something in new line with print(),so hear it does not work.
>>> 'Hello,\nworld!'
'Hello,\nworld!'


# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:

>>> print(x)
Hello, 

>>> x = "awesome"
>>> print("Python is " + x)
Python is awesome

>>> print('Hello,\nworld!')
Hello,
world!

>>> num = 12
>>> name = 'Sam'
>>> print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))
My number is: 12, and my name is: Sam

>>> print('My number is: {}, and my name is: {}'.format(num,name))
My number is: 12, and my name is: Sam

# Error is showing up when:
>>> x = 5
>>> y = "John"
>>> print(x + y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
# Use the len method to print the length of the string.
>>> x = "Hello World"
>>> print(len(x))

# Get the first character of the string txt.
>>> txt = "Hello World"
>>> x = txt[0]

# Get the characters from position 2 to position 5 (not included).
>>> txt = "Hello World"
>>> x = txt[2:5]

# Return the string without any whitespace at the beginning or the end.
>>> txt = " Hello World "
>>> x = txt.strip()

# Convert the value of txt to upper case.
>>> txt = "Hello World"
>>> x = txt.upper()

# Convert the value of txt to lower case.
>>> txt = "Hello World"
>>> x = txt.lower()

# Replace the character H with a J.
>>> txt = "Hello World"
>>> txt = txt.replace("H","J")
