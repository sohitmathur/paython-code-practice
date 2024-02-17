# list = [3,8,2,9,11]
#
# min=list[0]
# max=list[0]
#
# for i in range(len(list)):
#     if list[i]>max:
#         max=list[i]
#     elif list[i]<min:
#         min=list[i]
# print("max:",max)
# print("min",min)



# n=int(input("enter the the total number of element you want inside list:"))
# l=[]
# for i in range(n):
#     ele=int(input("enter the element:"))
#     l.append(ele)
# print("my list",l)
# sorted_list=l.sort()
# print('sorted_list',l)
# minimum_ele=l[0]
# print("the minimum element is",minimum_ele)
# maximum_ele=l[-1]
# print("the maximum element is",maximum_ele)
# secont_largest_ele=l[-2]
# print("the secont_largest element is",secont_largest_ele)



# n=int(input("enter the total number of element you want inside list:"))
# l=[]
# for i in range(n):
#     ele=int(input("enter the element:"))
#     l.append(ele)
# print("my list",l)
# sorted_list=l.sort()
# print('sorted list is',l)
# minimum_ele=l[0]
# print('the minimum element is:',minimum_ele)
# maximum_ele=l[-1]
# print('the maximum_ele is:',maximum_ele)
# maximum_second_ele=l[-2]
# print('the maximum_second_ele is:',maximum_second_ele)
#

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num % i ==0:
#         print("its not prime no")
#         break
# else:
#    print("its prime no")


# num=int(input("enter the the total number of element you want inside the list:"))
# l=[]
# for i in range(num):
#     ele=int(input('enter the element:'))
#     l.append(ele)
# print("my list",l)
# sorted_list=l.sort()
# print('sorted element',l)
# minimum_ele=l[0]
# print("the minimum element is:",minimum_ele)
# maximum_ele=l[-1]
# print("the maximum element is:",maximum_ele)
# second_max_ele=l[-2]
# print("the second_max_ele element is:",second_max_ele)


# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i ==0:
#         print(f"{num} its not a prime no:")
#         break
# else:
#     print(f"{num} it is prime no")


# n=int(input("enter the total number of element you want inside the list:"))
# l=[]
# for i in range(n):
#     ele=int(input("enter the number"))
#     l.append(ele)
# print('the list is',l)
# sorted_ele=l.sort()
# print('the sorted list is',l)
# minimum_ele=l[0]
# print("the minimium number is",minimum_ele)
# maximum_ele=l[-1]
# print("the maximium number is",maximum_ele)
# second_highest_ele=l[-2]
# print("the second highest element is",second_highest_ele)


# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print("its not a prime no")
#         break
# else:
#     print("its a prime no")
# import timeit
# print(timeit.timeit('x=[1,2,3,4]'))
# print(timeit.timeit('x=(1,2,3,4)'))


# zipcode=range(2000,20000)
# for i in zipcode:
#     print(i)

# sort list without using sort keyword
# list1= [2,8,1,3,9,4,5,6,565,1]
# n= len(list1)
# for i in range(n):
#     for j in range(i+1,n):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)

# write a code whether the string palindrom or not?

# s= "nitin"
# if s==s[::-1]:
#     print("yes its a palindrom")
# else:
#     print("its not")

# sort dictionery using dict comprehenstion



# list=[i for i in range(100) if i%2==0 ]
# print(list)


# find the pairs with given sum
# list=[12,63,8,9,36,21]
# n= len(list)
# k=10
# for i in range(n):
#     for j in range(i+1,n):
#         if (list[j]+list[j]) == k:
#             print(list[i],list[j])

# s= "the sky is blue"
# l= s.split()
# l=l[::-1]
# l=" ".join(l)
# print(l)
#




# find the maximum repeated charecter in string without having 2 complexcity?

# s= "ibqboicqninwioneu"
# char={}
# for i in s:
#     if i in char:
#         char[i]=+1
#     else:
#         char[i]=1
# max_char=max(char,key= char.get)
# print(max_char)

# write a code raise exception

# l=[2,3,4]
# sum=0
# for i in l:
#     if i == 1:
#         raise Exception("exception: is found")
#     else:
#         sum=+1
# print(l)



# l=[23,56,1,5,78]
# p=(23,45)
# l.extend(p)
# # l.append(p)
# print(l)



# x= lambda a:a+5
# print(x(5))

# l=[1,2,3,4,5]
# cube=list(map(lambda a:a **3,l))
# print(cube)

# decorator

# def divi(a,b):
#     print(a/b)
# def new_divi(func):
#
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#
#     return inner
#
# divi1=new_divi(divi)
# divi1(2,5)

# list=[i for i in range(100) if i %2==0 ]
# print(list)

# dict comprehention

# d1= {n:n*n for n in range(1,10)}
# print(d1)

#
# age= 35
# disscount= 5 if age<25 else 10
# print(disscount)



# for i in range(10):
#     if i==7:
#         pass
#     print(i,end=",")




# list1=[2,1,6,3,8,4,6,232,19,9,5]
# n=len(list1)
# for i in range(n):
#     for j in range(i+1,n):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)



# name= 'sohit'
# age= 25
# print("the name of the employee is {} and employee age is".format('sohit',25))
import copy

dic={"ram":25,"ganesh":30,"mangesh":29}
# dic_keys=list(dic.keys())
# print (list(dic))
# print(* dic)


# x=list(map(int,(input("enter the number:").split(","))))
# print(x)

# def divi(a,b):
#    print(a/b)
# def new_divi(func):
#
#     def inner_divi(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#     return inner_divi
# new1=new_divi(divi)
# new1(5,10)

# list=[i for i in range(10)if i%2]
# print(list)
#
# d1={n:n*n for n in range(10)if n%2 }
# print(d1)

# genrators
# def squre(n):
#     for i in range(1,n+1):
#         yield i*i
# a= squre(3)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# inheritance

# class A:
#     def display(self):
#         print("a display")
# class B(A):
#     def show(self):
#         print ("show display")
# d=B()
# d.show()
# d.display()

# class Employee():
#     company="Google"
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def employee_info(self):
#         print(f"the name of the employee is {self.name} & age of employee is {self.age} and salary is {self.salary} company name is {self.company}")
# e=Employee('sohit',25,100000)
# e.employee_info()
#

# s="helloworld"
# print(s[0:5])

# d1={'A':1,'B':2,'C':3}
# d2=d1.copy()
# d2.pop('A')
# print(d2)

# square= (lambda x:x*x)(5)
# print(square)

# recursion
# def reverse_list(lst):
#     if not lst:
#         return[]
#     return [lst[-1]]+reverse_list(lst[:-1])
# print(reverse_list([1,2,3,4]))






# def divi(a,b):
#     print(a/b)
# def new_divi(func):
#
#     def inner_divi(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#     return inner_divi
# new=new_divi(divi)
# new(5,20)
#

# ls=[i for i in range(10) if i%2==0]
# print(ls)

# d={n:n*n for n in range(10)}
# print(d)

# def sqr(n):
#     for i in range(1,n+1):
#         yield i*i
# a=sqr(3)
# print(next(a))
# print(next(a))
# print(next(a))
# data = [
#     {
#         "name": "Finance",
#         "employees": [
#             {
#                 "name": "Karan",
#                 "salary": 100,
#             },
#             {
#                 "name": "Monica",
#                 "salary": 1000,
#             },
#         ],
#     },
#     {
#         "name": "Account",
#         "employees": [
#             {
#                 "name": "Sanket",
#                 "salary": 200,
#             },
#             {
#                 "name": "Prathamesh",
#                 "salary": 900,
#             },
#         ],
#     },
# ]
# d=data
# print(data[0]['employees'][1]['salary'])
# print(data[1]['employees'][1]['name'])
# print(data[0]['employees'][1]['name'])

# nested dictionery

# course={
#     'java':{'course_duration':'2 months','fees':10000},
#     'python':{'course_duration':'2 months','fees':20000},
#     'php':{'course_duration':'2 months','fees':30000},
# }
#
# # print(course['java']['fees'])
#
# for i,j in course.items():
#     print(i,j['fees'])


# def divi(a,b):
#     print(a/b)
# def inner_divi(func):
#
#     def new_divi(a,b):
#         if a<b:
#             a,b=b,a
#         return func (a,b)
#     return new_divi
# divi1 = inner_divi(divi)
# divi(4,2)


# def square(n):
#     for i in range(n):
#         yield i*i
#
# square_list=list(square(10))
# print(square_list)
#

# class A:
#     def display(self):
#         print("display the show")
# class B(A):
#     def show(self):
#         print("show the display")
# ab=B()
# ab.show()
# ab.display()

# for i in range(10):
#    if i==7:
#     break
#    print(i,end=",")

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
#     def emp_info(self):
#         print(f"the name of the employee is {self.name} & the age of employee is {self.age} and salary of employee is {self.salary}")
# e=Employee('sohit',25,100000)
# e.emp_info()

# def func(*args,**kwargs):
#     print("we welcome you",args,kwargs)
#
# f=func('sir',5546,roll=123)

# def merge(d1,d2):
#     return(d2.update(d1))
#
# d1= {'ram':12,'sham':15}
# d2= {'raj':23,'praj':20}
#
# print(merge(d1,d2))
# print(d2)

# l1=[i for i in range(11) if i%2==0]
# print(l1)

# def merge(d1,d2):
#     return(d2.update(d1))
# d1={'rahul':25,'mahesh':21}
# d2={'sahul':15,'jahesh':71}
#
# (merge(d1,d2))
# print(d2)


# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
#
# def make_sound(animal):
#     animal.make_sound()
#
# dog = Dog()
# cat = Cat()
#
# make_sound(dog)
# make_sound(cat)
#

# class MyClass:
#
#   @staticmethod
#   def create_object(self):
#     return MyClass()
#
# object = MyClass.create_object()
# print(object)

# def merge(d1,d2):
#   return(d2.update(d1) )
# d1={'ram':25,'sham':45}
# d2={'r':5,'s':4}
#
# merge(d1,d2)
# print(d2)


# try:
#   for i in range(1,10):
#      if i%2==0:
#       print("the number is divisibele")
# except:


# a=input("enter the number please:")
# print(f"multiplication of table of {a}")
# try:
#  for i in range(1,11):
#    print(f"int{a} X {i} = {int(a)*i}")
# except ValueError:
#   print("Invalid Input!")
# print("end of the program")

# deep copy
# l=[[1,2],[3,4]]
# dp=copy.deepcopy(l)
# dp[0][1]=47
#
# print(dp)
# print(l)

# shallow copy
# l2=[[7,8],[[9,10]]]
# sc=copy.copy(l2)
# sc[0][1]=13
# print(sc)
# print(l2)

# n=int(input("enter the number"))
# for in range(0,n):
#   for j in range(0,i+1):

# list1=[12,3,4]
# list2=[1,45,7]
# list1.extend(list2)
# print(list1)

# t1=(1,2,3)
# t2=(4,5,6)
#
# d={t1:'first',t2:'second'}
# print(d)

# l1=[1,2,3]
# l2=[5,6,7]
#
# d={l1:'first',l2:'second'}
# print(d)

lis=[1,2,3,4,5]

cube= list(map(lambda x:x**3,lis))
print(cube)