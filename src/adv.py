from room import Room
from item import Item
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List of available directions
commands = ('n', 's', 'e', 'w', 'q', 'grab', 'drop')

# List of items

items = {
    'coins': Item('coins', "A bag of 20 gold coins."),
    'sword': Item('sword', "Rune scimmy."),
    'key': Item('key', "A golden key."),
    'armor': Item('armor', "Iron armor."),
    'shield': Item('shield', "Silver shield."),
    'treasure': Item('treasure', "You found the treasure!")
}

room['outside'].add_items(items['coins'])
room['foyer'].add_items(items['sword'])
room['overlook'].add_items(items['armor'])
room['narrow'].add_items(items['shield'])
room['treasure'].add_items(items['treasure'])



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

class Game:
    def __init__(self):
        self.playing = False
    
    def start_game(self):
        self.playing = True
        self.get_new_player()
        
        while self.playing:
            room = self.player.current_room
            print(f'\nCurrent Room: {room.name}')
            print(f'\n{room.description}')
            print(f'\nAvailable Items:')
            for i, x in enumerate(room.items):
                print(f'Item {i+1}: {x.name}')

            #get player's next move
            new_input = self.get_input()
            inputs = [x.lower() for x in new_input]
            
            #dispatch next move
            if new_input[0] == "q":
                self.playing = False 
            else:
                self.player.perform_action(*inputs)
    
    def get_input(self):
        error_message = "\nError: Enter a direction (N, S, E, W)"
        player_input = input("\nNext move: ").split()
        
        #check if action input
        if len(player_input) > 1:
            if player_input[0] in commands and player_input[1] in items:
                return player_input

        # check if valid direction
        elif player_input[0] in commands:
           return player_input[0]
        else:
            print(error_message)     

    def get_new_player(self):
        name = input("Welcome to the adventure game. What is your name?\n")
        self.player = Player(name, room["outside"])
        self.display_directions()
    
    def display_directions(self):
        print(f"\nWelcome {self.player.name}. You can select your next move by entering 'N', 'S', 'E', or 'W'. Enter 'q' to quit game.")
    

def main():
    game = Game()
    game.start_game()

main()



