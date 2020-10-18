######################  NumPy Searching Array  #################################

# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

# Find the indexes where the value is 4 
import numpy as np
print('#####     Finding the indexes where the value is 4     #####')
arr = np.array([1,2,3,4,5,4,4])
print(np.where(arr == 4))
# The example above will return a tuple: (array([3, 5, 6],)
# Which means that the value 4 is present at index 3, 5, and 6.

# Find the indexes where the values are even:
print('#####     Finding the indexes where the values are even     #####')
arr = np.array([1,2,3,4,5,6])
print(np.where(arr%2 == 0))

# Find the indexes where the values are odd:
print('#####     Finding the indexes where the values are odd     #####')
arr = np.array([1,2,3,4,5,6])
print(np.where(arr%2 == 1))


######################  Search Sorted  #################################

# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.

# Find the indexes where the value 7 should be inserted 
print('#####     Finding the indexes wheer the value 7 should be inserted to maintaing the search order     #####')
arr = np.array([6,7,8,9])
print(np.searchsorted(arr,7))
# Example explained: The number 7 should be inserted on index 1 to remain the sort order.
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

######################  Search From the Right Side  #################################

# By default the lest most index is returned, but we can give side='right' to return the right most index instead.
# Find the indexes where the value 7 should be inserted, starting from the right:
print('#####     Finding the indexes where the value 7 should be inserted, starting from the right     #####')
arr = np.array([6,7,8,9])
print(np.searchsorted(arr,7,side='right'))

######################  Multiple Values  #################################

# To search for more than one value, use an array with the specified values.

# Find the indexes where the values 2,4, and 6 should be inserted 
print('#####     Finding the indexes where the values 2,4,6 should be inserted in order to maintain the order     #####')
arr = np.array([1,3,5,7])
print(np.searchsorted(arr,[2,4,6]))
# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.