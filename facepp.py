# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==5 and j==5 or i==5 and j==7):
#             print("o",end=" ")
#         elif( i==7 and j==6):
#             print("^",end=" ")
#         elif(i==4 and j==6 or i==4 and j==5 or i==4 and j==4  or i==4 and j==7 or i==4 and j==8 or i==3 and j==8 or i==3 and j==7 or i==3 and j==6 or i==3 and j==5 or i==3 and j==4 or i==5 and j==4 or i==5 and j==8 or i==6 and j==4 or i==6 and j==8):
#             print("*",end=" ")
#         elif(i==9 and j==5):
#             print("\\|0|/",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
n = 10

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 5 and (j == 5 or j == 7):
            print("O", end=" ")
        elif i == 7 and j == 6:
            print("V", end=" ")
        elif i == 9 and j == 5:
            print("......", end=" ")
        elif i == 1 and j == 2:
            print("_", end=" ")
        elif i == 1 and j == 9:
            print("_", end=" ")
        elif i == 3 and (j == 2 or j == 9):
            print("|", end=" ")
        elif i == 4 and (j == 2 or j == 9):
            print("*", end=" ")
        elif i == 8 and (j == 2 or j == 9):
            print("*", end=" ")
        elif i == 9 and (j == 2 or j == 9):
            print("*", end=" ")
        elif (i == 4 or i == 8) and (j == 1 or j == 10):
            print("__", end=" ")
        elif i in [2, 6]:
            if j == 1:
                print("//", end=" ")
            elif j == 10:
                print("\\", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
# n = 12
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 2 and 4 <= j <= 7:
#             print("*", end=" ")
#         elif i == 3 and j in [3, 4, 7, 8]:
#             print("*", end=" ")
#         elif i == 4 and j in [2, 9]:
#             print("*", end=" ")
#         elif i == 5 and j in [2, 5, 6, 9]:
#
#             print("*", end=" ")
#         elif i == 6 and j in [2, 9]:
#             print("*", end=" ")
#         elif i == 7 and j == 5:
#             print("__", end=" ")
#         elif i == 9 and j in [4, 6]:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


