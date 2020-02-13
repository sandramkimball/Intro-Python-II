from room import Room
from player import Player
from item import  Item

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", r_items=[Item('Salami', 'Dry and spicy')]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",r_items=[Item('Moose Head', 'It stares into your soul')]),


    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", r_items=[Item('Katana', 'Bruh, it\'s super sharp.')]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", r_items=[Item('Legendary Squeeky Toy', 'Squeek squeeky squeek')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", r_items=[Item('Cat', 'Looks mean')]),
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


player = Player(input('What is thoust name? '), room['outside'], p_items=['Key'])

print(f"Current Room Status:\n", player.current_room)

while True:
    command = input(f"\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(G)rab Item*\n(D)rop Item*\n(Q)uit\nCommand: ")
    command = command.lower().strip()

    if command == 'q':
        exit()
    if command == '':
        continue
    if command in ['n', 's', 'e', 'w']:
        player.move(command)
        
    if command == 'g':
        player.get_item(player.current_room.r_items)
        # room[current_room].remove_item(player.current_room.r_items)

    if command == 'd':
        player.drop_item(player.current_room.r_items)
        # room[current_room].return_item(player.current_room.r_items)


    else:
        print('There isn\'t a room there.')
