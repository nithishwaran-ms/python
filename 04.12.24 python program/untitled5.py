class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        """Adds or updates marks for a specific subject."""
        self.marks[subject] = mark
        print(f"Marks for {subject} updated to {mark}.")

    def get_average(self):
        """Returns the average of all marks."""
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        return average_marks

    def display_details(self):
        """Displays the student’s name, roll number, and average marks."""
        average_marks = self.get_average()
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {average_marks:.2f}")

# Example Task: Demonstrating the Student class
def student_information_task():
    # Create a new student
    student = Student("Alice", "S001")
    
    # Add or update marks
    student.add_marks("Math", 85)
    student.add_marks("Science", 90)
    student.add_marks("History", 78)
    
    # Display student details
    student.display_details()

# Execute the task
student_information_task()
