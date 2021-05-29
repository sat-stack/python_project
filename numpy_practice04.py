import numpy as np

# NumPy Array Iterating

# Iterating 1-D Arrays:
a = np.array([1, 2, 3])
for x in a:
    print(x)

# Iterating 2-D Arrays:
b = np.array([[1, 2, 3], [4, 5, 6]])
for x in b:
    print(x)

    # To return the actual values, the scalars, we have to iterate the arrays in each dimension:
c = np.array([[1, 2, 3], [4, 5, 6]])   # iterate on each scalar element of the 2-D array
for x in c:
  for y in x:
    print(y)

# Iterating 3-D Arrays:
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in d:
  print(x)

#  Iterate down to the scalars:
e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in e:
  for y in x:
    for z in y:
      print(z)

# Iterating Arrays Using nditer() :
f = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(f):
  print(x)

# Iterating Array With Different Data Types:
g = np.array([1, 2, 3])
for x in np.nditer(g, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterating With Different Step Size:
h = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(h[:, ::2]):
  print(x)

# Enumerated Iteration Using ndenumerate():
i = np.array([1, 2, 3])                          # Enumerate on 1D array
for idx, x in np.ndenumerate(i):
  print(idx, x)

j = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])     # Enumerate on 2D array
for idx, x in np.ndenumerate(j):
  print(idx, x)

# ------------------------------------------------------------------------------
# NumPy Joining Array

# Joining two arrays

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
k = np.concatenate((a1, a2))
print(k)

# joining two 2-D arrays along rows (axis=1)
b1 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
l = np.concatenate((b1, b2), axis=1)
print(l)

# Joining Arrays Using Stack Functions
c1 = np.array([1, 2, 3])
c2 = np.array([4, 5, 6])
m = np.stack((c1, c2), axis=1)
print(m)

# Stacking Along Rows:
d1 = np.array([1, 2, 3])
d2 = np.array([4, 5, 6])
n = np.hstack((d1, d2))
print(n)

# Stacking Along Columns:
e1 = np.array([1, 2, 3])
e2 = np.array([4, 5, 6])
o = np.vstack((e1, e2))
print(o)

# Stacking Along Height (depth):
f1 = np.array([1, 2, 3])
f2 = np.array([4, 5, 6])
p = np.dstack((f1, f2))
print(p)

# -------------------------------------------------------------
# NumPy Splitting Array

# Split the array in 3 parts
q = np.array([1, 2, 3, 4, 5, 6])
newq= np.array_split(q, 3)   # The return value is an array containing three arrays
print(newq)

# Split the array in 4 parts
r = np.array([1, 2, 3, 4, 5, 6])
newr = np.array_split(r, 4)   # If the array has less elements than required, it will adjust from the end accordingly
print(newr)

# Access the splitted arrays:
s = np.array([1, 2, 3, 4, 5, 6])
news = np.array_split(s, 3)
print(news[0])
print(news[1])
print(news[2])

# Split the 2-D array into three 2-D arrays:
t = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newt = np.array_split(t, 3)
print(newt)

# Split the 2-D array(3 element)  into three 2-D arrays
u = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newu = np.array_split(u, 3)
print(newu)

# Split the 2-D array into three 2-D arrays along rows:
v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newv = np.array_split(v, 3, axis=1)
print(newv)

# Using the hsplit() method to split the 2-D array into three 2-D arrays along rows:
w = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
neww = np.hsplit(w, 3)
print(neww)
