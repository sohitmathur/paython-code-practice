# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and

class Student:
    college_name = 'MIT Pune'
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def show(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("City is :",self.city)
        print(Student.college_name)
        return 'hi to anjali'
st1 = Student('Soht',25,'Pune')
result = st1.show()
print(result)


