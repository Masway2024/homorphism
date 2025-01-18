# Parent class - Vehicle
class Vehicle:
    def move(self):
        pass  # The move method is common, but it will be defined in child classes

# Subclass - Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Creating objects of Car and Plane
vehicle1 = Car()
vehicle2 = Plane()

# Demonstrating polymorphism
vehicle1.move()  # Output: Driving 🚗
vehicle2.move()  # Output: Flying ✈️
