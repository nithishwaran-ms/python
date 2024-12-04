class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.fuel_level = 100  # Initial fuel level set to 100

    def drive(self, distance):
        """Reduces the fuel level based on the distance driven (1 unit of fuel per 10 km)."""
        fuel_needed = distance / 10
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Driven {distance} km. Fuel level is now {self.fuel_level}.")
        else:
            print(f"Not enough fuel to drive {distance} km. Please refuel.")

    def refuel(self, amount):
        """Increases the fuel level by the specified amount."""
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100  # Ensure fuel level doesn't exceed 100
        print(f"Refueled by {amount}. Fuel level is now {self.fuel_level}.")

    def display_status(self):
        """Displays the car’s make, model, and fuel level."""
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Fuel Level: {self.fuel_level}")

# Example usage
def car_simulation_task():
    # Create a new car
    my_car = Car("Toyota", "Corolla")
    
    # Display status
    my_car.display_status()
    
    # Drive the car for 50 km
    my_car.drive(50)
    
    # Display status again
    my_car.display_status()
    
    # Refuel the car by 30 units
    my_car.refuel(30)
    
    # Display status again
    my_car.display_status()

# Execute the task
car_simulation_task()

