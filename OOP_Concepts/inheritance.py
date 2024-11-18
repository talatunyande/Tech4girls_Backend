#!/usr/bin/python3
#  making a method called Employee
class Employee:
# initializing method init
    def __init__(self,name,position):
        self.name=name
        self.position =position
    def get_details (self):
        return f"{self.name} and i'm {self.position}"

#inheritance of Manager in Employee
class Manager(Employee):
    def __init__(self,name,position,department):
        self.department=department
#super allows the child to inherit the init attribute of the parent        
        super().__init__(name,position)
        
    def get_details(self):
        return f"{self.name} i'm a {self.position} at the {self.department}"
        
manager = Manager("Garba","manager", "operation department")
print(manager.get_details())
emp=Employee("NyandeTalatu","Organizer",)
print(emp.get_details())

