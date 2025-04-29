class Vehicle:
    def __init__(self, brand, model, year):
        """
        Constructor for the base Vehicle class.
        
        Args:
            brand (str): The brand of the vehicle
            model (str): The model of the vehicle
            year (int): The manufacturing year of the vehicle
        """
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        Returns the vehicle's information.
        
        Returns:
            str: A formatted string with vehicle details
        """
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        """
        Constructor for the Car class.
        
        Args:
            brand (str): The brand of the car
            model (str): The model of the car
            year (int): The manufacturing year of the car
            num_doors (int): The number of doors in the car
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        """
        Returns the car's information including number of doors.
        
        Returns:
            str: A formatted string with car details
        """
        base_info = super().display_info()
        return f"{base_info}, Number of doors: {self.num_doors}"

class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        """
        Constructor for the Truck class.
        
        Args:
            brand (str): The brand of the truck
            model (str): The model of the truck
            year (int): The manufacturing year of the truck
            payload_capacity (float): The payload capacity of the truck in kilograms
        """
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity
    
    def display_info(self):
        """
        Returns the truck's information including payload capacity.
        
        Returns:
            str: A formatted string with truck details
        """
        base_info = super().display_info()
        return f"{base_info}, Payload Capacity: {self.payload_capacity}"


# Only run main() if this script is run directly
if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        vehicle_info = input().split()
        
        if vehicle_info[0] == 'Car':
            vehicle = Car(vehicle_info[1], vehicle_info[2], 
                          int(vehicle_info[3]), int(vehicle_info[4]))
        elif vehicle_info[0] == 'Truck':
            vehicle = Truck(vehicle_info[1], vehicle_info[2], 
                            int(vehicle_info[3]), float(vehicle_info[4]))
        
        print(vehicle.display_info())