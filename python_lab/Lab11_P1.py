# A. Your Dream Car

class Car:
    def __init__(self, speed: float, consumption_rate: float) -> None:
        # Initiate speed and fuel for the car. Specifically, the car should have:

        # A class attribute speed, which is the speed of the car, having value of the input argument speed.
        # A class attribute consumption_rate, which is the fuel consumed rate per hour of the car, having value of the input argument consumption_rate.
        # A class attribute fuel_level, which is the fuel level of the car, having value of the
        self.speed = speed
        self.consumption_rate = consumption_rate
        self.fuel_level = 50  # Default fuel level as per problem description

    def can_reach(self, distance: float) -> bool:
        # Part (b): 
        # Can the car reach the given distance? 
        # Define the method can_reach for the car, 
        # which obtains distance as input and returns True 
        # if the car can reach the given distance based on given fuel level, False otherwise.
                # Calculate hours needed to travel the distance
        hours_needed = distance / self.speed
        
        # Calculate fuel needed for the journey
        fuel_needed = hours_needed * self.consumption_rate
        
        # Check if current fuel level is sufficient
        return self.fuel_level >= fuel_needed

    def refuel_cost(self, price_per_unit: float) -> float:
        # Part (c): Refuel cost Define the method refuel_cost for the car, which obtains price_per_unit as input and returns the cost to refuel the car back to 100 fuel levels. The formula for calculating the cost is
        # 100-price_per_unit*fuel_level
        # Calculate fuel needed to reach full tank
        
        fuel_to_add = 100 - self.fuel_level
        
        # Calculate total cost
        return fuel_to_add * price_per_unit




if __name__ == "__main__":
    # Input
    # The input has five components:

    # The integer displays the speed of the car, ranging from 1 to 100 (km/h).
    # The integer displays consumption rate per hour, ranging from 1 to 10
    # The integer displays the current fuel level, ranging from 0 to 100
    # The integer displays the distance the car needs to drive, ranging from 1 to 104
    # The integer displays the price to fill 1 unit of fuel, ranging from 1 to 50
    # Those numbers are given in one line, separated by space.
    speed, consumption_rate, fuel_level, distance, price_per_unit = map(int, input().split())
    car = Car(speed, consumption_rate)
    car.fuel_level = fuel_level
    
    # Output
    # The output has three lines:
    # The first line shows three car's attributes by calling the class' attributes, separating by space.
    # The second line shows the boolean value of whether the car can reach the given distance based on the given fuel level or not.
    # The third line shows the cost to refuel the car back to 100 fuel levels.
    print(f"{car.speed} {car.consumption_rate} {car.fuel_level}")
    print(car.can_reach(distance))
    print(car.refuel_cost(price_per_unit))