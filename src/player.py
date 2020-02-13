# Write a class to hold player information, e.g. current room, items

class Player:
    def __init__(self, name, current_room, p_items):
        self.name = name
        self.current_room = current_room
        self.p_items = p_items

    def __str__(self):
        return f"{self.name} is in the {self.current_room}."

    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
        else:
            print('There\'s a wall there.')

    def get_item(self, p_items, r_item):
        p_items.append(r_item)
        return f"You picked up a {r_item}."

    def drop_item(self, p_items, item):
        for i in p_items:
            if i == item:
                p_items.remove(i)
                print(Item dropped.)



