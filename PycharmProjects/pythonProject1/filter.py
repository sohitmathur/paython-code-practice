def greater_than_5(num):
    if num >= 5:
        return True
    else:
        return False
g10 =lambda num:num>10
l=[5,3,9,36,23,96,36,0,96,36]
print(list(filter(greater_than_5,l)))
print(list(filter(g10,l)))
