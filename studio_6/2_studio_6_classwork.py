# This is the base class we are starting with.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# TODO: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=4):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def set_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def __str__(self):
        return f"max_speed: {self.max_speed}, mileage: {self.mileage}, seating_capacity: {self.seating_capacity}"

# TODO: Instantiate your Bus class to an object to a variable called school_bus, the max speed 80, and mileage 45000.

school_bus = Bus(80, 45000)

# TODO: Add seating_capacity as a parameter in the def __init__(), but give it a default property of 4 seating_capacity=4 and add self.seating_capacity = seating_capacity.

# TODO: Create a method in your Bus class called set_seating_capacity, which takes the parameter: seating_capacity and sets self.seating_capacity to equal the seating_capacity parameter.

# TODO: call school_bus.set_seating_capacity and pass a value of 42.

school_bus.set_seating_capacity(42)
# TODO: Override the __str__ function in the Bus class to print all of the properties onto a single line.

# TODO: Create a new class which will also inherit the Vehicle class (a different type of vehicle than a bus). Inherit everything from vehicle and add one more set_xxxx method to set a property of that vehicle. 

class Car(Vehicle):
    def __init__(self, max_speed, mileage, color):
        super().__init__(max_speed, mileage)
        self.color = color

    def set_color(self, color):
        self.color = color

# TODO: Push both new files to your remote Engr102 repository and copy and paste your repository URL as a submission.