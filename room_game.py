from room import Room
from character import Enemy, Friend
from item import Item

def print_dictionary(d):
    for k, v in d.items():
        print(v, k)

def end_game():
    if success == True:
        print("Congratulations!  You've survived two fights and successfully collected eight souvenirs:")
    else:
        print("""You've run out of charms and you're out of luck too!
        You've lost the game, but you do have these souvenirs of your journey:""")
    print_dictionary(souvenirs)
    print("Thanks for playing the Haunted Manor Maze game.  Goodbye!")
    quit()

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
gert.set_conversation("I'm going to scare you to bits, but don't open those curtains!")
gert.set_weakness("light")
franky = Enemy("Franky", "A vicious vampire")
franky.set_conversation("My fangs can bite though anything except the one thing I hate!")

# create friends
catrina = Friend("Catrina", "A friendly skeleton with a big floppy hat.")
catrina.set_conversation("I'm here to help you.")
belinda = Friend("Belinda", "A friendly witch with a black cat.")
belinda.set_conversation("Cast a spell and all will be well!")

# position enemies and friends in rooms
dining_hall.set_character(dave)
hall.set_character(gert)
bedroom.set_character(franky)
cellar.set_character(catrina)
drawing_room.set_character(belinda)

current_room = kitchen
souvenirs = {}
charms = 0
fight = 0

# start the game
print("""
______________________________HAUNTED MANOR MAZE__________________________________

Welcome to the Haunted Manor Maze game.  The Haunted Manor consists of eight rooms.
In the game, you must visit all the room and collect a souvenir from each.
However, some ghosts and ghouls are lying in wait to ambush you.  To win the game,
you need to pick two fights with them.  Lose a fight and you could lose the game!
But don't worry, there are some friendly spooks who have special lucky charms to help
you.  Collect enough charms and you will be protected from the ghouls!

Can you emerge from the maze unscathed with eight souvenirs?  Good Luck! Here's the
first room...""")

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
            print(f"Your charm count is now {charms}.\nYou can use your charm to fend off an enemy.")
    response = input("You can leave the room, choose a souvenir, talk or fight.  What would you like to do? Type l, c, t or f. >  ")
    if response == "t":
        try:
            print(f"OK, {inhabitant.name} says {inhabitant.conversation}")
        except AttributeError:
            print("Too bad, there's no-one around to talk :-(")
    elif response == "c":
        if current_room.status == False:
            print("Sorry, you've already collected a souvenir here.  Try another room!")
        else:
            item_name = input("What item can you see? > ")
            item = Item(item_name)
            item_description = input(f"What's the {item.get_name()} like? > ")
            item.set_description(item_description)
            print(f"Well done!  You now have a {item.get_description()} {item.get_name()} to help you on your journey.")
            souvenirs[item.get_name()] = item_description
            souvenir_count = (len(souvenirs.keys()))
            current_room.status = False
            if souvenir_count == 8 and fight >= 2:
                end_game()
            else:
                print(f"You've {souvenir_count} souvenirs and your fight count is {fight}.  Keep trying!")
    elif response == "f":
        try:
            status = isinstance(inhabitant, Enemy)
            if status == True:
                fight +=1
            print("OK, what do you want to fight with? (Hint, the baddies never take a bath!)")
            fight_with = input()
            result = inhabitant.fight(fight_with)
            if result == False:
                if charms > 0:
                    charms -= 1
                    print(f"You're lucky, one of your charms has saved you this time.  Your charm count is now {charms}")
                    if souvenir_count == 8 and fight >= 2:
                        success = True
                        end_game()
                else:
                    success = False
                    end_game()
        except AttributeError:
            print("It's your lucky day - no-one's around to fight!")
    print("You can now go: ")
    current_room.get_directions()
    command = input("Choose your direction. > ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)