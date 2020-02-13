from room import Room
from player import Player
from item import  Item

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# PLAYER
# player = Player(input('What is thoust name? '), room['outside'])
player1 = Player('A-aron', room['outside'], 'spatula')


def command_parcer(player):
    quit = False

    while not quit: 
        print(f"Current Room Status:\n", player.current_room)

        command = input(f"\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(G)rab Item*\n(D)rop Item*\n(Q)uit\nCommand: ")
        command = command.lower().strip()
        # current_room = player.current_room
        # next_room = getattr(current_room, f'{command}_to')

        if command == 'q':
            quit = True
        if command == '':
            continue
        if command in ['n', 's', 'e', 'w']:
            # player.current_room = next_room
            player.move(command)

        else:
            print('There isn\'t a room there.')

        # if command == 'n' and player.current_room.n_to is not None:
        #     player.current_room = player.current_room.n_to
        #     print(f'You go North into...\n', current_room.n_to )

        # if command == 's' and player.current_room.s_to is not None:
        #     player.current_room = player.current_room.s_to
        #     print(f'You turn South and enter....\n {current_room}')

        # if command == 'e' and room.current_room.e_to is not None:
        #     player.current_room = player.current_room.e_to
        #     print(f'You head East to...\n {current_room}')

        # if command == 'w' and player.current_room.w_to is not None:
        #     player.current_room = player.current_room.w_to
        #     print(f'You go West to...\n {current_room}')

        # else:
        #     print("There isn\'t a room there.")
    
command_parcer(player1)
