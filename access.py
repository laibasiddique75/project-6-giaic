 # 7. Access Modifiers: Public, Private, and Protected
 # Assignment:
 # Create a class Employee with:

 # a public variable name,

 # a protected variable _salary, and

 # a private variable __ssn.

 # Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary  # Protected attribute
        self.__ssn = ssn       # Private attribute

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be a positive number")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Private SSN via getter: {self.get_ssn()}")

# Create a Manager instance
m = Manager("Laiba", 30000, "123-45-6789", "HR")

# Show manager info
m.show_manager_info()

# Update salary
m.set_salary(35000)
print("Updated Salary:", m._salary)

# Accessing private variable the correct way
# Direct access (will raise AttributeError)
try:
    print(m.__ssn)
except AttributeError:
    print("Cannot access private attribute '__ssn' directly!")

# Accessing private variable using name mangling (not recommended)
print("Accessing private SSN via name mangling:", m._Employee__ssn)
