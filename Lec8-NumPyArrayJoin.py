######################  Joining NumPy Arrays  #################################

# Joining means putting contents of two or more arrays in a single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# Join Two arrays 
import numpy as np
print("#####     Joining two arrays with axis(rows) 0     #####")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.concatenate((arr1,arr2)))

# Join two 2-D arrays along rows(axis = 1)
print("#####     Joining two 2-D arrays with axis(rows) 1     #####")
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
print(np.concatenate((arr1,arr2),axis=1))


######################  Joining Arrays Using Stack Functions  #################################

# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the concatenate() method along with the axis. If axis is not explicitly passed it is taken as 0.

print("#####     Using Stack     #####")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])
print(np.stack((arr1,arr2,arr3),axis=1))



######################  Stacking Along Rows  #################################

# NumPy provides a helper function: hstack() to stack along rows.
print("#####     Stacking along Rows     ######")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.hstack((arr1,arr2)))

######################  Stacking Along Rows  #################################

# NumPy provides a helper function: vstack() to stack along columns.
print("#####     Stacking along columns     #####")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1,arr2)))

######################  Stacking Along Height(depth)  #################################

# NumPy provides a helper function: dstack() to stack along height,which is the same as depth.
print('#####     Stacking along Height(depth)     #####')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.dstack((arr1,arr2)))