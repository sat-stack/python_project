'''a = 3
b = 5
print(a//b)
print(a/b)'''

'''n = 3
for n > 3:
   print(i * i)

   i += 1'''
'''n = 3
for i in range(0, n):
    print(i * i)'''

'''i = 0
n = 2
while i < n:
    print(i * i)
    i += 1'''


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("1" )
#     print("")

# n=5
# for i in range(1,n+1):
#     print("*"*i)


# output should be 1 2 3 4 8 9 10 11 12

'''count = 1

while (count < 15):
    if count < 6 or count > 10:
       print('The count is:', count)
    count = (count + 1)


print ("Good bye!")'''

# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


# # Measure some strings:

'''words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))'''


# # Range function:

# for i in range(5):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(-10, -20, -100 ):
#     print(i)

# x = sum(range(4))   # 0 + 1 + 2 + 3 = 6 , so the output is 60
# print(x)


# y = list(range(4))  # [0, 1, 2, 3]
# print(y)


'''for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')'''


'''for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)'''


'''def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()   # Now call the function we just defined: fib(2000) , output = 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597'''

# import datetime
#
#
#
#
# date = "05-01-11"
# date_in = datetime.datetime.strptime(date, '%m-%d-%y')
# date_formatted = date_in.strftime("%Y-%m-%d")
# print(date)
# print(date_in)
# print(date_formatted)

q = '''
    SELECT COUNT(rain)
    FROM weather_underground
    WHERE rain = 1;'''

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1) # k= 6 , i am last in line , result = 6 + 15 = 21
    print(result)
  else:
    result = 0
  return result


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  # k= 5, i am 2nd last in line , result = 5 + 10 = 15
    print(result)
  else:
    result = 0
  return result


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  # k=4, i am 3rd last in line, result = 4 + 6 = 10
    print(result)
  else:
    result = 0
  return result


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1) # k=3, result = 3+ 3 = 6
    print(result)
  else:
    result = 0
  return result



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)   #k=2 , result = 3
    print(result)
  else:
    result = 0
  return result




def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)    # K=1 , result = 1
    print(result)
  else:
    result = 0
  return result



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  #k =0
    print(result)
  else:
    result = 0
  return result


print("\n\nRecursion Example Results")
tri_recursion(6)
