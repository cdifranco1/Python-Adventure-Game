from utils import slow_print


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        slow_print(f'You have picked up {self.description}')