# Learn how to reverse a String in Python.
# There is no built-in function to reverse a String in Python.

# The fastest (and easiest?) way is to use a slice that steps backwards, -1.

# Reverse the string "Hello World":
>>> txt = "Hello World"[::-1]
>>> print(txt)


# We have a string, "Hello World", which we want to reverse:
# The String to Reverse
>>> txt = "Hello World" [::-1]
>>> print(txt)


# Create a slice that starts at the end of the string, and moves backwards.
# In this particular example, the slice statement [::-1] is the same as [11:0:-1] which means start at position 11 (because "Hello "World" has 11 characters), end at position 0, move with the step -1, negative one, which means one step backwards.

# Slice the String
>>> txt = "Hello World" [::-1] 
>>> print(txt)

# Now we have a string txt that reads "Hello World" backwards.
# Print the String to demonstrate the result

# Print the List
>>> txt = "Hello World"[::-1] 
>>> print(txt)

# Create a Function
# If you like to have a function where you can send your strings, and return them backwards, 
# you can create a function and insert the code from the example above.

>>> def my_function(x):
      return x[::-1]

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt)
sdrawkcab ekil skool txet siht woh rednow I


# Create a function that takes a String as an argument.
# Create a Function
>>> def my_function(x): 
      return x[::-1]

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt)

# Slice the string starting at the end of the string and move backwards.

# Slice the String
>>> def my_function(x):
      return x [::-1] 

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt)

# Return the backward String
# Return the String
>>> def my_function(x):
      return x[::-1] 

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt )


# Call the function, with a string as a parameter:
# Call the Function
>>> def my_function(x):
      return x[::-1]

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt)


# Print the Result
>>> def my_function(x):
      return x[::-1]

>>> mytxt = my_function("I wonder how this text looks like backwards")
>>> print(mytxt)
