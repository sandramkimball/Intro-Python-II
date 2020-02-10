# Write a class to hold player information, e.g. current room, items

player_items = []
current_room = ''

def p_items(player_items, argv):
    for i in argv:
        player_items = player_items.append(i)
    
    for i in player_items:
        return f"{i}"

def get_item(player_items, item):
    player_items = player_items.append(item)
    return f"You picked up a {item}."

def drop_item(player_items, item):
    for i in player_items:
        if i == item:
            player_items.remove(i)
            return f"Item dropped."


class Player:
    def __init__(self, name, current_room, player_items):
        self.name = name
        self.current_room = current_room
        self.player_items = player_items

    def __str__(self):
        return f"{self.name} is in the {self.current_room}."

# PART 2:
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser


