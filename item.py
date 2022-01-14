class Item():
    def __init__(self, name):
        self.name = name
        self.description = None
        self.colour = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description