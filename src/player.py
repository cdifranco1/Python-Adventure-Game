# Write a class to hold player information, e.g. what room they are in
# currently.

direction_map = {'n': 'n_to'}

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        err_msg = "\nYou can't move that direction! Choose a different direction.\n"
        if direction == 'n':
            try:
                self.current_room = self.current_room.n_to
            except AttributeError:
                print(err_msg)
        if direction == 's':
            try:
                self.current_room = self.current_room.s_to
            except AttributeError:
                print(err_msg)
        if direction == 'e':
            try:
                self.current_room = self.current_room.e_to
            except AttributeError:
                print(err_msg)
        if direction == 'w':
            try:
                self.current_room = self.current_room.w_to
            except AttributeError:
                print(err_msg)
        



    

