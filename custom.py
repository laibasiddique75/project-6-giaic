# Define custom exception
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Age is valid.")

# Test the function with try...except
try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)
