class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Displays the employee’s details."""
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

    def give_raise(self, percent):
        """Increases the salary by a specified percentage."""
        raise_amount = self.salary * (percent / 100)
        self.salary += raise_amount
        print(f"Salary increased by {percent}%. New salary is {self.salary}.")

# Example usage
def employee_management_task():
    # Create a new employee
    employee = Employee("Alice", "E001", 50000)

    # Display employee details
    employee.display_details()
    
    # Give a raise
    employee.give_raise(10)
    
    # Display employee details again
    employee.display_details()

# Execute the task
employee_management_task()
