class Employee:
    def __init__(self,name,salary):
        #public
        self.name=name
        #private
        self._salary=salary
    def show(self):
        print("Name is",self.name,"and salary is",self._salary)
emp=Employee("Riya",40000)
emp.show()
print(emp.name)
##salary is not working because it private
