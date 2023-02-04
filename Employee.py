class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __repr__(self):
        return self.name + "has a salary of " + str(self.salary) + ".00"



class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def __repr__(self):
        return self.name + "has a salary of " + str(self.salary) + ".00 and manages the " + self.department + " department"

class Executive(Manager):
    def __init__(self,name,salary,department):
        super().__init__(name,salary,department)
    def __repr__(self):
        return self.name + " has a salary of " + str(self.salary) + ".00 and is the executive for the " + self.department + " department"

employee = Employee("John Smith", 45000)
manager = Manager("Jane Doe", 60000, "Widgets")
executive = Executive("Weird Guy", 90000, "Thingies")

print(employee)
print(manager)
print(executive)



