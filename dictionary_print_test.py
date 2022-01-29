# testing dictionary display
from room import Room

# create rooms
dining_hall = Room("Dining hall")
hall = Room("Hall")
bedroom = Room("Bedroom")

# linking rooms together
dining_hall.link_room(hall, "south")
hall.link_room(dining_hall, "north")
hall.link_room(bedroom, "east")
bedroom.link_room(hall, "west")

# test 1 - returns dictionary self.linked_rooms = {} from Room class
print('Test 1:\n', hall.linked_rooms)

# returns values from dictionary
print('Test 2:')
for key in hall.linked_rooms:
    print(key, '->', hall.linked_rooms[key].name)