# Learn how to remove duplicates from a List in Python.

# Remove any duplicates from a List:

>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list(dict.fromkeys(mylist))
>>> print(mylist)

# First we have a List that contains duplicates:

# A List with Duplicates
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list(dict.fromkeys(mylist))
>>> print(mylist)

# Create a dictionary, using the List items as keys. 
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.

# Create a Dictionary
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list( dict.fromkeys(mylist) )
>>> print(mylist)

# Then, convert the dictionary back into a list:

# Convert Into a List
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list( dict.fromkeys(mylist) ) 
>>> print(mylist)

# Now we have a List without any duplicates, and it has the same order as the original List.

# Print the List to demonstrate the result

# Print the List
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list(dict.fromkeys(mylist))
>>> print(mylist)

# Create a Function
# If you like to have a function where you can send your lists, and get them back without duplicates, 
# you can create a function and insert the code from the example above.


>>> def my_function(x):
      return list(dict.fromkeys(x))

>>> mylist = my_function(["a", "b", "a", "c", "c"])

>>> print(mylist)


# Example Explained
# Create a function that takes a List as an argument.

# Create a Function
>>> def my_function(x): 
      return list(dict.fromkeys(x))

>>> mylist = my_function(["a", "b", "a", "c", "c"])

>>> print(mylist)

# Create a dictionary, using this List items as keys.
# Create a Dictionary
>>> def my_function(x):
      return list( dict.fromkeys(x) )

>>> mylist = my_function(["a", "b", "a", "c", "c"])
>>> print(mylist)

# Convert the dictionary into a list.
# Convert Into a List
>>> def my_function(x):
      return list( dict.fromkeys(x) ) 

>>> mylist = my_function(["a", "b", "a", "c", "c"])
>>> print(mylist)

# Return the list
# Return List
>>> def my_function(x):
      return list(dict.fromkeys(x))

>>> mylist = my_function(["a", "b", "a", "c", "c"])

>>> print(mylist)

# Call the function, with a list as a parameter:

# Call the Function
>>> def my_function(x):
      return list(dict.fromkeys(x))

>>> mylist = my_function(["a", "b", "a", "c", "c"])
>>> print(mylist)

# Print the result:
# Print the Result
>>> def my_function(x):
      return list(dict.fromkeys(x))

>>> mylist = my_function(["a", "b", "a", "c", "c"])
>>> print(mylist)
