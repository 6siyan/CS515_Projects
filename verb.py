from game_state import GS
from resources import map_data,person_data
from desc_print import *

class Verb(object):
    def __init__(self) -> None:
        pass

def go(destination):
    if destination in map_data[GS.curr_room_id]["exits"].keys():
        GS.curr_room_id = map_data[GS.curr_room_id]["exits"][destination]
    else:
        print("Sorry, you need to 'go' somewhere.")

def look():
    print_room()

def get(item):
    if item in map_data[GS.curr_room_id]["items"]: #need do a repeat check here.
        # and not in person_data
        map_data[GS.curr_room_id]["items"].remove(item)
        person_data.append(item)
    else:
        print("No item here, call Chinese Factory now.")

def inventory():
    if len(person_data) == 0:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        print(person_data)



verb_dict = {"go": go, 
             "look": look, 
             "get": get, 
             "inventory": inventory}
