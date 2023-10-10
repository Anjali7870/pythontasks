# # # import random
# # # def kattle():
# # #     a = input("Enter a pattern type (1, 2, or 3): ")
# # #     if a == "1":
# # #         print("First type of pattern")
# # #         n = 6
# # #         for i in range(1, n + 1):
# # #             for k in range(1, n + 1):
# # #                 if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
# # #                     print("*", end=" ")
# # #                 else:
# # #                     print(" ", end=" ")
# # #             print()
# # #     elif a == '2':
# # #         print("Second pattern")
# # #         n = 6
# # #         # (triangular shape)
# # #         for i in range(n):
# # #             for j in range(i, n):
# # #                 print(" ", end=" ")
# # #             for j in range(i):
# # #                 print("*", end=" ")
# # #             for j in range(i):
# # #                 print("*", end=" ")
# # #             print()
# # #         # cylinder with a circle
# # #         for i in range(11):
# # #             for j in range(11):
# # #                 if (
# # #                         j == 0 or j == 10 or i == 1 and j == 2 or i == 1 and j == 4 or i == 1 and j == 6 or i == 1 and j == 8 or i == 8 and j == 2 or i == 8 and j == 4 or i == 8 and j == 6 or i == 8 and j == 8 or i == 10):
# # #                     print("*", end=" ")
# # #                 else:
# # #                     print(" ", end=" ")
# # #             print()
# # #     elif a == '3':
# # #         print("Third pattern")
# # #         for i in range(3):
# # #             for j in range(10):
# # #                 if (j == 0 or j == 9) and i in range(2, 8) or (i == 0 or i == 2) and j in range(2, 8) or i == 1 and (
# # #                         j == 1 or j == 9) or i == 8 and (j == 1 or j == 8):
# # #                     print("*", end=" ")
# # #                 else:
# # #                     print(" ", end=" ")
# # #             print()
# # #             for i in range(1, 10):
# # #                 for j in range(1, 10):
# # #                     if i == 1 or j == 1 or i == 9 or j == 9 or i == 2 or i == 8 or i == 2 or i == 3:
# # #                         print("*", end=" ")
# # #                     elif i == 9 and j == 2:
# # #                         print("*", end=" ")
# # #                     else:
# # #                         print(" ", end=" ")
# # #     else:
# # #         print("Enter a valid number")
# # #
# # # # for _ in range(3):
# # #     kattle()
# # def kattle(n):
# #     print("First pattern")
# #     for i in range(1, n + 1):
# #         for k in range(1, n + 1):
# #             if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
# #                 print("*", end=" ")
# #             else:
# #                 print(" ", end=" ")
# #         print()
# #
# #     # (triangular shape)
# #     print("\nSecond pattern")
# #     for i in range(n):
# #         for j in range(i, n):
# #             print(" ", end=" ")
# #         for j in range(i):
# #             print("*", end=" ")
# #         for j in range(i):
# #             print("*", end=" ")
# #         print()
# #
# #     # cylinder with a circle
# #     print("\nThird pattern")
# #     for i in range(11):
# #         for j in range(11):
# #             if (
# #                     j == 0 or j == 10 or i == 1 and j == 2 or i == 1 and j == 4 or i == 1 and j == 6 or i == 1 and j == 8 or i == 8 and j == 2 or i == 8 and j == 4 or i == 8 and j == 6 or i == 8 and j == 8 or i == 10):
# #                 print("*", end=" ")
# #             else:
# #                 print(" ", end=" ")
# #         print()
# #
# # # Function to display patterns based on user input
# # def display_patterns(num_patterns):
# #     for _ in range(num_patterns):
# #         n = int(input("Enter a number for pattern size: "))
# #         kattle(n)
# #         print()
# #
# # # Get user input for the number of patterns to display
# # num_patterns = int(input("Enter the number of patterns to display: "))
# # display_patterns(num_patterns)
# #
# def display_patterns(num_patterns):
#     for pattern_num in range(1, num_patterns + 1):
#         print(f"Pattern {pattern_num}:")
#
#         if pattern_num == 1:
#             # Pattern 1
#             n = 5  # Adjust the size of the pattern as needed
#             for i in range(1, n + 1):
#                 for k in range(1, n + 1):
#                     if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
#                         print("*", end=" ")
#                     else:
#                         print(" ", end=" ")
#                 print()
#
#         elif pattern_num == 2:
#             # Pattern 2
#             n = 5  # Adjust the size of the pattern as needed
#             for i in range(n):
#                 for j in range(i, n):
#                     print(" ", end=" ")
#                 for j in range(i):
#                     print("*", end=" ")
#                 for j in range(i):
#                     print("*", end=" ")
#                 print()
#
#         elif pattern_num == 3:
#             # Pattern 3
#             n = 5  # Adjust the size of the pattern as needed
#             for i in range(3):
#                 for j in range(n):
#                     if (j == 0 or j == n - 1) and i in range(2, n - 2) or (i == 0 or i == 2) and j in range(2, n - 2) or i == 1 and (j == 1 or j == n - 1) or i == n - 2 and (j == 1 or j == n - 2):
#                         print("*", end=" ")
#                     else:
#                         print(" ", end=" ")
#                 print()
#
#                 for i in range(n):
#                     for j in range(n):
#                         if i == 0 or j == 0 or i == n - 1 or j == n - 1 or i == 1 or i == n - 2:
#                             print("*", end=" ")
#                         elif i == n - 1 and j == 1:
#                             print("*", end=" ")
#                         else:
#                             print(" ", end=" ")
#                     print()
#
#
#
# # Get user input for the number of patterns to display
# num_patterns = int(input("Enter the number of patterns to display: "))
#
# # Display patterns one by one based on user input
# display_patterns(num_patterns)
# def display_pattern_1(n):
#     for i in range(1, n + 1):
#         for k in range(1, n + 1):
#             if i == 2 or i == 3 or k == 2 or k == 3 or k == 4 or k == 5:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
#
#
# def display_pattern_2(n):
#     for i in range(n):
#         for j in range(i, n):
#             print(" ", end=" ")
#         for j in range(i):
#             print("*", end=" ")
#         for j in range(i):
#             print("*", end=" ")
#         print()
#
#
# def display_pattern_3(n):
#     for i in range(3):
#         for j in range(n):
#             if (j == 0 or j == n - 1) and i in range(2, n - 2) or (i == 0 or i == 2) and j in range(2,
#                                                                                                     n - 2) or i == 1 and (
#                     j == 1 or j == n - 1) or i == n - 2 and (j == 1 or j == n - 2):
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
#
#         for i in range(n):
#             for j in range(n):
#                 if i == 0 or j == 0 or i == n - 1 or j == n - 1 or i == 1 or i == n - 2:
#                     print("*", end=" ")
#                 elif i == n - 1 and j == 1:
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()
#
#
# def display_patterns(num_patterns):
#     for pattern_num in range(1, num_patterns + 1):
#         print(f"Pattern {pattern_num}:")
#
#         if pattern_num == 1:
#             display_pattern_1(5)  # Adjust the size of the pattern as needed
#         elif pattern_num == 2:
#             display_pattern_2(5)  # Adjust the size of the pattern as needed
#         elif pattern_num == 3:
#             display_pattern_3(5)  # Adjust the size of the pattern as needed
#
#         input("Press Enter to continue to the next pattern...")
#
#
# # Get user input for the number of patterns to display
# num_patterns = int(input("Enter the number of patterns to display: "))
#
# # Display patterns one by one based on user input
# display_patterns(num_patterns)
import random

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






