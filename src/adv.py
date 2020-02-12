from room import Room
from player import Player

# Make a new player that is currently 'outside'.
# Write a loop that prints current room name and description.
# If user enters a cardinal direction, move to the room there.
# Print error message if the movement isn't allowed.
# If the user enters "q", quit the game.

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", "Salami"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", "Flower Pot"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", "Rubber Shamshir"),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", "Moose Head"),

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

class Directions:
    def __init__(self, room):
        self.room = room

    def n_to(self, room):
        return room['room'].n_to

    def s_to(self, room):
        return room['room'].s_to

    def e_to(self, room):
        return room['room'].e_to

    def w_to(self, room):
        return room['room'].w_to


def command_parcer(player, room, ):
    current_room = player.current_room    
    quit = False
    # def n_to(self, room):
    #     return room['room'].n_to

    # def s_to(self, room):
    #     return room['room'].s_to

    # def e_to(self, room):
    #     return room['room'].e_to

    # def w_to(self, room):
    #     return room['room'].w_to
    
    while not quit: 
        print(f"Current Room Status:\n", current_room)
        command = input(f"\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(G)rab Item*\n(D)rop Item*\n(Q)uit\nCommand: ")
        command = command.lower().strip()

        if command == '':
            continue

        if command == 'q':
            quit = True

        if command == 'n' and current_room.n_to:
            current_room = current_room.n_to
            print(f'You go North into...\n', current_room.n_to )

        if command == 's' and room[current_room].s_to:
            current_room = room[current_room].s_to
            print(f'You turn South and enter....\n {current_room}')

        if command == 'e' and room[current_room].e_to:
            current_room = room[current_room].e_to
            print(f'You head East to...\n {current_room}')

        if command == 'w' and room[current_room].w_to:
            current_room = room[current_room].w_to
            print(f'You go West to...\n {current_room}')

        else:
            print("There isn\'t a room there.")
    
player1 = Player('A-aron', room['outside'], 'key')
player2 = Player('Lafonda', room['outside'], 'spatula')
command_parcer(player1, room)


# Day 1 
# Create the REPL command parser in adv.py which allows the player to move to rooms in the four cardinal directions.
# COMPLETE: Fill out Player and Room classes in player.py and room.py 

# Day 2 
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser