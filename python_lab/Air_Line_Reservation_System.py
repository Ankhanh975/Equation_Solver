class Person:
    def __init__(self, name, age, passport_number):
        self.__name = name  
        self.__age = age    
        self.__passport_number = passport_number  

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_passport_number(self):
        return self.__passport_number


class Passenger(Person):
    def __init__(self, name, age, passport_number):
        super().__init__(name, age, passport_number)


class Seat:
    def __init__(self, seat_number):
        self.__seat_number = seat_number  
        self.__is_reserved = False
        self.__passenger = None

    def reserve(self, passenger):
        if not self.__is_reserved:
            self.__passenger = passenger
            self.__is_reserved = True
            return True
        return False

    def cancel_reservation(self):
        if self.__is_reserved:
            self.__passenger = None
            self.__is_reserved = False
            return True
        return False

    def get_seat_number(self):
        return self.__seat_number

    def is_reserved(self):
        return self.__is_reserved

    def get_passenger(self):
        return self.__passenger


class Flight:
    def __init__(self, flight_number, destination, departure_time, total_seats):
        self.__flight_number = flight_number  
        self.__destination = destination  
        self.__departure_time = departure_time  
        self.__seats = [Seat(seat_number) for seat_number in range(1, total_seats + 1)]

    def book_seat(self, passenger):
        for seat in self.__seats:
            if not seat.is_reserved():
                if seat.reserve(passenger):
                    print(f"Seat {seat.get_seat_number()} successfully booked for {passenger.get_name()}.")
                    return
        print("No available seats on this flight.")

    def cancel_reservation(self, passport_number):
        for seat in self.__seats:
            if seat.is_reserved() and seat.get_passenger().get_passport_number() == passport_number:
                if seat.cancel_reservation():
                    print(f"Reservation for {seat.get_passenger().get_name()} (Passport: {passport_number}) has been canceled.")
                    return
        print("Reservation not found.")

    def display_details(self):
        available_seats = sum(1 for seat in self.__seats if not seat.is_reserved())
        print(f"Flight {self.__flight_number} | Destination: {self.__destination} | Departure: {self.__departure_time} | Available Seats: {available_seats}/{len(self.__seats)}")

    def display_passenger_list(self):
        print(f"Passengers on Flight {self.__flight_number}:")
        for seat in self.__seats:
            if seat.is_reserved():
                print(f"- Seat {seat.get_seat_number()}: {seat.get_passenger().get_name()} (Passport: {seat.get_passenger().get_passport_number()})")

    def get_flight_number(self):
        return self.__flight_number

    def get_destination(self):
        return self.__destination


class AirlineSystem:
    def __init__(self):
        self.__flights = []

    def add_flight(self, flight_number, destination, departure_time, total_seats):
        flight = Flight(flight_number, destination, departure_time, total_seats)
        self.__flights.append(flight)
        print(f"Flight {flight_number} added successfully!")

    def view_flights(self):
        print("\nAvailable Flights:")
        for flight in self.__flights:
            flight.display_details()

    def find_flight_by_number(self, flight_number):
        for flight in self.__flights:
            if flight.get_flight_number() == flight_number:
                return flight
        return None

    def find_flight_by_destination(self, destination):
        flights_found = [flight for flight in self.__flights if flight.get_destination().lower() == destination.lower()]
        return flights_found

    def book_seat(self):
        flight_number = input("Enter Flight Number: ")
        flight = self.find_flight_by_number(flight_number)
        if flight:
            name = input("Enter Passenger Name: ")
            age = int(input("Enter Passenger Age: "))
            passport = input("Enter Passport Number: ")
            passenger = Passenger(name, age, passport)
            flight.book_seat(passenger)
        else:
            print("Flight not found.")

    def cancel_reservation(self):
        flight_number = input("Enter Flight Number: ")
        flight = self.find_flight_by_number(flight_number)
        if flight:
            passport = input("Enter Passport Number: ")
            flight.cancel_reservation(passport)
        else:
            print("Flight not found.")

    def view_passengers(self):
        flight_number = input("Enter Flight Number: ")
        flight = self.find_flight_by_number(flight_number)
        if flight:
            flight.display_passenger_list()
        else:
            print("Flight not found.")

    def search_flight_by_destination(self):
        destination = input("Enter Destination: ")
        flights = self.find_flight_by_destination(destination)
        if flights:
            print("\nFlights to", destination, ":")
            for flight in flights:
                flight.display_details()
        else:
            print("No flights found for this destination.")

    def menu(self):
        while True:
            print("\n1. Add Flight\n2. Book Seat\n3. Cancel Reservation\n4. View Flights\n5. View Passenger Details\n6. Search Flight by Destination\n7. Exit")
            choice = input("Enter your choice: ")
            try:
                if choice == '1':
                    flight_number = input("Enter Flight Number: ")
                    destination = input("Enter Destination: ")
                    departure_time = input("Enter Departure Time: ")
                    total_seats = int(input("Enter Total Seats: "))
                    self.add_flight(flight_number, destination, departure_time, total_seats)
                elif choice == '2':
                    self.book_seat()
                elif choice == '3':
                    self.cancel_reservation()
                elif choice == '4':
                    self.view_flights()
                elif choice == '5':
                    self.view_passengers()
                elif choice == '6':
                    self.search_flight_by_destination()
                elif choice == '7':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    system = AirlineSystem()
    system.menu()
