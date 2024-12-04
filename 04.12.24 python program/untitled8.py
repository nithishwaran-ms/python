class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities

    def add_item(self, item, quantity):
        """Adds a specified quantity of an item to the cart."""
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} of {item} to the cart.")

    def remove_item(self, item, quantity):
        """Removes a specified quantity of an item from the cart."""
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
                print(f"Removed {quantity} of {item} from the cart.")
            elif self.items[item] == quantity:
                del self.items[item]
                print(f"Removed all {item} from the cart.")
            else:
                print(f"Cannot remove {quantity} of {item}. Only {self.items[item]} available.")
        else:
            print(f"{item} is not in the cart.")

    def view_cart(self):
        """Displays all items in the cart along with their quantities."""
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

    def clear_cart(self):
        """Clears all items from the cart."""
        self.items.clear()
        print("All items have been removed from your cart.")

# Example Task: Demonstrating the ShoppingCart class
def shopping_cart_task():
    # Create a new shopping cart
    cart = ShoppingCart()
    
    # Add items to the cart
    cart.add_item("Apple", 3)
    cart.add_item("Banana", 2)
    
    # View items in the cart
    cart.view_cart()
    
    # Remove an item
    cart.remove_item("Apple", 1)
    
    # View items in the cart again
    cart.view_cart()
    
    # Clear the cart
    cart.clear_cart()
    
    # View items in the cart again
    cart.view_cart()

# Execute the task
shopping_cart_task()
