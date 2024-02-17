# a = int(input('enter the  1st number:'))
# b= int(input('enter the 2nd number:'))
# print('the average of the two number is:',(a+b)/2)
# a= input('enter the number :')
# print(type(a))

# num=int(input("enter the number:"))
# print("the square of number is :",num*num)

# rahul_info=('rahul is a handsome guy')
# print(rahul_info.replace('rahul','pankaj'))
#
# user= (input('enter the name please:'))
# print('Good Morning\n',user)


# letter= """Dear <|Name|>
# you are selected\nas a data Scientest!your joining date will be \n<|Date|>"""
#
# letter=letter.replace('<|Name|>','Sohit')
# letter=letter.replace('<|Date|>','15 augest')
# print(letter.format('letter'))


# l1= (4,5,8,25,36,45,8)
# print((l1))

# a=[12,36,53,89,0,0,0]
# print(a.count(0))

# dict={'name':'raj','city':'pune','sal':100000}
# print(dict.setdefault('name'))
# print(dict)

# l1={1,2,3}
# print(type(l1))



# Dict={'Hindu':'sanatani','Ram':'hindu bhagwan','Sita':'hindu Goddess'}
# print("option are",Dict.keys())
# a=input('please enter the word:')
# print("the meaning of the word is:",Dict.get(a))

# num1= int(input("enter the number 1:"))
# num2= int(input("enter the number 2:"))
# num3= int(input("enter the number 3:"))
# num4= int(input("enter the number 4:"))
# num5= int(input("enter the number 5:"))
# num6= int(input("enter the number 6:"))
# num7= int(input("enter the number 7:"))
# my_list={num1,num2,num3,num4,num5,num6,num7}
# print(my_list)
#

# list = {18,"18"}
# print(list)

# s= set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

# fav_lang= {}
# f1= (input("enter the favorite language shubham:\n"))
# f2= (input("enter the favorite language harshita:\n"))
# f3= (input("enter the favorite language pooja:\n"))
# f4= (input("enter the favorite language neha:\n"))
# fav_lang['shubham']=f1
# fav_lang['harshita']=f2
# fav_lang['pooja']=f3
# fav_lang['neha']=f4
# print(fav_lang)

# num1=int(input("enter the number 1:\n"))
# num2=int(input("enter the number 2:\n"))
# num3=int(input("enter the number 3:\n"))
# num4=int(input("enter the number 4:\n"))
#
# if (num1>num4):
#     f1=num1
# else:
#     f1=num4
# if (num2>num3):
#     f2=num2
# else:
#     f2=num3
# if(f1>f2):
#     print(f"{f1} is the greatest")
# else:
#     print(f"{f2} is the greatest")

# sub1=int(input("enter the marks sub 1:\n"))
# sub2=int(input("enter the marks sub 2:\n"))
# sub3=int(input("enter the marks sub 3:\n"))
#
# if (sub1<33 or sub2 <33 or sub3 < 33):
#     print("you are failed in exam due to less marks in the subject")
# elif(sub1+sub2+sub3/3<40):
#     print("you are filed beacuse of less of less marks")
# else:
#     print("you are passed")
#

# text=input("enter the text:\n")
# if ("make a lot of money " in text):
#     spam=True
# elif("buy now " in text ):
#     spam=True
# elif("subscribe to my youtube channel" in text):
#     spam=True
# else:
#     spam=False
# if(spam):
#     print("this text is spam")
# else:
#     print("its not a spam")

# usernm=input("please enter username:\n")
# if (len(usernm)>10):
#     print("it contain more than 10 charecters")
# else:
#     print("it contains less than 10 charecters")
#



# names=["raj","shubham","pankaj","raju"]
# name=input("enter a name please:\n")
# if (name in names):
#     print("the name is present ")
# else:
#     print("name is not present ")

# mark=int(input("enter the mark please:"))
# if (mark >= 90 or mark==100):
#     print("you got an Ex grade")
# elif(mark>= 80 or mark==90):
#     print("you got grate A")
# elif(mark>=70 or mark==80):
#     print("you got grade B")
# elif(mark>=60 or mark==70):
#     print("you got grade C")
# elif(mark>=50 or mark==60):
#     print("you got grade D")
# elif(mark<50):
#     print("sry you are fail! try again next year")

# name=('harry')
# post= input("plesese write the post:")
# if (name in post.lower()):
#     print("this post about the harry")
# else:
#     print("this post is not about harry")
#

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num}x{i} =",num*i)

# l1 = ["harry","sam","sony","ajay"]
# for name in l1:
#      if name.startswith("s"):
#       print(f"hello {name} we welcome u at taj hotel")
#

# num=int(input("enter the number:"))
# i=1
# while num*num:
#     print()

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num}X{i}",num*i)

# l1= int(input("enter the number please:"))
# prime=True
# for i in range(2,l1):
#     if l1%i ==0:
#         prime=False
#         break
# if prime:
#     print("its prime number")
# else:
#     print("its not")

# num=int(input("enter the number:"))
# fatrorial=1
# for i in range(1,num+1):
#     factorial =fatrorial * i
# print(f"the factorial of {num} is {factorial}")


# n=3
# for i in range(5):
#     print("*"* i)

# marks =[78,89,62,96,98]
# percentage=(sum(marks)/500)*100
# print(percentage)

# def percentage(marks):
#       p=(sum(marks)/500)*100
#       return p
# marks1 =[78,89,62,96,98]
# percentage1=percentage(marks1)
# print(percentage1)

# def greeting(name="stranger"):
#       print("Good Morning",name)
#
# # costumer1=(input("enter the name:"))
# # print(greeting(costumer1))
# greeting("harry")
# greeting()

# def factorial(n):
#       if n==0 or n==1:
#             return 1
#       else:
#             return n*factorial(n-1)
# print(factorial(1))

# def gretest(num1,num2,num3):
#   if num1>num2:
#     if num1>num3:
#       return num1
#     else:
#       return num3
#   else:
#     if num2>num3:
#       return num2
#     else:
#       return num3
# g= gretest(12,13,85)
# print("the gretest no is",g)



# def ferhenite(cel):
#   return (cel * 9/5) + 32
# c=37
# print("ferhenite to celcius",ferhenite(37))

# print("Hello",end=" ")
# print("How",end=" ")
# print("Are",end=" ")
# print("You",end=" ")

# n=5
# for i in range(6):
#   print("*"*(n-i))


# def covetor(inch):
#   return(inch*2.54)
# c=11
# print("inch into centimeter",covetor(c))

# def split_and_remove(string,word):
#   new_string=string.replace(word,"")
#   return new_string.strip()
#
# me= "      harry is good boy       "
# n= split_and_remove(me,"harry")
# print(n)

# def table(num):
#   print(f"the table of {num} is ")
#   for i in range(1, 11):
#     print(f"{num}X{i}={num * i}")
#
# no=int(input("enter the number:"))
# table(no)


# with open('another.txt','r') as f:
#   a=f.read()
#   if 'this'in a:
#       print("yes its present")
#   else:
#       print("its not present ")



# class employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def get_details(self):
#         print(f"the name of the employee is {self.name}")
#         print(f"the age of the employee is {self.age}")
#         print(f"the salary of the employee is {self.salary}")
#
#     company = "Google"
#     def get_salary(self,signature):
#         print(f"the salary of an employee working in {self.company} is {self.salary}\n{signature}")
#     # @staticmethod
#     # def greet():
#     #     print(f"Good Morning Sir")
#
# harry=employee('raj',24,100000)
# harry.get_details()

# sejal=employee()
# harry.salary=100000
# harry.greet()
# harry.get_salary('Thanks!')
# # employee.get_salary('harry')

# sejal.salary=200000

# print(harry.company)
# print(sejal.company)
# employee.company="Youtube"
# print(harry.company)

# print(harry.salary)
# print(sejal.salary)


# class Employee:
#     def __init__(self,name,salary,company):
#         self.name=name
#         self.salary=salary
#         self.company=company
#     def get_Details(self):
#         print(f"the name of the employee is {self.name}")
#         print(f"the salary of the employee is {self.salary}")
#         print(f"the company of the employee is {self.company}")
#
# company=Employee("harry",10,"Microsoft")
# company.get_Details()

# class Calculator:
#     def __init__(self,num):
#         self.num=num
#
#
#     def squre(self):
#         print(f"the square of the {self.num} is {self.num **2}")
#     def cube(self):
#         print(f"the cube of the given {self.num} is {self.num **3}")
#     def square_root(self):
#         print(f"the squre of {self.num} is {self.num **0.5}")
#
#     @staticmethod
#     def greet():
#         print("hello please enter the number:")
#
#
# cal=Calculator(5)
# cal.greet()
# cal.squre()
# cal.cube()
# cal.square_root()


# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#     def get_Status(self):
#         print(f"the name of train is: {self.name}")
#         print(f"the seat are available in train is: {self.seats}")
#     def fare_Info(self):
#         print(f"the fare of train is Rs.{self.fare}")
#     def book_Ticket(self):
#         if self.seats > 0:
#             print(f"your ticket is has been booked!your seat no is {self.seats}")
#             self.seats=self.seats-1
#         else:
#             print("sorry the train is full! kindly try tatkal")
#
#
# intercity=Train("Intercity Express",100,2)
# intercity.get_Status()
# intercity.book_Ticket()
# intercity.book_Ticket()
# intercity.book_Ticket()
# intercity.get_Status()
# # intercity.fare_Info()


# class Employee:
#      company="Google"
#      def show_Details(self):
#          print("this is employee")
# class Programmer(Employee):
#     language="python"
#     def get_Language(self):
#         print(f"the programming language is {self.language}")
# a=Employee()
# a.show_Details()
#
# p=Programmer()
# p.show_Details()


# class Employee:
#     company="Youtube"
#     Ecode=456217
#     name="sohit"
# class Freelancer:
#     company="Goggle"
#     level=4
#     Ecode=4562174
#
# class programmer(Employee,Freelancer):
#     name="Rohit"
#     level=2
# p=programmer
# print(p.Ecode)
# print(p.name)

# class Employee:
#     company="Google"
#     salary=100
#     @classmethod
#     def changeSalary(cls,sal):
#         cls.salary=sal
#
#
# e=Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(e.salary)
#

# class Employee:
#     company="Youtube"
#     salary=500
#     bonus=100
#     @property
#     def total_Salary(self):
#         return self.salary+self.bonus
#
# e=Employee()
# e.total_Salary()
# print(e.total_Salary)


# class Animal:
#     mammmel='Tigar'
#
# class Pets(Animal):
#     colour="yellow"
# class Dog(Pets):
#     def bark(self):
#         print("barak bauhh bauhhh")
# a=Animal()
# p=Pets()
# d=Dog()
# d.bark()

# class Employee:
#     salary=100000
#     sal_increment=1.5
#     @property
#     def salaryafterIncrement(self):
#         return self.salary*self.sal_increment
#
#
#     @salaryafterIncrement.setter
#     def salaryafterIncrement(self,sai):
#         self.salary*self. increment
#         self.increment =sai/self.salary
#
# e=Employee()
# e.salaryafterIncrement = 2000
# print(e.sal_increment)

# while(True):
#     print("press q to quit")
#     a=(input("enter the number:"))
#     if a=='q':
#         break
#     a=int(a)
#     if (a>6):
#       print("the entered number is greater than 6")
#     else:
#       print("enter number is less than 6")
# print("Thanks for playing this game")

# while(True):
#     print("press q to exit")
#     a=(input("enter the number:"))
#     if a=='q':
#         break
#     try:
#      a=int(a)
#      if a>9:
#       print("entered number is greater than 9")
#      else:
#          print(f"{a} is lesser than given no")
#     except Exception as e:
#         print(f"please write valid input {e}")
#
#
# print("thank you for plying this game")
#
# while(True):
#  try:
#     a=int(input("enter the number:"))
#     c=5/a
#     print(c)
#  except ValueError as e:
#      print("please enter a valid input")
#      print(e)
#
#  except ZeroDivisionError as e:
#   print(f"make sure your not dividing as zero")
#   print(e)
#
# print("thanks for using this game")
#

# def increment(num):
#     try:
#      return int(num) +1
#     except:
#      raise ValueError ("this is not good")
#     finally:
#         print("we are done")
#
# a= increment(63)
# print(a)

# try:
#     i = int(input("enter the number:"))
#     c=1/i
# except Exception as e:
#     print(e)
# finally:
#     print("we are done")
# print("thanks for using this program")

# a=54
# def num():
#     global a
#     print(f"print statment 1: {a}")
#     a=23
#     print(f"print statment 2:{a}")
# num()
# print(a)

# list=[5,8,9,'False',996,'True']
# for index,item in enumerate(list):
#     print(item,index)


# a=[7,8,9,63,369,2,568,235]
# b=[]
# for item in a:
#  if item%2==0:
#     b.append(item)
#     print(item)
# b=[i for i in a if i%2==0]
# c=[i for i in a if i%2!=0]
# print(b)
# print(c)

# t= [5,8,6,3,2,1,2,3,1]
# s={i for i in t}
# print(s)

# l= [7,5,9,3,5,6,6,8,9]
# for i,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#      print(item,i)

# num= int(input("enter the number:"))
# table=[num*i for i in range (1,11)]
# print(table)

# sqaure= lambda a:a*a
# sum=lambda a,b,c:a+b+c
#
# a=12
# b=15
# c=18
# print(sqaure(a))
# print(sum(a,b,c))
#


# l= ['mango','apple','banana','stawberry']
#
# line= "\n".join(l)
# print(line)

# city='pune'
# name='sohit'
# job= "Ds"
#
# print(" hello this is {0} and my city is {1} & his job is {2}" .format(name,city,job))


# def squre(num):
#     return num*num
#
# l1=[1,5,6,87]
# l2=[]
# for i in l1:
#     l2.append(squre(i))
# print(l2)

# print(list(map(squre,l1)))

# def greater_no(num):
#     if num>10:
#         return True
#     else:
#         return False

# l=[1,5,6,39,85,2,3,45]
# print(list(filter(greater_no,l)))

# from functools import reduce
# sum= lambda a,b:a+b
# l = [1, 5, 6, 39, 85, 2, 3, 45]
# val=(reduce(sum,l))
# print(val)

# name=input("enter the name please:")
# marks=int(input("enter the marks please:"))
# phone_no=int(input("enter the phone no please:"))
# print("the name of the student is {} his marks  are {}  and phone number is {}".format(name,marks,phone_no))

# num=int(input("enter the number:"))
# l1=[str(7*i) for i in range(1,11)]
# # print(l1)
# vertical_Table="\n".join(l1)
# print(vertical_Table)
# for i in range(1,11):
#     print("the table of 7 is:",num*i)



# def divisible(num):
#     if num%5==0:
#         return True
#     else:
#         return False

# l1=[1,56,36,89,23,12,5,25,35]
#
# a= filter(lambda a:a%5==0,l1)
# print(list(a))
#

from functools import reduce

l=[1,8,5,36,894]
a= reduce(max,l)
print(a)