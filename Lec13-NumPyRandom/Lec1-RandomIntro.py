######################  Random Numbers in NumPy  #################################

"""
 What is a Random Number ?
             Random number does NOT mean a different number every time. Random means 
        something that can not be predicted logically.
 
 Pseudo Random and True Random.             
               Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
        If there is a program to generate random number it can be predicted, thus it is not truly random.
        Random numbers generated through a generation algorithm are called pseudo random.
        Can we make truly random numbers?
        Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
        We do not need truly random numbers, unless its related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).
        In this tutorial we will be using pseudo random numbers.

 """

######################  GEnerate Random Number  #################################        

# NumPy offeres the random module to work with random numbers.

# Generate a random integer from 0 to 100
from numpy import random
print("#####      Generating a random integer from 0 to 100     #####")
x = random.randint(100)
print(x)


######################  GEnerate Random Float  #################################        

# THe random module's rand() method returns a random float between 0 and 1.

# Generate a random float from 0 to 1
print("#####     Generating a random float from 0 to 1     #####")
x = random .rand() 
print(x)


######################  GEnerate Random Array  #################################        

# In NumPy we work with arrays, and you can use the two methods from the above example to make random arrays.

"""   Integers   """

# The randint() method takes a size parameter where you can specify the shape of an array.

# Generate a 1-D array containing 5 random integers from 0 to 100
print("#####     Generating a 1-D array containing 5 random integers from 0 to 100     #####")
x = random.randint(100,size=(5))
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
print("##### Generating a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:     #####")
x = random.randint(100,size=(3,5))
print(x)


"""   Float   """

# The rand() method also allows you to specify the shape of the array.

# Generate a 1-D array containing 5 random floats:
print("#####     Generating a 1-D array containing 5 random floats:     #####")
x = random.rand(5)
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
print("#####     Generate a 2-D array with 3 rows, each row containing 5 random numbers:     #####")
x = random.rand(3,5)
print(x)


######################  GEnerate Random Number From Array  #################################        

"""
    The choice() method allows you to generate a random value based on an array of values.
    The choice() method takes an array as a parameter and randomly returns one of the values.

"""   
# Return one of the values in an array:
print("#####     Returning one of the values in an array:     #####") 
x = random.choice([10,12,11,13,14,15])
print(x)

"""
    The choice() method also allows you to return an array of values.
    Add a size parameter to specify the shape of the array.

"""

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
print("######     Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):     #####")
x = random.choice([3,5,7,9],size=(3,5))
print(x)
