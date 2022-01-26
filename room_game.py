from room import Room
from character import Enemy, Friend
from item import Item
from rpginfo import RPGInfo
import random

# create welcome message
haunted_manor_maze = RPGInfo("The Haunted Manor Maze")

# create rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")
cellar = Room("Cellar")
drawing_room = Room("Drawing room")
pantry = Room("Pantry")
hall = Room("Hall")
bedroom = Room("Bedroom")
rooms = [kitchen, ballroom, dining_hall, cellar, drawing_room, pantry, hall, bedroom]

# set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A grand room with chandeliers and a grandfather clock in the corner.")
dining_hall.set_description("A cold room with a large table and 18 chairs covered with cobwebs.")
cellar.set_description("A spooky, cavernous room crawling with spiders.")
drawing_room.set_description("A cosy room with two sofas and a blazing fire.")
pantry.set_description("A musty room containing bottles of silver polish and knife sharpeners.")
hall.set_description("A galleried room with a grand central staircase.")
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
gert.set_weakness("candle")
franky = Enemy("Franky", "A vicious vampire")
franky.set_conversation("My fangs can bite though anything except the one thing I hate!")
franky.set_weakness("garlic")

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

# create souvenirs
s1, s2, s3, s4, s5, s6, s7, s8 = (Item(), )*8
souvenir_items = [s1, s2, s3, s4, s5, s6, s7, s8]
souvenir_names = ['garlic', 'candle', 'soap', 'ruby', 'sword', 'rope', 'helmet', 'cloak']
souvenirs = []

for s in souvenir_items:
    x = random.randint(0, (len(souvenir_names)-1))
    s.name = souvenir_names.pop(x)
    souvenirs.append(s.name)

# position souvenirs in rooms
y = 0
for r in rooms:
    r.set_souvenir(souvenirs[y])
    y += 1

# functions
def end_game():
    if success == True:
        print(f"Congratulations!  You've survived two fights and successfully collected {Room.number_of_rooms} souvenirs:")
        print_backpack()
    else:
        print("You've no charms and you're out of luck too!")
        if backpack_count > 1:
            print("You've lost the game, but you do have these souvenirs of your journey:")
            print_backpack()
        elif backpack_count == 1:
            print("You've lost the game, but you do have this souvenir of your journey:")
            print_backpack()
        else:
            print("You've lost the game and have no souvenirs.")
    print(f"Thanks for playing {haunted_manor_maze.title}.  Goodbye!\n")
    RPGInfo.credits()
    quit()

def print_backpack():
    # prints contents of backpack
    for i in backpack:
        print(i)

# values at start of game
RPGInfo.author = "Andrew Watson"
current_room = kitchen
backpack = []
backpack_count = 0
charms = 0
fight = 0

# start the game
haunted_manor_maze.welcome()
RPGInfo.info()
print(f"\n{haunted_manor_maze.title.upper()}")
print(f"""{haunted_manor_maze.title} consists of {Room.number_of_rooms} rooms.  In the game, you must visit all the rooms
and collect a souvenir from each.  However, some ghosts and ghouls are lying in wait
to ambush you.  To win the game, you need to pick two fights with them, choosing one
of your souvenirs from your backpack to help defend you.  Lose a fight and you could
lose the game!  But don't worry, there are some friendly spooks who have special lucky
charms to help you.  Collect enough charms and you will be protected from the ghouls.
And if you stop and talk, you may pick up some helpful hints about what to fight the
ghouls with!

Can you emerge from the maze unscathed with {Room.number_of_rooms} souvenirs?  Good Luck! Here's the
first room...""")

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    object = current_room.get_souvenir()
    if inhabitant is None:
        print("There is no-one in this room.")
    else:
        inhabitant.describe()
    if isinstance(inhabitant, Friend):
        response = input(f"Would you like one of {inhabitant.get_name()}'s lucky charms? ")
        if response == "yes":
            charms = charms + inhabitant.offer_charm()
            print(f"Your charm count is now {charms}.\nYou can use your charm to fend off an enemy.")
    if current_room.item_status == True:
        print(f"You're lucky - there's a souvenir here!  Look for the {object}...")
    else:
        print("There are no souvenirs left in this room.")
    response = input("You can leave the room, collect a souvenir for your backpack, talk or fight.  What would you like to do? Type l, c, t or f. >  ")
    if response == "t":
        try:
            print(f"OK, {inhabitant.name} says {inhabitant.conversation}")
        except AttributeError:
            print("Too bad, there's no-one around to talk :-(")
    elif response == "c":
        if current_room.item_status == False:
            print("Sorry, you've already collected a souvenir here.  Try another room!")
        else:
            print(f"Well done!  You've now got the {object} to help you on your journey.")
            backpack.append(object)
            backpack_count = (len(backpack))
            current_room.item_status = False
            if backpack_count == Room.number_of_rooms and fight >= 2:
                success = True
                end_game()
            else:
                if backpack_count == 1:
                    print(f"You've {backpack_count} souvenir, your fight count is {fight} and your charm count {charms}.  Keep trying!")
                else:
                    print(f"You've {backpack_count} souvenirs, your fight count is {fight} and your charm count {charms}.  Keep trying!")
    elif response == "f":
        try:
            enemy_status = isinstance(inhabitant, Enemy)
            if enemy_status == True:
                fight +=1
            print("OK, what do you want to fight with? Choose something from your backpack:")
            print_backpack()
            while True:
                fight_with = input()
                if fight_with in backpack:
                    break
                elif backpack_count == 0:
                    print("You've nothing in your backpack yet.  You've nothing to defend yourself with!")
                    fight_with = None
                    break
                else:
                    print("Sorry, that's not in your backpack.  Try again!  > ")
            result = inhabitant.fight(fight_with)
            if result == False:
                if charms > 0:
                    charms -= 1
                    print(f"You're lucky, one of your charms has saved you.  Your charm count is now {charms}")
                    if backpack_count == Room.number_of_rooms and fight >= 2:
                        success = True
                        end_game()
                else:
                    success = False
                    end_game()
            else:
                if backpack_count == Room.number_of_rooms and fight >= 2:
                    success = True
                    end_game()
        except AttributeError:
            print("It's your lucky day - no-one's around to fight!")
    print("You can now go: ")
    current_room.get_directions()
    command = input("Choose your direction. > ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)