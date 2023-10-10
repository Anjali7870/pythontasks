#def modify(print_patterns):

def print_patterns():
    n = int(input("Enter the number of patterns to print: "))
    prod = round(n / 3)
    for _ in range(prod):
        print("First pattern:")
        for i in range(1, 7):
            for k in range(1, 7):
                if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        print("Second pattern:")
        for i in range(5):
            for j in range(i, 5):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            for j in range(i):
                print("*", end=" ")
            print()

        for i in range(11):
            for j in range(11):
                if (
                        j == 0 or j == 10 or i == 1 and j == 2 or i == 1 and j == 4 or i == 1 and j == 6 or i == 1 and j == 8 or i == 8 and j == 2 or i == 8 and j == 4 or i == 8 and j == 6 or i == 8 and j == 8 or i == 10):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        print("Third pattern:")
        for i in range(3):
            for j in range(10):
                if (j == 0 or j == 9) and i in range(2, 8) or (i == 0 or i == 2) and j in range(2, 8) or i == 1 and (
                        j == 1 or j == 9) or i == 8 and (j == 1 or j == 8):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        for i in range(1, 10):
            for j in range(1, 10):
                if i == 1 or j == 1 or i == 9 or j == 9 or i == 2 or i == 8 or i == 2 or i == 3:
                    print("*", end=" ")
                elif i == 9 and j == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


print_patterns()
# def hello_world_decorator(func):
#     def wrapper():
#         print("Hello, World!")
#         func()
#     return wrapper
#
# @hello_world_decorator
# def my_function():
#     print("My function is running.")
#
# my_function()
