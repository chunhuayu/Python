# Dictionary : A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Create and print a dictionary:

>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
        }
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Accessing Items : You can access the items of a dictionary by referring to its key name, inside square brackets:
>>> Get the value of the "model" key:
>>> x = thisdict["model"]
Mustang


# There is also a method called get() that will give you the same result:
>>> Get the value of the "model" key:
>>> x = thisdict.get("model")
Mustang


# Change Values : You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
        }
>>> thisdict["year"] = 2018
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# Loop Through a Dictionary : You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
>>> for x in thisdict:
      print(x)
brand
model
year


# Print all values in the dictionary, one by one:
>>> for x in thisdict:
      print(thisdict[x])
Ford
Mustang
1964

# You can also use the values() function to return values of a dictionary:
>>> for x in thisdict.values():
      print(x)
Ford
Mustang
1964


# Loop through both keys and values, by using the items() function:
>>> for x, y in thisdict.items():
      print(x, y)
brand Ford
model Mustang
year 1964


# Check if Key Exists : To determine if a specified key is present in a dictionary use the in keyword:
>>> Check if "model" is present in the dictionary:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
        }
>>> if "model" in thisdict:
      print("Yes, 'model' is one of the keys in the thisdict dictionary")
Yes, 'model' is one of the keys in the thisdict dictionary


# Dictionary Length : To determine how many items (key-value pairs) a dictionary has, use the len() method.
# Print the number of items in the dictionary:
>>> print(len(thisdict))
3


# Adding Items : Adding an item to the dictionary is done by using a new index key and assigning a value to it:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> thisdict["color"] = "red"
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Removing Items : There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> thisdict.pop("model")
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> thisdict.popitem()
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang'}


# The del keyword removes the item with the specified key name:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> del thisdict["model"]
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}


# The del keyword can also delete the dictionary completely:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> del thisdict
>>> print(thisdict) #this will cause an error because "thisdict" no longer exists.
Traceback (most recent call last):
  File "demo_dictionary_del3.py", line 7, in <module>
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
NameError: name 'thisdict' is not defined


# The clear() keyword empties the dictionary:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> thisdict.clear()
>>> print(thisdict)
{}


# Copy a Dictionary : You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# Make a copy of a dictionary with the copy() method:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> mydict = thisdict.copy()
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Another way to make a copy is to use the built-in method dict().
# Make a copy of a dictionary with the dict() method:
>>> thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
>>> mydict = dict(thisdict)
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
>>> thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
