# Write a class, Weather, with three attributes: temperature, wind speed, and wind direction.
# Use the input() and print() functions, and your Weather class, to capture and describe the current weather data at your location.
# add a child class, VerbalWeather, that inherits attributes from Weather but converts the numerical inputs for temperature and
# wind speed into their matching verbal descriptions according to ranges (e.g. over 20°C is ‘warm’ and over 30 km/h is ‘windy’).

class Weather:
    'This is the base class for all weather readings'
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
    def weather_report(self):
        print(f"Today it is {self.temperature} ˚C, the wind speed is {self.wind_speed} mph coming form the {self.wind_direction}")

class Verbal(Weather):
    def verbal(self):
        if int(self.temperature) < 10:
            self.temperature = 'chilly'
        elif int(self.temperature) < 20:
           self.temperature = 'warm'
        else:
           self.temperature = 'hot'
        print(f"Today it is {self.temperature}", end="")
        if int(self.wind_speed) < 10:
            self.wind_speed = 'calm'
        elif int(self.wind_speed) < 30:
            self.wind_speed = 'breezy'
        else:
            self.wind_speed = 'blowing a gale'
        print(f" and {self.wind_speed}", end="")
        if self.wind_direction.lower() == 's':
            self.wind_direction = ' southerly'
        elif self.wind_direction.lower() == 'n':
            self.wind_direction = ' northerly'
        elif self.wind_direction.lower() == 'e':
            self.wind_direction = 'n easterly'
        else:
            self.wind_direction = ' westerly'
        print(f" with the wind coming from a{self.wind_direction} direction.")

def create_record():
    temperature = input("What's today's temperature in ˚C? ")
    wind_speed = input("What's today's wind speed in mph? ")
    wind_direction = input("What direction is the wind coming from? ")
    record = Weather(temperature, wind_speed, wind_direction)
    verbal = Verbal(temperature, wind_speed, wind_direction)
    verbal.verbal()

# intro
print("This app allows you to record your local weather.")
while True:
    create_record()
    response = input("Would you like to create another record? Y/N ")
    if response.lower() == 'n':
        break
print("Thank you for using this app!")
