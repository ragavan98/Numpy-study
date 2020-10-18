######################  NumPy Filter Arrays  #################################

# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.

# A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

# Create an array from the elements on index 0 and 2 :
import numpy as np
print("##### Creating an array from the elements on index 0 and 2      #####")
arr = np.array([41,42,43,44,45])
filter_arr = np.array([True, False, True, False, False])
newArr = arr[filter_arr]
print(newArr)
# The example above will return [41, 43], why?
# Because the new filter contains only the values where the filter array had the value True, in this case, index 0 and 2.

######################  Creating the Filter Array  #################################

# In the example above we hard-coded he TRUE and FALSe values, but the common use is to create a filter array based on conditions.
# Create a filter array that will return only values higher than 42
print("#####     Creating a filter array that will return only values higher than 42     #####")
arr = np.array([41,42,43,44])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
         filter_arr.append(False)
newArr = arr[filter_arr]
print(newArr)            

# Create a filter array that will return only even elements from the original array
print("#####     Creating a filter array that will only return even elements from the original array     #####")
arr = np.array([41,42,43,44])
filter_arr = []
for element in arr:
    if element%2 == 0:
        filter_arr.append(True)
    else:
         filter_arr.append(False)
newArr = arr[filter_arr]
print(newArr)            


######################  Creating Filter Directly From Array  #################################

# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

# Create a filter array that will return only values higher than 42
print("#####     Creating a filter array that will return only values higher than 42     #####")
arr = np.array([41,42,43,44,45])
filter_arr = arr > 42
print("Filter array is\n",filter_arr)
print(arr[filter_arr])

# Create a filter array that will return only even elements from the original array:
print("#####     Creating a filter array that will only return even elements from the original array     #####")
arr = np.array([41,42,43,44,45,46])
filter_arr = arr%2 == 0
print("Filter array is\n",filter_arr)
print(arr[filter_arr])
