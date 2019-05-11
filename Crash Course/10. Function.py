### functions : A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:

>>> def my_function():
      print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:

>>> def my_function():
      print("Hello from a function")
>>> my_function()
Hello from a function

# Parameters : Information can be passed to functions as parameter.
# Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
# The following example has a function with one parameter (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

>>> def my_function(fname):
      print(fname + " Refsnes")

>>> my_function("Emil")
Emil Refsnes
>>> my_function("Tobias")
Tobias Refsnes
>>> my_function("Linus")
Linus Refsnes

# Default Parameter Value : The following example shows how to use a default parameter value.
# If we call the function without parameter, it uses the default value:

>>> def my_function(country = "Norway"):
      print("I am from " + country)
>>> my_function("Sweden")
>>> my_function("India")
>>> my_function()
>>> my_function("Brazil")
I am from Sweden
I am from India
I am from Norway
I am from Brazil


# Passing a List as a Parameter
# You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as a parameter, it will still be a List when it reaches the function:

>>> def my_function(food):
      for x in food:
        print(x)
>>> fruits = ["apple", "banana", "cherry"]
>>> my_function(fruits)


# Return Values : To let a function return a value, use the return statement:
>>> def my_function(x):
      return 5 * x
>>> print(my_function(3))
>>> print(my_function(5))
>>> print(my_function(9))
15
25
45


# Recursion : Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
# or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
# We use the k variable as the data, which decrements (-1) every time we recurse. 
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
# Recursion Example

>>> def tri_recursion(k):
      if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
      else:
        result = 0
      return result
>>> print("\n\nRecursion Example Results")
>>> tri_recursion(6)
Recursion Example Results
1
3
6
10
15
21


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
