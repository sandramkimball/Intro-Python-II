# Write a class to hold player information, e.g. current room, items



class Player:
    def __init__(self, name, current_room, p_items):
        self.name = name
        self.current_room = current_room
        self.p_items = p_items

    p_items = []
    current_room = {}

    def __str__(self):
        return f"{self.name} is in the {self.current_room}."

    # def current_room():
    # def room_direction():

    def get_item(self, p_items, r_item):
        p_items.append(r_item)
        return f"You picked up a {r_item}."

    def drop_item(self, p_items, item):
        for i in p_items:
            if i == item:
                p_items.remove(i)
                return f"Item dropped."


# save direction: current and where moving to:
# command input sets room_direction? opposite?
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser


