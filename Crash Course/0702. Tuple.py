# Tuple is immutable
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Create a Tuple:
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')

# Access Tuple Items: You can access tuple items by referring to the index number, inside square brackets:
# Return the item in position 1:
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple[1])
banana

# Loop Through a Tuple: You can loop through the tuple items by using a for loop.
# Iterate through the items and print the values:
>>> thistuple = ("apple", "banana", "cherry")
>>> for x in thistuple:
      print(x)
      
# Check if Item Exists, To determine if a specified item is present in a tuple use the in keyword:
# Check if "apple" is present in the tuple:
>>> thistuple = ("apple", "banana", "cherry")
>>> if "apple" in thistuple:
      print("Yes, 'apple' is in the fruits tuple")

# Tuple Length : To determine how many items a tuple has, use the len() method:
# Print the number of items in the tuple:
>>> thistuple = ("apple", "banana", "cherry")
>>> print(len(thistuple))


# Add Items: Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# You cannot add items to a tuple:
>>> thistuple = ("apple", "banana", "cherry")
>>> thistuple[3] = "orange" # This will raise an error
>>> print(thistuple)
TypeError: 'tuple' object does not support item assignment

# Remove Items : You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# The del keyword can delete the tuple completely:
>>> thistuple = ("apple", "banana", "cherry")
>>> del thistuple
>>> print(thistuple) #this will raise an error because the tuple no longer exists
NameError: name 'thistuple' is not defined

# The tuple() Constructor: It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:
>>> thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
>>> print(thistuple)
('apple', 'banana', 'cherry')

>>> t[0] = 'NEW'

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-44-97e4e33b36c2> in <module>()
----> 1 t[0] = 'NEW'

TypeError: 'tuple' object does not support item assignment
