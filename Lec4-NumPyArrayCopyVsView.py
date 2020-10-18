# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.




######################  Copy  #################################

# Make a copy, change the original array, and display both arrays 
import numpy as np
print("####     Making a Copy, changing the original array, and displaying both the arrays    ####")
arr = np.array([1,2,3,4,5])
newArr = arr.copy()
arr[0] = 5
print("Original array",arr)
print("Copy array",newArr)


######################  View  #################################

# Make a View, change the original array, and display both arrays 
print("####     Making a View, changing the original array, and displaying both the arrays    ####")
arr = np.array([1,2,3,4,5])
newArr = arr.view()
arr[0] = 45
print("Original array",arr)
print("View",newArr)


######################  Make Changes in the VIEW  #################################

# Make a view, change the view, and display both arrays
print("####     Making a view, changing the view, and displaying both the arrays    ####")
arr = np.array([1,2,3,4,5])
newArr = arr.view()
newArr[0] = 23
print("original array",arr)
print("view",newArr)
# The original array SHOULD be affected by the changes made to the view.

#################################################################################################################################

######################  Check if Array Owns it's Data  #################################

# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.


# Print the value of the base attribute to check if an array owns it's data or not
print("####     Print the value of the base attribute to check if an array owns it's data or not    ####")
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
# The copy returns None.
# The view returns the original array.






