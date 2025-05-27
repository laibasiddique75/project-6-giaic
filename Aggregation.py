class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Reference to existing Employee object

    def show_details(self):
        print(f"Department: {self.department_name}")
        print(f"Employee: {self.employee.name}")

# Create an Employee object (independent)
emp = Employee("Ali")

# Pass the Employee object to Department (aggregation)
dept = Department("HR", emp)

# Show department and employee details
dept.show_details()
