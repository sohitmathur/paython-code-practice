class Employee:
    def __init__(self,name,id,salary):

        self.name=name
        self.id=id
        self.salary=salary
        print("Empoyee details")
    def get_detail(self):
        print(f"the name of a employee is {self.name}")
        print(f"the id of a employee is {self.id}")
        print(f"the salary of a employee is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning Sir")
sohit = Employee('sohit',101,100000)
sohit.greet()
sohit.get_detail()