# 1 class Programmer:
#     company = 'Microsoft'
#
#     def __init__(self, name, desginitaion, salary):
#         self.name = name
#         self.desginitaion = desginitaion
#         self.salary = salary
#
#     def getinfo(self):
#         print(f"employee name is {self.name}")
#         print(f"employee desginitaion  is {self.desginitaion}")
#         print(f"employee salary is {self.salary}")
#
#
# sohit = Programmer('sohit', 'data scientist', 100000)
# sakshi= Programmer('sakshi','tester',200000)
# sohit.getinfo()
# sakshi.getinfo()

# 2.
# class Calculator:
#     def __init__(self, number):
#         self.number = number
#     @staticmethod
#     def greet():
#         print('HELLO')
#     def squre(self):
#         print(f"the square of {self.number} is {self.number ** 2}")
#
#     def squre_root(self):
#         print(f"the square root of {self.number} is {self.number ** 0.5}")
#
#     def cube(self):
#         print(f"the cube of {self.number} is {self.number ** 3}")
#
#
# a = Calculator(3)
# a.greet()
# a.squre()
# a.squre_root()
# a.cube()

# 3.
# class Sample:
#     a = 'harry'
#
# obj = Sample()
# obj.a='sohit'
# Sample.a='sohit'
# print(Sample.a)
# print(obj.a)

# 4.

# class Train:
#     def __init__(self, train_name, seats, fare):
#         self.train_name = train_name
#         self.seats = seats
#         self.fare = fare
#
#     def get_info(self):
#         print("****************")
#         print(f"the train name is {self.train_name}")
#         print(f"the seats are available in train {self.seats}")
#         print("****************")
#
#     def fare_info(self):
#         print(f"the fare of the ticket is Rs {self.fare}")
#
#     def book_ticket(self):
#         if (self.seats > 0):
#             print(f"your ticket has been booked! your seat no is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("sorry the train is boooked please try tatkal")
#
#
# intercity = Train('Intercity express 101', 90, 1)
# intercity.get_info()
# intercity.book_ticket()
# intercity.book_ticket()
# intercity.book_ticket()
# intercity.get_info()

# def sonali():
#     print('hii! how are you')
# sonu=sonali()
