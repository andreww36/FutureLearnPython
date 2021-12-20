# Write a class, Weather, with three attributes: temperature, wind speed, and wind direction.
# Use the input() and print() functions, and your Weather class,
# to capture and describe the current weather data at your location.
# add a child class, VerbalWeather, that inherits attributes from Weather but converts the numerical
# inputs for temperature and wind speed into their matching verbal descriptions according to ranges
# (e.g. over 20°C is ‘warm’ and over 30 km/h is ‘windy’).

class Weather:
    'This is the base class for all weather readings'
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
    def weather_report(self):
        print(f"Today it is {self.temperature} ˚C, the wind speed is {self.wind_speed} mph coming form the {self.wind_direction}")

class Verbal(Weather):
    def weather_report(self):
        if int(self.temperature) < 10:
            self.temperature = 'chilly'
        elif int(self.temperature) < 20:
           self.temperature = 'warm'
        else:
           self.temperature = 'hot'
        print(f"Today it is {self.temperature} ˚C, the wind speed is {self.wind_speed} mph coming form the {self.wind_direction}")

def create_record():
    temperature = input("What's today's temperature in ˚C? ")
    wind_speed = input("What's today's wind speed in mph? ")
    wind_direction = input("What direction is the wind coming from? ")
    record = Weather(temperature, wind_speed, wind_direction)
    record.weather_report()
    record2 = Verbal(temperature, wind_speed, wind_direction)
    record2.weather_report()

# intro
print("This app allows you to record your local weather.")
create_record()