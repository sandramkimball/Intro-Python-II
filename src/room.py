# Implement a class to hold room info: name, description attributes.

class Room:
    def __init__(self, name, description, item, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.item = item
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def list(self, *argv):
        return argv

    def __str__(self):
        return f'Room: {self.name}\n {self.description}\n You also see a {self.r_items}.'

    #actions(functions):
    def return_item(self, command, items):
        if command=='d':
           list.append(item)

    def remove_item(self, command, items):
        if command=='g':
            for i in list:
                if i == item:
                    list.remove(i)    

# add directions for linked rooms
# Make rooms able to hold multiple items
# add 'direction' and 'item' to params???? def a mini class for item?
# how tf to pass params between classes