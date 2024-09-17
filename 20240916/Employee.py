class Employee:
    def __init__(self,name,address,code,salary):
        self.name=name
        self.address=address
        self.code=code
        self.salary=salary 
    def __str__(self): 
        return f'{self.name},{self.address},{self.code},{self.salary}'
    
emp1=Employee('dilli','6-2','python1',100000)
print(emp1)