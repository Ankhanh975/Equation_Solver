# A. Vehicle Class Hierarchy

# Create a class hierarchy for vehicles, ensuring the following requirements:
# Base Class: Vehicle
# Attributes:
# brand (string): The brand of the vehicle.
# model (string): The model of the vehicle.
# year (integer): The manufacturing year of the vehicle.
# Methods:
# __init__(self, brand, model, year): Constructor to initialize the attributes.
# display_info(self): Returns the vehicle's information (brand, model, year).
class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    
# Derived Class: Car
# Inherits from: Vehicle.
# Additional Attribute:
# num_doors (integer): The number of doors in the car.
# Methods:
# __init__(self, brand, model, year, num_doors): Constructor to initialize the attributes.
# display_info(self): Returns the vehicle's information along with the number of doors.
# Derived Class: Truck
# Inherits from: Vehicle.
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of doors: {self.num_doors}"
    
# Additional Attribute:
# payload_capacity (float): The payload capacity of the truck in kilograms.
# Methods:
# __init__(self, brand, model, year, payload_capacity): Constructor to initialize the attributes.
# display_info(self): Returns the vehicle's information along with the payload capacity.
class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Payload Capacity: {self.payload_capacity}"

if __name__ == "__main__":
    # Input
    # The input consists of multiple lines:
    # The first line contains an integer n (1≤n≤10
    # ), representing the number of vehicles.
    # Each of the following n lines contains details of a vehicle:
    # For a Car: Car brand model year num_doors (e.g., Car Toyota Corolla 2020 4).
    # For a Truck: Truck brand model year payload_capacity (e.g., Truck Ford F150 2018 1500.5).

    n = int(input().strip())
    vehicles = []

    for _ in range(n):
        inputs = input().strip().split()
        
        if inputs[0] == 'Car':
            vehicle = Car(inputs[1], inputs[2], int(inputs[3]), int(inputs[4]))
        else:  # Truck
            vehicle = Truck(inputs[1], inputs[2], int(inputs[3]), float(inputs[4]))
        
        vehicles.append(vehicle)

    # Output
    # For each vehicle, display the complete information returned by the display_info() method. Ensure all details (brand, model, year, and either the number of doors or payload capacity) are displayed on the same line.
    for vehicle in vehicles:
        print(vehicle.display_info())
    
