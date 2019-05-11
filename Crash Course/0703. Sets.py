# Sets: A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# Create a Set:
>>> thisset = {"apple", "banana", "cherry"}
>>> print(thisset)

>>> {1,2,3}
{1, 2, 3}

>>> {1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}
{1, 2, 3}

# Access Items : You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, 
# or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:

>>> thisset = {"apple", "banana", "cherry"}
>>> for x in thisset:
      print(x)
banana
cherry
apple

# Check if "banana" is present in the set:
>>> thisset = {"apple", "banana", "cherry"}
>>> print("banana" in thisset)
True

# Change Items : Once a set is created, you cannot change its items, but you can add new items.

# Add Items : To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.
# Add an item to a set, using the add() method:
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.add("orange")
>>> print(thisset)
{'apple', 'banana', 'orange', 'cherry'}

# Add multiple items to a set, using the update() method:
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.update(["orange", "mango", "grapes"])
>>> print(thisset)
{'orange', 'mango', 'cherry', 'grapes', 'banana', 'apple'}

# Get the Length of a Set : To determine how many items a set has, use the len() method.
# Get the number of items in a set:
>>> thisset = {"apple", "banana", "cherry"}
>>> print(len(thisset))
3

# Remove Item : To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.remove("banana")
>>> print(thisset)
{'apple', 'cherry'}

# Note: If the item to remove does not exist, remove() will raise an error.
# Remove "banana" by using the discard() method:
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.discard("banana")
>>> print(thisset)
{'cherry', 'apple'}

# Note: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed. 
# The return value of the pop() method is the removed item.
# Remove the last item by using the pop() method:
>>> thisset = {"apple", "banana", "cherry"}
>>> x = thisset.pop()
>>>print(x)
cherry
>>> print(thisset)
{'banana', 'cherry'}

# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
# The clear() method empties the set:
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.clear()
>>> print(thisset)
set()

# The del keyword will delete the set completely:
>>> thisset = {"apple", "banana", "cherry"}
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "demo_set_del.py", line 5, in <module>
    print(thisset) #this will raise an error because the set no longer exists
NameError: name 'thisset' is not defined

# The set() Constructor: It is also possible to use the set() constructor to make a set.
# Using the set() constructor to make a set:
>>> thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
>>> print(thisset)
{'cherry', 'banana', 'apple'}

# Check if "apple" is present in the fruits set.
>>> fruits = {"apple", "banana", "cherry"}
>>> if ("apple" in  fruits):
      print("Yes, apple is a fruit!")

# Use the add method to add "orange" to the fruits set.
>>> fruits = {"apple", "banana", "cherry"}
>>> fruits.add("orange")

# Use the correct method to add multiple items (more_fruits) to the fruits set.
>>> fruits = {"apple", "banana", "cherry"}
>>> more_fruits = ["orange", "mango", "grapes"]
>>> fruits.update(more_fruits)

# Use the remove method to remove "banana" from the fruits set.
>>> fruits = {"apple", "banana", "cherry"}
>>> fruits.remove("banana")

# Use the discard method to remove "banana" from the fruits set.
>>> fruits = {"apple", "banana", "cherry"}
>>> fruits.discard("banana")
