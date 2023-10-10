def kattle():
    n = 9
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

        # (triangular shape)
        for i in range(n):
            for j in range(i, n):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            for j in range(i):
                print("*", end=" ")
            print()
        #  cylinder with a circle
        for i in range(11):
            for j in range(11):
                if (
                        j == 0 or j == 10 or i == 1 and j == 2 or i == 1 and j == 4 or i == 1 and j == 6 or i == 1 and j == 8 or i == 8 and j == 2 or i == 8 and j == 4 or i == 8 and j == 6 or i == 8 and j == 8 or i == 10):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
print(kattle())
