# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object and call the added method
p = Person("Ali")
print(p.greet())
