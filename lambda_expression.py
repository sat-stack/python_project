# lambda expression

x = lambda a, b, c : a + b + c
print(x(9, 12, 56))


# triple

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(8)

print(mytripler(42))


# double and triple

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)
mytripler = myfunc(8)

print(mydoubler(14))
print(mytripler(14))