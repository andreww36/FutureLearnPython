class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!" )
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def check_friend(self):
        return False

    def get_name(self):
        return self.name

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

class Friend(Character):
    lucky_charm = 3

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def offer_charm(self):
        if self.lucky_charm == 0:
            print("Sorry, I've no more charms left :-(")
        else:
            self.lucky_charm -= 1
            if self.lucky_charm == 1:
                print(f"{self.name} has {self.lucky_charm} lucky charm left.")
            else:
                print(f"{self.name} has {self.lucky_charm} lucky charms left.")
            print("You can use your charm to fend off an enemy.")
            return 1