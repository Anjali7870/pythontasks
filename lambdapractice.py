# #lambda function
# y= lambda a: a+45
# print(y(56))
# print(type(y))
# def lam(num):
#     num = num + 67
#     return num
# print(lam(6))
# def sub(n):
# return lambda x, y : n(x + y)
# c=sub(10)
# print(c(5 , 56))
def sub(n):
    return lambda x, y: n - x * y  # Pass both x and y as arguments to n


c = sub(10)  # Define a subtraction function and pass it to sub
print(c(5, 56))  # This will print -51 (5 - 56)
#Using lambda() Function with filter()
T#he filter() function in Python takes in a function and
#a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
