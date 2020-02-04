# Implement a class to hold room info: name, description attributes.

room_items = []
        
def get_item(room_items, item):
    for i in room_items:
        if not item:
            room_items = room_items.append(item)

def drop_item(room_items, item):
    for i in room_items:
        if i == item:
            room_items.remove(i)


class Room:
    def __init__(self, name, description, r_item):
        self.name = name
        self.description = description
        self.r_item = r_item

# PART 2:
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser