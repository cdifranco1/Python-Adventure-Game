from utils import slow_print

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
        elif args[0] == "i":
            self.show_inventory()
        else:
            self.move(args[0])

    def move(self, direction):
        err_msg = "\nYou can't move that direction! Choose a different direction.\n"
        try:
            next_room = getattr(self.current_room, f'{direction}_to')
            self.current_room = next_room
        except AttributeError:
            slow_print(err_msg)
    
    def grab_item(self, item_name):
        try:

            item = next(x for x in self.current_room.items if x.name == item_name)
            item.on_take()
            self.inventory.append(item)
            self.current_room.remove_item(item)
        except StopIteration:
            slow_print(f'Current room does not have {item_name}')
    
    def drop_item(self, item_name):
        try:
            item = next(x for x in self.inventory if x.name == item_name)
            self.inventory = [x for x in self.inventory if x.name != item_name]
            self.current_room.add_items(item)
        except StopIteration:
            slow_print(f'{item_name} is not in your inventory.')
    
    def show_inventory(self):
        slow_print('Inventory: ') 
        for i, x in enumerate(self.inventory):
            if i == len(self.inventory) - 1:
                print(x.name)
            else:
                print(f'{x.name},', end=" ")




        



    

