# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# import bs4
# import requests
#
#
# url='https://api.coindesk.com/v1/bpi/currentprice.json'
# data= requests.get(url)
# soup=bs4.BeautifulSoup(data.text,'html.parser')
# print(soup.prettify())
# # for para in soup.find_all('p'):
# #     print(para.text)
# # for links in soup.find_all('p'):
# #     link=links.get('href')
# #     print('link')


# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#
#
#     def emp_info(self):
#       print(f"employee name is {self.name} and employee age is {self.age}")
#
#
# e = Employee('rahul', 28)
# e.emp_info()

# lis={i for i in range(10)if i%2}
# dict={i:i*i for i in range(1,11)}
# print(lis)
# print(dict)

# swap the number

# num1=int(input("enter the number 1:"))
# num2=int(input("enter the number 2:"))
#
# num1,num2=num2,num1
# temp=num1
# num1=num2
# num2=temp
#
# print("values after swaping no 1 is:",num1)
# print("values after swaping no 2 is:",num2)

# prime number
# num=int(input("enter the number please:"))
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count ==2:
#             print("its prime number")
#     else:
#             print("number is not prime")

# factorial=1
# num=int(input("enter the number please:"))
#
# if num<0:
#     print("the factorial for negative number does not exits")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"the num is {num} & its factorial is {factorial}")

# recursation
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#          return n* factorial(n-1)
# num=5
# print("the factorial of",num,"is",factorial(num))

# n1=0
# n2=1
#
# print(n1)
# print(n2)
#
# for i in range(2,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

# n1=12
# n2=15
# print("before swaping no is",n1)
# print("before swaping no is",n2)
# # n1,n2=n2,n1
#
# temp=n1
# n1=n2
# n2=temp
#
# print("after the swaping no are",n1)
# print("after the swaping no are",n2)

# prime no

# num=int(input("enter the number please:"))
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print(f"{num} is prime number")
#     else:
#         print(f"the {num} is not a prime number")

# factorial=1
# num=10
#
# if num<0:
#     print("the factorial of negative number does not exits")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"the factorial for the {num} is {factorial}")

# recursation


# def facorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * facorial(n-1)
# num=10
# f=facorial(10)
# print(f)
# print(f"the facorial of {num} is {facorial(num)}")

# fabonic number
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,10):
#     sum=a+b
#     print(sum)
#     a=b
#     b=sum

# find the length of list

# mylist=[1,2,5,6,8]
# print(mylist)
# count=0
# for i in mylist:
#     count=count+1
# print(f"the length of the list is {count}")

# swaping of the number

# input=[0, 2, 0, 3, 8, 0, 5]
# print(input)
# pos1,pos2=1,-2
# input[pos1],input[pos2]=input[pos2],input[pos1]
# print(input)

# input.sort()
# print(Input)


# print(input)

# Output: [0, 0, 0, 2, 3, 8, 5]
# Input[1]=Input[-2]
# print(Input)

# Input[3]=Input[5]

# =Input[]
# print(Input)

 # mylist=[1,8,6,9,13,52]
# length=len(mylist)
# temp=mylist[0]
# mylist[0]=mylist[-1]
# mylist[-1]=temp

# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print(mylist)

# how to find nth occurance word
# mylist=["geeks","for","geeks"]
# word="geeks"
# n=2
# count=0
# for i in range(0,len(mylist)):
#     if (mylist[i]==word):
#         count=count+1
#         if count==n:
#             del mylist[i]
# print(mylist)

# how to search element in list
# mylist=[1,8,9,3,5]
# element=5
# flag=0
# for i in mylist:
#     if i==element:
#         flag=1
#         break
#
# if flag==1:
#     print("element is found")
# else:
#     print("element is not found")

# mylist=[1,8,9,3,5]
# ele=3
# count=0
#
# if ele in mylist:
#     if ele==mylist:
#
#      print("element is found")
# else:
#     print("its not present")

# mylist=[1,8,9,3,5]
# reverse_List=mylist[::-1]
# print(reverse_List)

# mylist=[1,8,9,3,5]
# mynewlist=[i for i in mylist]
# print(mynewlist)

# count occurance in the element
# mylist=[1,8,9,3,5,1,8,9,3,9]
# x=5
# count=0
# for ele in mylist:
#     if ele==x:
#         count=count+1
# print(f"the {x} repeated for {count}")

# mylist=[10,8,5]
# result=1
# for i in mylist:
#     result=result*i
#
# print(result)
# def multiply(a,b,c):
#     return lambda a,b,c:a*b*c
#
# print(multiply(1,4,5))

# palindrome

# user=input("enter the string please:")
# reverse=user[::-1]
# print(reverse)
# if user==reverse:
#     print("its palindrome string")
# else:
#     print("given string is not palindrome")

# str="welcome to this program"
# words=str.split(" ")
# print(str)
# words=words[-1::-1]
# words=words[::-1]
# outputstr=' '.join(words)
# print(outputstr)

# how to find length of str

# str="we are all happy"
# counter=0
# for i in str:
#     counter=counter+1
# print(counter)

# to check special charecter in URl
import re
# str="we are so happy @,<>/: #%$ to have you"
# str2="we are so happy to have you"
#
# regax=re.compile('[@_<>/:#%$]')
# if (regax.search(str)==None):
#     print('no special charecter in the string')
# else:
#     print("it contain special charecter")

# import re
# str="I am Blogger at https://www.variables.sh/complex-regular-expression-examples/"
#
# url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
# print(url)

# def freq_word():
#     str=input("Please Enter the String:")
#     li=str.split()
#     d={}
#     for i in li:
#         if i not in d.keys():
#             d[i]=0
#         d[i]=d[i]+1
#     print(d)
#
# freq_word()

# converstion of two list into values:

# def conversation():
#     keys=[1,2,3]
#     values=["one","two","three"]
#     result=dict(zip(keys,values))
#     print (result)
# conversation()

# d={1: 'one', 2: 'two', 3: 'three'}
# print(d.items())

# def dict_to_item():
#     x={"one":1,"two":2,"three":3}
#     for i in x.items():
#         print(i)
# dict_to_item()

# list is slower than tuple.

# import timeit
# print=(timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]',number=10000000))
# print=(timeit.timeit('x=(1,2,3,4,5,6,7,8,9,10,11,12)',number=10000000))
import timeit

# {a:1,b:2,c:3}
# #
# # dict={a:a for a in range}
#
# lis=[i for i in range(1,10)]
# tup=({n:n for n in range(1,28)})
# print(tup)

#   Febonice number
# n1=0
# n2=1
# print(n1)
# print(n2)
#
# for i in range(2,11):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

# create febonice serice using genrator

# def fib_gen():
#     a=0
#     b=1
#     while True:
#         c=a
#         a=b
#         b=c+a
#         yield c
# f=fib_gen()
# for i in range(20):
#     print(next(f),end=" ")

# lis=[1,2,3,4,5,6]
# l=lis[::-1]
# print(l)

# how to merge two dict
# dic1={'red_bag':4,'blue_bag':8}
# dic2={'orange_bag':4,'white_bag':5}
# dic1.update(dic2)
# print(dic1)

# dic3={**dic1,**dic2}
# print(dic3)

# find unique value in the list
# l1=[1,2,3,5,6,1,2,3]
# ar= list(set(l1))
# print(ar)

# lis1=[]
# for i in l1:
#     if (i not in lis1):
#      lis1.append(i)
# print(lis1)

# remove_duplicte=lambda l1:set(l1)
# print(remove_duplicte(l1))

# li=[12,56,36,89,2,6,96,23,75,45]
# t=li.sort()
# print(li)
# print(f"largest element is ",li[-1])

# user=input("enter the string please:")
# reverse=user[::-1]
# if user==reverse:
#     print("its palindrome string")
# else:
#      print("its not palindrome")

# palindrome for string
# def palindrome(n):
#     reverse=n[::-1]
#     if reverse==n:
#         print("yes its palindrome string")
#     else:
#         print("given string is not palindrome")
# palindrome('non')

# def palindrome(num):
#     num=str(num)
#     reverse=num[::-1]
#     if reverse==num:
#         print("yes its palindrome string")
#     else:
#         print("given string is not palindrome")
# num=123122
# print(palindrome(num))

# def palindrome(n):
#     temp=n
#     rev_n=0
#     while(temp>0):
#         digit= temp%10
#         print(digit)
#         rev_n=rev_n *10+digit
#         temp= temp//10
#     if n== rev_n:
#         return True
#     else:
#         return False
#
# n=123
# p=palindrome(n)

# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

# def feb(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         sum=a+b
#         print(sum)
#         a=b
#         b=sum
# f=feb(7)

# recursition
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# num=5
# print(factorial(num))


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# n=10
# # print(factorial(n))
# print(f"the factorial of {n} is {factorial(n)}")

# i=1
#
# while i<=5:
#     print("Yes! indeed")
#     i=i+1

# def fizbuzz(n):
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print("Fizzbuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Fizz")
#         else:
#             print(i)
#
# fizbuzz(20)

#prime number

# num=int(input("enter the number please:"))
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("the number is prime number")
#     else:
#         print("its not a prime number")

# l1=[10,4,56,8,6,89,7,23]
# l= set(l1)
# print("second largest number is",l(-2))

# arr=[10,56,84,21,11,36,2]
# max=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]
# print(max)

# arr=[10,56,84,21,11,36,2]
# min=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]<min:
#         min=arr[i]
# print(min)

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=7
# print(factorial(n))

# f=open('oop')
# content=f.read()
# print(content)

# rotating list


def right_rotate(list,num):
    outputlist=[]
    for item in range(len(list)-num,len(list)):
        outputlist.append(list[item])
    for item in range(0,len(list)-num):
        outputlist.append(list[item])
    return outputlist

rotate_Number=3
list_1=[1,2,3,4,5]
print(right_rotate(list_1,rotate_Number))

# data=[1,2,3,4,5]
# it=iter(data)
# while True:
#     try:
#         print(next(it))
#     except Exception as e:
#             break

# data mangling
# class Test:
#     a=10
#     __b=20
# print(Test.a)
# print(Test._Test__b)

# lis=[1,2,5,6,'all','@']
# lis2=[]
# for i in lis:
#     if type(i)==str:
#         lis2.append(i)
# print(lis)
# print(lis2)

# decorator

# def dev(a,b):
#     print(a/b)
#
# def smart_dev(func):
#
#     def inner_dev(a,b):
#       if (a<b):
#         a,b=b,a
#         return func(a,b)
#
#     return inner_dev
# dev=smart_dev(dev)
#
# dev(4,5)
# list=[i for i in range(10) if i%2]
# print(list)

# dict={n:n*n for n in range(11)}
# print(dict)

# def genrator(n):
#     for i in range(1,n+1):
#         yield i*i
# g=genrator(3)
# print(next(g))
# print(next(g))
# print(next(g))

# class A:
#     def func1(self):
#         print("the func1 is running")
# class B:
#     def func2(self):
#         print("the func2 is running")
# class C(A,B):
#     def func3(self):
#         print("the func3 is running")
# first_class=C
# first_class.


# for i in range(1,10):
#     if i==7:
#         break
#     print(i,end=",")

# with open("oop") as f:
#  e=f.read()
# print(e)


# a=5
# b=0
# try:
#  print(a/b)
# except Exception as e:
#     print("the error is",e)

list=[12,2,5,69,12,1,12,1]
x=12
count=0
for i in list:
    if i==x:
        count=count+1
print(f"the number {x} has occured {count}")
