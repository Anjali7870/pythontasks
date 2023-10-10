n = 6
for i in range(1, n + 1):
    for k in range(1, n + 1):
        if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# # #create a pattren
# n=7
# for i in range(1,n):
#     for j in range(1,n):
#         if i==6 or j==1 or j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=8
# for i in range(1,n):
#     for j in range(0,n):
#         if (i==7 or i==j or j==n-1-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

import random
#
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
count = 0
while count < 50:
    n = random.randint(1, 1000)
    if prime(n):
        print(n)
        count += 1