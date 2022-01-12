class Item():
    def __init__(self, name):
        self.name = name
        self.description = None
        self.colour = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return description

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return colour


# Any additional attributes and methods you would like to add
# Don’t forget to test your Item class by importing item in main.py, creating an Item object, and then calling the methods.
