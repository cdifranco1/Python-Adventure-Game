# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def perform_action(self, *args):
        if len(args) > 1:
            if args[0] == "grab":
                self.grab_item(args[1])
            if args[0] == "drop":
                self.drop_item(args[1])
        else:
            self.move(args[0])

    def move(self, direction):
        err_msg = "\nYou can't move that direction! Choose a different direction.\n"
        try:
            next_room = getattr(self.current_room, f'{direction}_to')
            self.current_room = next_room
        except AttributeError:
            print(err_msg)
    
    def grab_item(self, item_name):
        try:
            item = next(x for x in self.current_room.items if x.name == item_name)
            item.on_take()
            self.inventory.append(item)
            self.current_room.remove_item(item)
        except StopIteration:
            print(f'Current room does not have {item}')
    
    def drop_item(self, item_name):
        try:
            item = next(x for x in self.inventory if x.name == item_name)
            self.inventory = [x for x in self.inventory if x.name == item_name]
            self.current_room.add_items(item)
        except StopIteration:
            print(f'{item} is not in your inventory.')



        



    

