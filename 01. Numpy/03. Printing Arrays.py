# Printing Arrays
# When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
##### the last axis is printed from left to right,
##### the second-to-last is printed from top to bottom,
##### the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

# One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.

>>>
>>> a = np.arange(6)                         # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4,3)           # 2d array
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2,3,4)         # 3d array
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]
 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]


# See below to get more details on reshape.
# If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:

>>>
>>> print(np.arange(10000))
[   0    1    2 ..., 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100,100))
[[   0    1    2 ...,   97   98   99]
 [ 100  101  102 ...,  197  198  199]
 [ 200  201  202 ...,  297  298  299]
 ...,
 [9700 9701 9702 ..., 9797 9798 9799]
 [9800 9801 9802 ..., 9897 9898 9899]
 [9900 9901 9902 ..., 9997 9998 9999]]


# To disable this behaviour and force NumPy to print the entire array, you can change the printing options 
# using set_printoptions.
>>>
>>> np.set_printoptions(threshold=np.nan)
