from functools import reduce

def sum(a,b):
    return (a+b)

l1 = [12,36,56,89]
val = reduce(sum,l1)
print(val)