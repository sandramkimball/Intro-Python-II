# Implement a class to hold room info: name, description attributes.
from item import  Item

# class item_list:
#     def __init__(self, *argv):
#         self.argv = argv

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'{self.name}\n {self.description}'

    
    #actions(functions):
    # def return_item(self, command, item):
    #     if command=='d':
    #        item_list.append(item)

    # def remove_item(self, command, item):
    #     if command=='g':
    #         for i in item_list:
    #             if i == item:
    #                 item_list.remove(i)    

    
# Item('Cat', 'Looks mean')
# Item('Katana', 'It\'s super sharp.')