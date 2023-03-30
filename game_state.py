

class Game_state(object):
    def __init__(self, curr_room = 0, personal_item = []) -> None:
        self.curr_room = curr_room
        self.personal_item = personal_item

global GS
GS = Game_state(1)