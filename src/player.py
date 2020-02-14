# Write a class to hold player information, e.g. current room, items

class Player:
    def __init__(self, name, current_room, p_items=[]):
        self.name = name
        self.current_room = current_room
        self.p_items = p_items

    def __str__(self):
        return f"{self.name} is in the {self.current_room}."

    def move(self, command):
        next_room = getattr(self.current_room, f"{command}_to")
        if next_room is not None:
            self.current_room = next_room
            print('You enter the', self.current_room)
        else:
            print('There\'s a wall there.')

    def get_item(self, item):
        self.p_items.append(item)
        print(f"You picked up a {item}.\n Inventory: \n {self.p_items}")

    def drop_item(self, item):
        self.p_items.remove(item)
        print(f'You dropped the {item}. \n Inventory: \n {self.p_items}')



