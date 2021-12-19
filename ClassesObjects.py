class Person:
    'This is the base class for all Persons registered'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hello my name is {self.name} and I\'m {self.age} years old.')
list = []
person_instance = Person('Andrew', '61')
# call function introduce()
person_instance.introduce()
print(person_instance.name)
print(person_instance.age)
list.append(person_instance.name)
list.append(person_instance.age)
print(list)

