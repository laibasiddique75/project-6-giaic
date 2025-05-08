 # 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Test the function outside the class
result = MathUtils.add(5, 7)
print("Sum of my 2 numbers is:", result)
