>>> [1,2,3]
[1,2,3]

>>> ['hi',1,[1,2]]
['hi',1,[1,2]]

# create a list
>>> thislist = ["apple", "banana", "cherry"]
>>> print(thislist)

>>> my_list = ['a','b','c']
>>> my_list.append('d')
>>> my_list
['a', 'b', 'c', 'd']

# You access the list items by referring to the index number:
>>> my_list[0]
'a'

>>> my_list[1]
'b'

>>> my_list[1:]
['b', 'c', 'd']

>>> my_list[:1]
['a']

# To change the value of a specific item, refer to the index number:
>>> my_list[0] = 'NEW'
>>> my_list
['NEW', 'b', 'c', 'd']

>>> nest = [1,2,3,[4,5,['target']]]
>>> nest[3]
[4, 5, ['target']]

>>> nest[3][2]
['target']

>>> nest[3][2][0]
'target'

# You can loop through the list items by using a for loop:
>>> thislist = ["apple", "banana", "cherry"]
>>> for x in thislist:
        print(x)
apple
banana
cherry

# Print the second item in the fruits list.
>>> fruits = ["apple", "banana", "cherry"]
>>> print(fruits[1])


# Change the value from "apple" to "kiwi", in the fruits list.
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits[0]="kiwi"

# Use the append method to add "orange" to the fruits list.
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.append("orage")

# Use the insert method to add "lemon" as the second item in the fruits list.
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.insert(1,"lemon')

# Use the remove method to remove "banana" from the fruits list.
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.remove("banana")
