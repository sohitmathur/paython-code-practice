# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
#

# *********map************
# def cube(n):
#     return n*n*n

# l = [1,2,3,4,5]

# nioam= list(map(lambda x: x*x*x ,l))
# print (nioam)


# ************filter************
# def filterfunc(n):
#     return n>2
#
# nioam1 = list(filter(filterfunc,l))
# print(nioam1)

# ***********reduce************
from functools import reduce
numbers = [1,2,3,4,5]
def mysum(x,y):
    return x+y

sum =reduce(mysum,numbers)
print(sum)