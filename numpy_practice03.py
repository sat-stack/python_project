import numpy as np

# shape of numpy array

a = np.array([[1, 3, 5, 7], [9, 11, 13, 15]])          # the shape of a 2-D array
print(a.shape)                  # output is (2, 4) : the array has 2 dimensions, and each dimension has 4 elements

b = np.array([1, 2, 3, 4], ndmin=5)   # 5 dimensions using ndmin
print(b)
print('shape of array :', b.shape)    # verify that last dimension has value 4

# reshaping array

# reshaping from 1D to 2D
c = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])  # 1-D array with 12 elements into a 2-D array
newc = c.reshape(4, 3)  # outermost dimension will have 4 arrays, each with 3 elements
print(newc)

# reshaping 1D to 3D
d = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])  # 1-D array with 12 elements into a 3-D array
newd = d.reshape(3, 2, 2)   # 3 arrays that contains 2 arrays, each with 2 elements
print(newd)

# Check if the returned array is a copy or a view
e = np.array([2, 3, 5, 7, 11, 13, 17, 19])
print(e.reshape(2, 4).base)   # output returns the original array, so it is a view

# unknown dimension
f = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # Converting 1D array with 8 elements to 3D array with 2x2 elements
newf = f.reshape(2, 2, -1)  # We can not pass -1 to more than one dimension
print(newf)

# flattening arrays (converting a multidimensional array into a 1D array)
g = np.array([[3, 7, 11], [13, 17, 19]])   # converting an array into a 1D array
newg = g.reshape(-1)
print(newg)





