from room import Room
from character import Enemy, Friend
from item import Item

# create rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")
cellar = Room("Cellar")
drawing_room = Room("Drawing room")
pantry = Room("Pantry")
hall = Room("Hall")
bedroom = Room("Bedroom")

# set descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A grand room with chandeliers and a grandfather clock in the corner.")
dining_hall.set_description("A cold room with a large table and 18 chairs covered with cobwebs.")
cellar.set_description("A spooky, cavernous room crawling with spiders.")
drawing_room.set_description("A cosy room with two sofas and a blazing fire.")
pantry.set_description("A musty room containing bottles of silver polish and knife sharpeners.")
hall.set_description("A galleried reception room with a grand central staircase.")
bedroom.set_description("A large room with a four-poster bed and window overlooking the park.")

# linking rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
kitchen.link_room(cellar, "east")
cellar.link_room(kitchen, "west")
cellar.link_room(pantry, "south")
pantry.link_room(cellar, "north")
pantry.link_room(dining_hall, "west")
dining_hall.link_room(pantry, "east")
ballroom.link_room(drawing_room, "south")
drawing_room.link_room(ballroom, "north")
dining_hall.link_room(hall, "south")
hall.link_room(dining_hall, "north")
hall.link_room(bedroom, "east")
bedroom.link_room(hall, "west")
drawing_room.link_room(hall, "east")
hall.link_room(drawing_room, "west")

# create enemies
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I hate hot baths!")
dave.set_weakness("soap")
gert = Enemy("Gert", "A scary ghost")
gert.set_conversation("I'm going to scare you to death!")
gert.set_weakness("water")
dining_hall.set_character(dave)
bedroom.set_character(gert)

# create friends
catrina = Friend("Catrina", "A friendly skeleton with a big floppy hat.")
catrina.set_conversation("I'm here to help you.")
belinda = Friend("Belinda", "A friendly witch with a black cat.")
belinda.set_conversation("Cast a spell and all will be well!")
cellar.set_character(catrina)
drawing_room.set_character(belinda)

current_room = kitchen
items = {}
charms = 0
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is None:
        print("This is room is empty.")
    else:
        inhabitant.describe()
    if isinstance(inhabitant, Friend):
        response = input(f"Would you like one of {inhabitant.get_name()}'s lucky charms? ")
        if response == "yes":
            charms = charms + inhabitant.offer_charm()
            print(f"Your charm count is now {charms}")
    response = input("What would you like to do: leave, choose an item, talk or fight? ")
    if response == "talk":
        try:
            print(f"OK, {inhabitant.name} says {inhabitant.conversation}")
        except AttributeError:
            print("Too bad, there's no-one around to talk :-(")
    elif response == "choose an item":
        item_name = input("What item can you see? > ")
        item = Item(item_name)
        colour = input(f"What colour is the {item.get_name()}? > ")
        item.set_colour(colour)
        print(f"You now have a {colour} {item.get_name()} to help you on your journey.")
        items[item.get_name()] = colour
        print(items)
    elif response == "fight":
        try:
            print("OK, what do you want to fight with? (Hint, the baddies never take a bath!)")
            fight_with = input()
            result = inhabitant.fight(fight_with)
            if result == False:
                if charms > 0:
                    charms -= 1
                    print(f"You're lucky, one of your charms has saved you this time.  Your charm count is now {charms}")
                else:
                    print("You've run out of charms and you're out of luck too!")
                    break
        except AttributeError:
            print("It's your lucky day - no-one's around to fight!")
    command = input("Which way do you want to go? > ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        print("Hello")

print("You've lost the game, but you do have these souvenirs of your journey:")
for k, v in items.items():
    print(v, k)
print("Goodbye!")