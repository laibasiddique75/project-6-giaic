class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an object of Multiplier
m = Multiplier(5)

# Test if the object is callable
print("Is m callable?", callable(m))  # True

# Call the object like a function
result = m(10)
print("Result:", result)
