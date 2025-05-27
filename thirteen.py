class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Using Engine's method via Car

# Creating an Engine object
my_engine = Engine()

# Passing the Engine object to Car
my_car = Car(my_engine)

# Starting the car (which starts the engine)
print(my_car.start_car())
