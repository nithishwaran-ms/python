class Weather:
    def __init__(self, location, temperature, humidity):
        self.location = location
        self.temperature = temperature
        self.humidity = humidity

    def update_weather(self, temp, hum):
        """Updates the temperature and humidity."""
        self.temperature = temp
        self.humidity = hum
        print(f"Weather updated: Temperature = {self.temperature}°C, Humidity = {self.humidity}%")

    def display_weather(self):
        """Displays the weather details in a formatted way."""
        print(f"Weather Report for {self.location}:")
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")

# Example usage
def weather_report_task():
    # Create a new weather report for a location
    weather = Weather("New York", 22, 60)
    
    # Display the initial weather details
    weather.display_weather()
    
    # Update the weather
    weather.update_weather(25, 55)
    
    # Display the updated weather details
    weather.display_weather()

# Execute the task
weather_report_task()
