### methods

>>> st = 'hello my name is Sam'
# return the lower case of st, but won't change the value of st
>>> st.lower()
'hello my name is sam'

# return the upper case of st, but won't change the value of st
>>> st.upper()
'HELLO MY NAME IS SAM'

# Split a string into a list where each word is a list item, default separator is any whitespace
>>> st.split()
['hello', 'my', 'name', 'is', 'Sam']

>>> tweet = 'Go Sports! #Sports'

# specify the separator is '#'
>>> tweet.split('#')
['Go Sports!', 'Sports']

>>>tweet.split('#')[1]
'Sports'

>>> d = {'key1':'item1','key2':'item2'}
>>> d.keys()
dict_keys(['key1', 'key2'])

>>> d.items()
				      
dict_items([('key1', 'item1'), ('key2', 'item2')])

>>> lst = [1,2,3]

>>> lst.pop()
3

>>> lst
[1,2]

>>> 'x' in [1,2,3]
False

>>> 'x' in ['x','y','z']
True
