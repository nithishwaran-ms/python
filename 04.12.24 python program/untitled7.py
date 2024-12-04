class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        """Returns the area of the rectangle."""
        return self.length * self.width

    def calculate_perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def is_square(self):
        """Checks if the rectangle is a square."""
        return self.length == self.width

# Example usage
rect1 = Rectangle(10, 5)
print(f"Area: {rect1.calculate_area()}")  # Output: 50
print(f"Perimeter: {rect1.calculate_perimeter()}")  # Output: 30
print(f"Is Square: {rect1.is_square()}")  # Output: False

rect2 = Rectangle(6, 6)
print(f"Area: {rect2.calculate_area()}")  # Output: 36
print(f"Perimeter: {rect2.calculate_perimeter()}")  # Output: 24
print(f"Is Square: {rect2.is_square()}")  # Output: True
