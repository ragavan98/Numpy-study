######################  NumPy Sorting Arrays  #################################

# Sorting means putting elements in a ordered sequence.
# Ordered sequence is any sequence that has an order corresponding - 
# to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Sort the array
import numpy as np
print("#####     Sorting the array     #####")
arr = np.array([3,0,2,5])
print(np.sort(arr))
# Note: This method returns a copy of the array, leaving the original array unchanged.

# You can also sort arrays of strings, or any other data type:

# Sort the array alphabetically
print("#####    Sorting the array alphabetically     #####")
arr = np.array(['vinith kumar','suganthan','ragavan'])
print(np.sort(arr))

# Sort a boolean array:
print("##### Sorting a boolean array     #####")
arr = np.array([True, False , True ])
print(np.sort(arr))

# If you use the sort() method on a 2-D array, both arrays will be sorted:
# Sorting a 2-D Array
print("#####     Sorting a 2-D Array     #####")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))