# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax : lambda arguments : expression
# The expression is executed and the result is returned:

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
>>> x = lambda a : a + 10
>>> print(x(5))
15

# Lambda functions can take any number of arguments:
# A lambda function that multiplies argument a with argument b and print the result:
>>> x = lambda a, b : a * b
>>> print(x(5, 6))
30

# A lambda function that sums argument a, b, and c and print the result:
>>> x = lambda a, b, c : a + b + c
>>> print(x(5, 6, 2))
13

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

>>> def myfunc(n):
      return lambda a : a * n
      
# Use that function definition to make a function that always doubles the number you send in:
>>> def myfunc(n):
      return lambda a : a * n
>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22

# Or, use the same function definition to make a function that always triples the number you send in:
>>> def myfunc(n):
      return lambda a : a * n
>>> mytripler = myfunc(3)
>>> print(mytripler(11))
33

# Or, use the same function definition to make both functions, in the same program:
>>> def myfunc(n):
      return lambda a : a * n
>>> mydoubler = myfunc(2)
>>> mytripler = myfunc(3)
>>> print(mydoubler(11)) 
>>> print(mytripler(11))
22
33

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
