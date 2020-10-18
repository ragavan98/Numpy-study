import numpy as np
#The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.
#see below Example
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr)) 

######################################################################################################################################################

#To create an ndarray, we can pass a list,tuple or any array-list object into the array() method
#and it will be converted into an ndarray 
#See below Example

arr1 = np.array((1,2,3,4,5)) #passing a tuple
print(arr1)
print(type(arr1))
