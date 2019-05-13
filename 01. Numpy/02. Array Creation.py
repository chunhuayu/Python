# There are several ways to create arrays.

# For example, you can create an array from a regular Python list or tuple using the array function. 
# The type of the resulting array is deduced from the type of the elements in the sequences.

>>>
>>> import numpy as np
>>> a = np.array([2,3,4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')

# A frequent error consists in calling array with multiple numeric arguments, 
# rather than providing a single list of numbers as an argument.
>>>
>>> a = np.array(1,2,3,4)    # WRONG
>>> a = np.array([1,2,3,4])  # RIGHT


# array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into 
# three-dimensional arrays, and so on.
>>>
>>> b = np.array([(1.5,2,3), (4,5,6)])
>>> b
array([[ 1.5,  2. ,  3. ],
       [ 4. ,  5. ,  6. ]])
       
       
# The type of the array can also be explicitly specified at creation time:
>>>
>>> c = np.array( [ [1,2], [3,4] ], dtype=complex )
>>> c
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])


# Often, the elements of an array are originally unknown, but its size is known. Hence, 
# NumPy offers several functions to create arrays with initial placeholder content. 
# These minimize the necessity of growing arrays, an expensive operation.
# The function zeros creates an array full of zeros, the function ones creates an array full of ones, 
# and the function empty creates an array whose initial content is random and depends on the state of the memory. 
# By default, the dtype of the created array is float64.
>>>
>>> np.zeros( (3,4) )
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
>>> np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
array([[[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]],
       [[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]]], dtype=int16)
>>> np.empty( (2,3) )                                 # uninitialized, output may vary
array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
       [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])


# To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
>>>
>>> np.arange( 10, 30, 5 )
array([10, 15, 20, 25])
>>> np.arange( 0, 2, 0.3 )                 # it accepts float arguments
array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])


# When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, 
# due to the finite floating point precision. For this reason, it is usually better to use the function linspace that receives 
# as an argument the number of elements that we want, instead of the step:
>>>
>>> from numpy import pi
>>> np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
>>> x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
>>> f = np.sin(x)

# numpy.array
>>>
>>> np.array([1, 2, 3])
array([1, 2, 3])


# Upcasting:
>>>
>>> np.array([1, 2, 3.0])
array([ 1.,  2.,  3.])

# More than one dimension:
>>>
>>> np.array([[1, 2], [3, 4]])
array([[1, 2],
       [3, 4]])

# Minimum dimensions 2:
>>>
>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])

# Type provided:
>>>
>>> np.array([1, 2, 3], dtype=complex)
array([ 1.+0.j,  2.+0.j,  3.+0.j])


# Data-type consisting of more than one element:
>>>
>>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
>>> x['a']
array([1, 3])

# Creating an array from sub-classes:
>>>
>>> np.array(np.mat('1 2; 3 4'))
array([[1, 2],
       [3, 4]])
>>>
>>> np.array(np.mat('1 2; 3 4'), subok=True)
matrix([[1, 2],
        [3, 4]])


# empty_like : Return an empty array with shape and type of input.
# ones_like : Return an array of ones with shape and type of input.
# zeros_like : Return an array of zeros with shape and type of input.
# full_like : Return a new array with shape of input filled with value.
# empty : Return a new uninitialized array.
# ones : Return a new array setting values to one.
# zeros : Return a new array setting values to zero.
# full : Return a new array of given shape filled with value.


# See also : linspace, numpy.random.rand, numpy.random.randn, fromfunction, fromfile
