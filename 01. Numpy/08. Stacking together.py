# Stacking together different arrays
# Several arrays can be stacked together along different axes:
>>>
>>> a = np.floor(10*np.random.random((2,2)))
>>> a
array([[ 8.,  8.],
       [ 0.,  0.]])
>>> b = np.floor(10*np.random.random((2,2)))
>>> b
array([[ 1.,  8.],
       [ 0.,  4.]])
>>> np.vstack((a,b))
array([[ 8.,  8.],
       [ 0.,  0.],
       [ 1.,  8.],
       [ 0.,  4.]])
>>> np.hstack((a,b))
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])


# The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D arrays:
>>>
>>> from numpy import newaxis
>>> np.column_stack((a,b))     # with 2D arrays
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
>>> a = np.array([4.,2.])
>>> b = np.array([3.,8.])
>>> np.column_stack((a,b))     # returns a 2D array
array([[ 4., 3.],
       [ 2., 8.]])
>>> np.hstack((a,b))           # the result is different
array([ 4., 2., 3., 8.])
>>> a[:,newaxis]               # this allows to have a 2D columns vector
array([[ 4.],
       [ 2.]])
>>> np.column_stack((a[:,newaxis],b[:,newaxis]))
array([[ 4.,  3.],
       [ 2.,  8.]])
>>> np.hstack((a[:,newaxis],b[:,newaxis]))   # the result is the same
array([[ 4.,  3.],
       [ 2.,  8.]])


# On the other hand, the function row_stack is equivalent to vstack for any input arrays. 
# In general, for arrays of with more than two dimensions, hstack stacks along their second axes, 
# vstack stacks along their first axes, and concatenate allows for an optional arguments giving the number of the axis 
# along which the concatenation should happen.

# Note
# In complex cases, r_ and c_ are useful for creating arrays by stacking numbers along one axis. 
# They allow the use of range literals (“:”)
>>>
>>> np.r_[1:4,0,4]
array([1, 2, 3, 0, 4])
# When used with arrays as arguments, r_ and c_ are similar to vstack and hstack in their default behavior, 
# but allow for an optional argument giving the number of the axis along which to concatenate.


# stack : join a sequence of arraysalong a new axis.
# vstack : Stack arrays in sequence vertically (row wise).
# dstack : Stack arrays in sequence depth wise (along third axis).
# concatenate : Join a sequence of arrays along an existing axis.
# hsplit : Split array along second axis.
# block : Assemble arrays from blocks.
