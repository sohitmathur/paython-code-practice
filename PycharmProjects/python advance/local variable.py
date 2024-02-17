class Employee:
    company_name= 'Infosys'

    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def show(self):
        print("company name ::",Employee.company_name)
        print("Id :",self.id)
        print("Name:",self.name)
        print("Sal :",self.sal)
        bonus= self.bonus_cal(self.sal)

        print("*"*25)
        print("total sal before bonus::",self.sal)
        print("total sal after bonus::",self.sal+bonus)
        print("*"*25)

    def bonus_cal(self,sal):
        b= (self.sal*0.15)
        return b
obj = Employee(101,'sohit',100000)
obj.show()
