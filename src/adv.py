from room import Room
from player import Player

# Make a new player that is currently 'outside'.
# Write a loop that prints current room name and description.
# If user enters a cardinal direction, move to the room there.
# Print error message if the movement isn't allowed.
# If the user enters "q", quit the game.

# PART 2:
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser


room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", "Salami"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", "Flower Pot"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", "Rubber Shamshir"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", "Moose Head"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", "Legendary Squeeky Toy"),
}

# Link rooms together
room['outside'].n_to = room['foyer'],
room['foyer'].s_to = room['outside'],
room['foyer'].n_to = room['overlook'],
room['foyer'].e_to = room['narrow'],
room['overlook'].s_to = room['foyer'],
room['narrow'].w_to = room['foyer'],
room['narrow'].n_to = room['treasure'],
room['treasure'].s_to = room['narrow']


# def find_room(current_room):
#    for k, v in room:
#         if k == current_room:
#             return v

print('PRINT THE DAMN ROOM VALUE:', room['outside'])


def status_report(player, room):
    current_room = player.current_room    
    quit = False
    
    while not quit: 
        command = input("(N)orth\n(S)outh\n(E)ast\n(W)est\n(Q)uit\nCommand: ")
        command = command.lower().strip()

        if command == '':
            continue

        if command == 'q':
            quit = True

        if command == 'n':
            current_room = room[current_room].n_to
            print(f'Current Room Status: {current_room}')

        elif command == 's' and room[current_room].s_to:
            current_room = room[current_room].s_to

        elif command == 'e' and room[current_room].e_to:
            current_room = room[current_room].e_to

        elif command == 'w' and room[current_room].w_to:
            current_room = room[current_room].w_to

        else:
            print("There isn\'t a room there.")

    print(f"Current Room: {current_room}\n Description:{current_room}")
    
player1 = Player('A-aron', 'outside', 'bat')
status_report(player1, room)
