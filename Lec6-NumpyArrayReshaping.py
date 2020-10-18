######################  Reshaping Arrays  #################################

# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.


######################  Reshape From 1-D to 2-D  #################################

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements
import numpy as np
print("####     Convert the following 1-D array with 12 elements into a 2-D array    ####")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(4,3)
print('1-D Array :\n',arr)
print('2-D Array after reshaping :\n',newArr)


######################  Reshape From 1-D to 3-D  #################################

# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements
print("####     Convert the following 1-D array with 12 elements into a 3-D array    ####")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2) #shows error but no prblm
print(newarr)


# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements
# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

######################  throws error as mentioned above  #################################

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)

#################################################################################################################################

# Reshaped array always returns a view, let's check that
print("####     Reshaped array always returns a view    ####")
arr = np.array([1,2,3,4,5,6,7,8])
print("View returns the actual value")
print(arr.reshape(2,4).base)
# The example above returns the original array, so it is a view.


#################################################################################################################################


######################  Unknown Dimension  #################################

# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

# Convert 1D array with 8 elements to 3D array with 2x2 elements
print("####     Convert 1D array with 8 elements to 3D array with 2x2 elements    ####")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2,2,-1))
#We can not pass -1 to more than one dimension


#################################################################################################################################


######################  Flattening the arrays  #################################


# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

# Convert the array in to a 1D array 
print("#####     Converting the array in to a 1D array     #####")
arr = np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print("Before Reshaping\n",arr)
print("After Reshaping into 1D array\n",arr.reshape(-1))

