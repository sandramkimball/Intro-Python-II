# Implement a class to hold room info: name, description attributes.

class Room:
    def __init__(self, name, description, r_items, direction):
        self.name = name
        self.description = description
        self.r_items = r_items
        self.direction = direction


    # r_items=[]

    def __str__(self):
        return f'Room: {self.name}\n {self.description}\n You also see a {self.r_items}.'

    #actions(functions):
    def return_item(self, command, r_items, item):
        if command=='d':
           r_items.append(item)

    def remove_item(self, command, r_items, item):
        if command=='g':
            for i in r_items:
                if i == item:
                    r_items.remove(i)    

# add directions for linked rooms
# Make rooms able to hold multiple items
# add 'direction' and 'item' to params???? def a mini class for item?
# how tf to pass params between classes