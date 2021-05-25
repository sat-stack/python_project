import numpy as np

# numpy datatypes

a = np.array([1, 2, 3, 4])    # data type of an array object
print(a)
print(a.dtype)

b = np.array(['litchi', 'peaches', 'cherry'])   # data type of an array containing strings
print(b)
print(b.dtype)

c = np.array([1, 2, 3, 4], dtype='S')        # array with data type string
print(c)
print(c.dtype)

d = np.array([1, 2, 3, 4], dtype='i4')   # array with data type 4 bytes integer
print(d)
print(d.dtype)


e = np.array([1.1, 2.1, 3.1])  # Converting Data Type on Existing Arrays by using astype()

ne = e.astype('i')    # data type from float(f) to integer by using 'i' as parameter value
print(ne)
print(ne.dtype)

nee = e.astype(int)   # data type from float to integer by using "int" as parameter value
print(nee)
print(nee.dtype)

neee = e.astype(bool)  # data type from float to boolean by using "bool" as parameter value
print(neee)
print(neee.dtype)


# numpy copy and view

f = np.array([1, 2, 3, 4, 5])    # copy - The copy SHOULD NOT be affected by the changes made to the original array
x = f.copy()
f[0] = 42
print(f)
print(x)

g = np.array([1, 2, 3, 4, 5])    # view - The view SHOULD be affected by the changes made to the original array
y = g.view()
g[2] = 32
print(g)
print(y)

h = np.array([1, 2, 3, 4, 5])  # Making changes in view: creating a view, changing the view, and displaying both arrays
z = h.view()                      # The original array SHOULD be affected by the changes made to the view
z[3] = 23
print(h)
print(z)


j = np.array([1, 3, 5, 7, 9, 11, 13, 15])    # checking if array owns its data
k = j.copy()      # copy owns data
l = j.view()      # view doesn't own data
print(k.base)     # owns data, so the copy returns None
print(l.base)     # doesn't own data, the view returns the original array



