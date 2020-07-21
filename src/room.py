# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_items(self, *items):
        for item in items:
            self.items.append(item)
    
    def remove_item(self, item):
        self.items = [x for x in self.items if x != item]


    