class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}...{self.description}'

    def __str__(self):
        return f'{self.name}...{self.description}'


Item('Salami', 'Dry and spicy')
Item('Cat', 'Looks mean')
Item('Katana', 'Bruh, it\'s super sharp.')
Item('Moose Head', 'It stares into your soul')
Item('Legendary Squeeky Toy', 'Squeek squeeky squeek')