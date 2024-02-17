# single inheritance
# class Employee:
#     company= 'Google'
#     def get_info(self):
#         print("this is an Employee")
# class Programmer(Employee):
#     company = 'Youtube'
#     def work(self):
#         print('this is office work')
# a=Employee()
# print(a.company)
# b=Programmer()
# a.get_info()
# b.work()
# print(b.company)
# b.get_info()

# multilevel inheritance

# class Freelancer:
#     company='fiverr'
#     level=0
#     def upgrade_level(self):
#         self.level=self.level+1
# class Visa():
#     def visa_info(self):
#         print('this is visa')
# class Programmer(Freelancer,Visa):
#     name='sohit'
# p= Programmer()
# p.upgrade_level()
# print(p.company)
# print(p.level)

class Employee:
    company='microsoft'
    salary=100000
    id=101
    @classmethod
    def change_sal(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
print(e.change_sal(455))
print(e.salary)
print(Employee.salary)



