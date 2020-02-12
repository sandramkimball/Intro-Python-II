# Implement a class to hold room info: name, description attributes.

class Room:
    def __init__(self, name, description, r_item, direction, item):
        self.name = name
        self.description = description
        self.r_item = r_item

    r_items=[]
    item=''

    def __str__(self):
        return f'Room: {+self.name}\n {self.description}\n The room contains a {self.r_item}.'

    # set state of direction of room for 'map'
    def room_link(self, name, command):
        if command == 'n':
            name = name.n_to
        if command == 's':
            name = name.s_to
        if command == 'e':
            name = name.e_to
        if command == 'w':
            name = name.w_to
        else:
            print('That is not an option.')

    def return_item(self, command, r_items, item):
        if command=='d':
           r_items.append(item)

    def remove_item(self, command, r_items, item):
        if command=='g':
            for i in r_items:
                if i == item:
                    r_items.remove(i)    

# add directional
# Make rooms able to hold multiple items
# Make the player able to carry multiple items