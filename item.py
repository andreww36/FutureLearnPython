class Item():
    def __init__(self):
        self._name = None
        self._description = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        while True:
            try:
                value_test = int(value)
            except ValueError:
                self._name = value
                break
            else:
                value = input("Please enter text to name this item! > ")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        while True:
            try:
                value_test = int(description)
            except ValueError:
                self._description = description
                break
            else:
                description = input("Please enter text! > ")