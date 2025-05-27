# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Apply decorator
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
