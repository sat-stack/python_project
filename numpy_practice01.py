import numpy as np

# 1-D array
a = np.array([1,2,3], ndmin = 3)            # ndmin helps with defining the number of dimensions
print(a)                                    # this will print the values with dimension 3 ie [[[value]]]
print('number of dimensions :', a.ndim)     # this will print the number of dimensions for our verification that dimension is 3

# 2-D array
b = np.array([[1, 2], [3, 4]])
print(b)

# 3-D array (a 3-D array with two 2-D arrays)
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(c)

d = np.array([1,4,7], dtype = complex)
print(d)

# to check the dimension of the array we will use ndim :
e = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # 3 dimension
g = np.array([[1, 2, 3], [4, 5, 6]])  # 2 dimension
print(e.ndim)
print(g.ndim)

# 1.DATA TYPES :

# using array-scalar type
dt = np.dtype(np.int32)
print(dt)

# or #int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4',

dt = np.dtype('i4')
print(dt)

# using endian notation
dt = np.dtype('>i4')
print(dt)

# structure data type
dt = np.dtype([('age',np.int8)])
print(dt)

# applying it to ndarray object
dt = np.dtype([('age',np.int8)])
f = np.array([(10,),(20,),(30,)], dtype = dt)
print(f)
print(f['age'])

# a structured data type called student with a string field 'name', an integer field 'age' and a float field 'marks
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
j = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(student)
print(j)


# 2.ARRAY ATTRIBUTES :

# array indexing, first element has index 0, 2nd element has index 1 and so on..
s = np.array([1, 2, 3, 4])
print(s[1])  # it will give 2 is an output
print(s[2] + s[3])  # to access the 3rd and the 4th element and add them
print(s[2] , s[3])   # to access the 3rd and the 4th element

# accessing 2 D arrays
t = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', t[0, 1])
print('5th element on 2nd dim: ', t[1, 4])

# accessing 3 D arrays
p = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(p[0, 1, 2])   # tricky one but got it

# negative indexing : from the end
q = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', q[1, -1])


# array slicing
r = np.array([1, 2, 3, 4, 5, 6, 7])
print(r[1:5])  # Slice elements from index 1 to index 5
print(r[4:])   # Slice elements from index 4 to the end of the array
print(r[:4])   # Slice elements from the beginning to index 4 (not included)
print(r[-3:-1])  # negative slicing :Slice from the index 3 from the end to index 1 from the end
print(r[1:5:2])  # step :Return every other element from index 1 to index 5, 1 is index , 5 is upto, 2 is difference

z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])  # step example
print(z[1:20:2])   # 1 is index , 20 is upto, 2 is difference
print(z[: : -1])
print(z[: : -2])
print(z[1:20: -2])
print(z[::2])   # Return every other element from the entire array

# 2 D slicing
y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(y[1, 1:4])   # From the second element, slice elements from index 1 to index 4 (not included), remember that second element has index 1
print(y[0:2, 2])   # From both elements, return index 2
print(y[0:2, 1:4])  # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array