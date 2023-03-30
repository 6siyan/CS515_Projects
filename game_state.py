

class Game_state(object):
    def __init__(self, curr_room) -> None:
        self.curr_room = curr_room
        self.personal_item = []

global GS
GS = Game_state(1)