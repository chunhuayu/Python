# There are three numeric types in Python:
# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:
>>> x = 1    # int
>>> y = 2.8  # float
>>> z = 1j   # complex
>>> print(type(x))
<class 'int'>

>>> print(type(y))
<class 'float'>

>>> print(type(z))
<class 'complex'>

>>> a = 35e3
>>> b = 12E4
>>> c = -87.7e100

>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'float'>
>>> print(type(c))
<class 'float'>

>>> e = 3+5j
>>> f = 5j
>>> k = -5j

>>> print(type(e))
<class 'complex'>
>>> print(type(f))
<class 'complex'>
>>> print(type(k))
<class 'complex'>


>>> 1 + 1
2

>>> 1 * 3
3

>>> 1 / 2
0.5

>>> 2 ** 4
16

>>> 4 % 2
0

>>> 5 % 2
1

>>> (2 + 3) * (5 + 5)
5
