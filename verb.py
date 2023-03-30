from game_state import GS

class Verb(object):
    def __init__(self) -> None:
        pass

def go(curr_room):
    destination = input("What would you like to do?")
    if destination in curr_room["exits"].keys():
        print(curr_room["exits"][destination])
    else:
        print("Sorry, you need to 'go' somewhere.")

verb_dict = {go(GS.curr_room): "go"}
