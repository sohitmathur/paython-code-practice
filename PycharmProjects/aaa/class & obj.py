# class person:
#     name='sohit'
#     professtion='dj'
#     age = 25
#     networth=1000000
#     def info (self):
#       print(f"{self.name} is a {self.professtion} his networth is {self.networth}")
#
#
#
# a= person()
# a.name= 'shubham'
# a.networth=1000
# # print(person.name,person.networth)
# a.info()


# class Number:
#     def sum(self):
#         return self.a+ self.b
#
# num = Number()
# num.a = 12
# num.b = 45
# j = num.sum()
# print(j)

# class RailwayForm:
#     form = "Railwayform"
#     def printdata(self):
#         print(f"costumer name is {self.name} & and salary is {self.sal}")
# rail= RailwayForm()
# rail.name= "sohit"
# rail.sal= 100000
# s = rail.printdata()
# print(s)

class Employee:
    company='spacex'
    def empdetail(self,signature):
        print(f"the name of the company is {self.company} and the salary of an employee is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning Sir")
sohit=Employee()
sohit.salary=100000
sohit.empdetail('thanks!')
sohit.greet()
