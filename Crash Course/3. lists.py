>>> [1,2,3]
[1,2,3]

>>> ['hi',1,[1,2]]
['hi',1,[1,2]]

>>> my_list = ['a','b','c']
>>> my_list.append('d')
>>> my_list
['a', 'b', 'c', 'd']

>>> my_list[0]
'a'

>>> my_list[1]
'b'

>>> my_list[1:]
['b', 'c', 'd']

>>> my_list[:1]
['a']

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
