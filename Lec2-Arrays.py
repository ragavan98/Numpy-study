import numpy as np

# Creating a 0-Dimensional array
print("####   Creating a 0-Dimensional array   ####")
arr0Dimensional = np.array(42)
print(arr0Dimensional)
# print(type(arr0Dimensional))  it is object type

#################################################################################################################################

# Creating a 1-Dimensional array
print("####   Creating a 1-Dimensional array   ####")
arr1Dimensional = np.array([1,2,3,4,5])
print(arr1Dimensional)
#print(type(arr1Dimensional))  it is object type

#################################################################################################################################

# Creating a 2-Dimentional array
print("####   Creating a 2-Dimensional array   ####")
arr2Dimensional = np.array([[1,2,3],[4,5,6]])
print(arr2Dimensional)
#print(type(arr2Dimensional))     it is object type

#################################################################################################################################

# Creating a 3-Dimentional array
print("####   Creating a 3-Dimensional array   ####")
arr3Dimensional = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3Dimensional)
#print(type(arr3Dimensional))       it is object type

#################################################################################################################################

# Checking Number of dimensions
print("####   Checking Number of dimensions   ####")
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#################################################################################################################################

# Higher Dimensional Arrays
# An Array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the "ndmin" argument.

#Creating an array with 5 dimensions and verify that it has 5 dimensions:
print("####   Creating an array with 5 dimensions and verify that it has 5 dimensions   ####")
dimCheckArr = np.array([1,2,3,4,5],ndmin=5)
print(dimCheckArr)
print('Number of dimensions :',dimCheckArr.ndim)

#################################################################################################################################
 
            ######################  Numpy Array Indexing  #################################

# Access Array Elements
# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in Numpy arraysstarts with o, meaning that the first element has index 0, and the second has index 1 etc.

# Get the first element form the following array
print("####   Get the first element form the following array   ####")
indArray = np.array([1,2,3,4,5])
print(indArray[0])

# Get the third and fourth elements from the following  array and add them.
print("####   Get the third and fourth elements from the following array    ####")
addArray = np.array([1,2,3,4,5])
print(addArray[2]+addArray[3])

            #####################   Access 2-D Arrays   ##################

# Access the 2nd element on 1st dimensional
print("####   Accessing the 2nd element on 1st dimensional    ####")
print('2nd element of the first dimension is',arr2Dimensional[0,1])

            #####################   Access 3-D Arrays   ##################

# Access the third element of the second array of the first array:            
print("####   Access the third element of the second array of the first array    ####")
print('3rd element of the second array of the first array is',arr3Dimensional[0,1,2])

# Example Explained
# arr[0, 1, 2] prints the value 6.

# And this is why:

# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6

#################################################################################################################################
 
            ######################  Negative Indexing  #################################

# Negative inexing is used to access an array from the end
# Print the last element form the 2nd dimension:
print("####   Printing the last element form the 2nd dimension    ####")
arr2Dimensional = np.array([[1,2,3],[4,5,6]])
print('using Positive indexing ',arr2Dimensional[1,2])
print('using Negative indexing ',arr2Dimensional[1,-1])

#################################################################################################################################
 
            ######################  NumPy Array Slicing  #################################

# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

# Slice elements from index 1 to index 5 from the following array:
print("####   Slicing elements from index 1 to index 5 from the following array    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[1:5])  # Note: The result includes the start index, but excludes the end index.

# Slice elements from index 4 to the end of the array
print("####   Slicing elements from index 4 to the end of the array    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[4:])

# Slice elements from the beginning to index 4 (not included)
print("####   Slicing elements from the beginning to index 4 (not included)    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[:4])
 
            ######################  Negative Slicing  #################################

# Slice from the index 3 from the end to index 1 from the end
print("####   Slicing from the index 3 from the end to index 1 from the end    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[-3:-1])
 
            ######################  Step  #################################

# Use the step value to determine the step of the slicing:            
# Return every other element from index 1 to index 5:
print("####     Returning every other element from index 1 to index 5    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[1:5:2])

# Return every other element from the entire array
print("####     Returning every other element from the entire array    ####")
arr1Dimensional = np.array([1,2,3,4,5,6,7])
print(arr1Dimensional[::2])

            ######################  Slicing 2-D Array  #################################

# From the second element, slice elements from index 1 to index 4 (not included)
print("####     From the second element, slicing elements from index 1 to index 4 (not included)    ####")
arr2Dimensional = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2Dimensional[1,1:4])

# From both elements, return index 2
print("####     From both elements, returning index 2    ####")
arr2Dimensional = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2Dimensional[0:2,2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print("####     From both elements, slicing index 1 to index 4 (not included), this will return a 2-D array    ####")
arr2Dimensional = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2Dimensional[0:2,1:4])