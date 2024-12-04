class HotelRoom:
    def __init__(self, room_number, rate_per_night):
        self.room_number = room_number
        self.rate_per_night = rate_per_night
        self.is_occupied = False  # Initially set to False

    def book_room(self):
        """Marks the room as occupied."""
        if not self.is_occupied:
            self.is_occupied = True
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is already occupied.")

    def checkout_room(self):
        """Marks the room as vacant."""
        if self.is_occupied:
            self.is_occupied = False
            print(f"Room {self.room_number} has been checked out.")
        else:
            print(f"Room {self.room_number} is already vacant.")

    def display_status(self):
        """Displays the room number, rate, and occupancy status."""
        status = "Occupied" if self.is_occupied else "Vacant"
        print(f"Room Number: {self.room_number}")
        print(f"Rate per Night: ${self.rate_per_night}")
        print(f"Status: {status}")

# Example usage
def hotel_room_management_task():
    # Create a new hotel room
    room101 = HotelRoom(101, 150)
    
    # Display initial status
    room101.display_status()
    
    # Book the room
    room101.book_room()
    
    # Display status after booking
    room101.display_status()
    
    # Check out of the room
    room101.checkout_room()
    
    # Display status after checkout
    room101.display_status()

# Execute the task
hotel_room_management_task()
