# create a class with arguments defined which can be used as methods
# assign a class and arguments to an object
# run methods from the class on that object
class Patient:
    'This is the base class for all Patients registered'
    rec_sugar_intake_g = 37.5
    rec_fat_intake_g = 77
    rec_salt_intake_mg = 2300
    def __init__(self, name, sugar_intake_g, fat_intake_g, salt_intake_mg):
        self.name = name
        self.sugar_intake_g = sugar_intake_g
        self.fat_intake_g = fat_intake_g
        self.salt_intake_mg = salt_intake_mg
    def health_check(self):
        healthy = True
        if self.sugar_intake_g > float(self.rec_sugar_intake_g):
            print(f"{self.name}'s sugar intake is too high.")
            healthy = False
        if self.fat_intake_g > float(self.rec_fat_intake_g):
            print(f"{self.name}'s fat intake is too high.")
            healthy = False
        if self.salt_intake_mg > float(self.rec_salt_intake_mg):
            print(f"{self.name}'s salt intake is too high.")
            healthy = False
        if healthy == True:
            print(f"{self.name} is healthy.")
    def __str__ (self):
        return self.name, self.sugar_intake_g, self.fat_intake_g, self.salt_intake_mg

# creates instance of Patient
def create_patient():
    name = input(f"Enter patient {i}'s name: ")
    sugar_intake_g = int(input(f"Enter patient {i}'s sugar intake in grams: "))
    fat_intake_g = int(input(f"Enter patient {i}'s fat intake in grams: "))
    salt_intake_mg = int(input(f"Enter patient {i}'s fat intake in miligrams: "))
    patient = Patient(name, sugar_intake_g, fat_intake_g, salt_intake_mg)
    print('Here is your record:')
    print(f'{patient.name} has sugar intake {patient.sugar_intake_g}g, fat intake {patient.fat_intake_g}g, and salt intake {patient.salt_intake_mg}mg.')
    patient.health_check()

print("This app assesses a patient’s daily nutritional intake.")
records = int(input('How many patient records would you like to create? '))
for i in range(records):
    i += 1
    create_patient()
print('Thank you for using this app.')