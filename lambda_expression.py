# n = int(input())
# x = int(input())
# y = int(input())
# z = int(input())

# print([[a, b, c] for a in range(0,x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n])


# f = []
# for i in range (0,x+1):
#     for j in range (0,y+1):
#         for k in range (0,z+1):
#             if((i+j+k) is not n):
#                 f.append([i,j,k])
#
#
# print (f)


# if __name__ == '__main__':
#     N = int(input())
#     empty = []
#     conv = []
#
#     for i in range(N):
#
#         x = input().split()
#         empty.append(x)
#
#     for i in range(len(empty)):
#         if empty[i][0] == 'insert':
#             x = int(empty[i][1])
#             y = int(empty[i][2])
#             conv.insert(x, y)
#         elif empty[i][0] == 'print':
#             print(conv)
#         elif empty[i][0] == 'remove':
#             conv.remove(int(empty[i][1]))
#         elif empty[i][0] == 'append':
#             conv.append(int(empty[i][1]))
#         elif empty[i][0] == 'sort':
#             conv.sort()
#         elif empty[i][0] == 'pop':
#             conv.pop()
#         elif empty[i][0] == 'reverse':
#             conv.reverse()

