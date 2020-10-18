######################  NumPy Splitting Array  #################################

# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Split the array in 3 parts
import numpy as np
print('#####     Splitting the array in 3 parts     #####')
arr = np.array([1,2,3,4,5,6])
print(np.array_split(arr,3))
# Note: The return value is an array containing three arrays.
# If the array has less elements than required, it will adjust from the end accordingly.

# Split the array in 4 parts:
print("#####     Splitting the array in 4 parts     #####")
arr = np.array([1,2,3,4,5,6])
print(np.array_split(arr,4)) 
# If the array has less elements than required,-
# it will adjust from the end accordingly.



# Note: We also have the method split() available -
# but it will not adjust the elements when elements -
# are less in source array for -
# splitting like in example above, array_split() worked -
# properly but split() would fail.


######################  Split Into Arrays  #################################

# The return value of the array_split() method is an -
# array containing each of the split as an array 
# If you split an array into 3 arrays, you can acess -
# them from the result just like any array element :

# Access the splitted array
print('#####     Accessing the splitted array     #####')
arr = np.array([1,2,3,4,5,6])
newArr = np.array_split(arr,3)
print(newArr[0])
print(newArr[1])
print(newArr[2])

# Split the 2-D array into three 2-D arrays.
print('#####     Splitting the 2-D array into three 2-D arrays     #####')
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print(np.array_split(arr,3))
# The example above returns three 2-D arrays
# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

# Split the 2-D array into three 2-D arrays.
print('#####     Splitting the 2-D array into three 2-D arrays     #####')
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
print(np.array_split(arr,3))
# The example above returns three 2-D arrays.

# In addition, you can specify which axis you want to do the split around.
# The example below also returns three 2-D arrays, but they are split along the row (axis=1).

# Split the 2-D array into three 2-D arrays along rows.
print("#####     Splitting the 2-D array into three 2-D arrays along rows     #####")
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
print(np.array_split(arr,3,axis=1))

# An alternate solution is using hsplit() opposite of hstack()

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
print('#####     Using the hsplit() method to split the 2-D array into three 2-D arrays along rows.     #####')
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
print(np.hsplit(arr,3))

# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().