# NumPy provides familiar mathematical functions such as sin, cos, and exp. 
# In NumPy, these are called “universal functions”(ufunc). 
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
>>>
>>> B = np.arange(3)
>>> B
array([0, 1, 2])

>>> np.exp(B)
array([ 1.        ,  2.71828183,  7.3890561 ])

>>> np.sqrt(B)
array([ 0.        ,  1.        ,  1.41421356])

>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([ 2.,  0.,  6.])


>>> np.all([[True,False],[True,True]])
False

>>>
>>> np.all([[True,False],[True,True]], axis=0)
array([ True, False])

>>>
>>> np.all([-1, 4, 5])
True

>>>
>>> np.all([1.0, np.nan])
True

>>>
>>> o=np.array([False])
>>> z=np.all([-1, 4, 5], out=o)
>>> id(z), id(o), z                             
(28293632, 28293632, array([ True]))

# any
>>> np.any([[True, False], [True, True]])
True

>>>
>>> np.any([[True, False], [False, False]], axis=0)
array([ True, False])

>>>
>>> np.any([-1, 0, 5])
True

>>>
>>> np.any(np.nan)
True

>>>
>>> o=np.array([False])
>>> z=np.any([-1, 4, 5], out=o)
>>> z, o
(array([ True]), array([ True]))
>>> # Check now that z is a reference to o
>>> z is o
True
>>> id(z), id(o) # identity of z and o              
(191614240, 191614240)


# numpy.apply_along_axis
>>>
>>> def my_func(a):
...     """Average first and last element of a 1-D array"""
...     return (a[0] + a[-1]) * 0.5
>>> b = np.array([[1,2,3], [4,5,6], [7,8,9]])
>>> np.apply_along_axis(my_func, 0, b)
array([ 4.,  5.,  6.])
>>> np.apply_along_axis(my_func, 1, b)
array([ 2.,  5.,  8.])


# For a function that returns a 1D array, the number of dimensions in outarr is the same as arr.
>>>
>>> b = np.array([[8,1,7], [4,3,9], [5,2,6]])
>>> np.apply_along_axis(sorted, 1, b)
array([[1, 7, 8],
       [3, 4, 9],
       [2, 5, 6]])


# For a function that returns a higher dimensional array, those dimensions are inserted in place of the axis dimension.
>>>
>>> b = np.array([[1,2,3], [4,5,6], [7,8,9]])
>>> np.apply_along_axis(np.diag, -1, b)
array([[[1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]],
       [[4, 0, 0],
        [0, 5, 0],
        [0, 0, 6]],
       [[7, 0, 0],
        [0, 8, 0],
        [0, 0, 9]]])
