### functions
# docstring: describe what your function does
>>> def my_func(param1='default'):
        """
        Docstring goes here.
        """
        print(param1)


>>> my_func
<function __main__.my_func>

>>> my_func()
default

>>> my_func('new param')
new param

>>> my_func(param1='new param')
new param

>>> def square(x):
        return x**2

>>> out = square(2)
>>> print(out)
4

### lambda expressions

>>> def times2(var):
        return var*2
>>> times2(2)
4

# lambda expression does not return any value
>>> lambda var: var*2
<function __main__.<lambda>>

### map and filter
# executive the same function
>>> seq = [1,2,3,4,5]
# map function does not return value, return the local memory address
>>> map(times2,seq)
seq = [1,2,3,4,5] 
<map at 0x105316748>
# by using list() to return the value of map() function
>>> list(map(times2,seq))
[1, 4, 6, 8, 10]

>>> list(map(lambda var: var*2,seq))
[1, 4, 6, 8, 10]

# filter function returns the local memory address.
>>> filter(lambda item: item%2 == 0,seq)
<filter at 0x105316ac8>

# by using list fuction to return the output value
# filter the true value.
>>> list(filter(lambda item: item%2 == 0,seq))
[2, 4]
