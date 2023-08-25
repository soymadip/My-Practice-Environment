class Employee:
    company = "apple"    
    def show(self):
       print(f"The name is {self.name} & company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany



e1 = Employee()
e1.name = "harry"
e1.show()
