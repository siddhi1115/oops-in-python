class Employee:
    def salary(self):
        print("Employee salary: 50000")

class Manager(Employee):
    def salary(self):
        print("Manager salary: 80000")

emp = Employee()
mgr = Manager()

emp.salary()
mgr.salary()