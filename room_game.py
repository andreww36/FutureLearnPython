from room import Room
from character import Enemy
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
ballroom.link_room(drawing_room, "south")
drawing_room.link_room(ballroom, "north")
dining_hall.link_room(hall, "south")
hall.link_room(dining_hall, "north")
hall.link_room(bedroom, "east")
bedroom.link_room(hall, "west")
drawing_room.link_room(hall, "east")
hall.link_room(drawing_room, "west")

# creating enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I'm dying for a hot bath!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is None:
        print("This is room is empty.")
    else:
        inhabitant.describe()
        response = input("What would you like to do?  Leave the room, choose an item, talk or fight? ")
        if response == "talk":
            print(f"OK, {inhabitant.name} says {inhabitant.conversation}")
        elif response == "choose an item":
            item_name = input("What item can you see? > ")
            item = Item(item_name)
            colour = input(f"What colour is the {item.get_name()}? > ")
            item.set_colour(colour)
            print(f"You now have a {colour} {item.get_name()} to help you on your journey.")
        elif response == "fight":
            print("OK, what do you want to fight with? ")
            fight_with = input()
            result = inhabitant.fight(fight_with)
            if result == False:
                break
    command = input("Which way do you want to go? > ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        print("Hello")

print("You've lost the game.  Goodbye!")