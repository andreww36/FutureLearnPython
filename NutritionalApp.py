# create a class with arguments defined which can be used as methods
# assign a class and arguments to an object
# run methods from the class on that object
# the <self> parameter is only used within the class defintion
class Patient:
    'This is the base class for all Patients registered'
    def __init__(self, name, sugar_intake_g, fat_intake_g, salt_intake_mg):
        self.name = name
        self.sugar_intake_g = sugar_intake_g
        self.fat_intake_g = fat_intake_g
        self.salt_intake_mg = salt_intake_mg
    def __str__ (self):
        return self.name, self.sugar_intake_g, self.fat_intake_g, self.salt_intake_mg

# creates multiple instances of Patient
def create_and_check_patient():
    records = input('How many patient records would you like to create?')
    for i in range(int(records)):
        i += 1
        name = input(f"Enter patient {i}'s name: ")
        sugar_intake_g = int(input(f"Enter patient {i}'s sugar intake in grams: "))
        fat_intake_g = int(input(f"Enter patient {i}'s fat intake in grams: "))
        salt_intake_mg = int(input(f"Enter patient {i}'s fat intake in miligrams: "))
        patient = Patient(name, sugar_intake_g, fat_intake_g, salt_intake_mg)
        print('Here is your record:')
        print(f'Patient {patient.name} has sugar intake {patient.sugar_intake_g}g, fat intake {patient.fat_intake_g}g, and salt intake {patient.salt_intake_mg}mg.')
        healthy = True
        if patient.sugar_intake_g > 37.5:
            print(f"{patient.name}'s sugar intake is too high.")
            healthy = False
        if patient.fat_intake_g > 77:
            print(f"{patient.name}'s fat intake is too high.")
            healthy = False
        if patient.salt_intake_mg > 2300:
            print(f"{patient.name}'s salt intake is too high.")
            healthy = False
        if healthy == True:
            print(f"{patient.name} is healthy.")
create_and_check_patient()