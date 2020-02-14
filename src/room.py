# Implement a class to hold room info: name, description attributes.

class Room:
    def __init__(self, name, description, r_items=[]):
        self.name = name
        self.description = description
        self.r_items = r_items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


    def __str__(self):
        return f"STR: {self.name}\n {self.description}\n There is a {self.r_items}/n"
    def __repr__(self):
        return f"REPR: {self.name}\n {self.description}\n There is a {self.r_items}\n"

    def return_item(self, item):
        self.r_items.append(item)

    def remove_item(self, item):
        self.r_items.remove(item)