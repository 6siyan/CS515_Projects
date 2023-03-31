from game_state import GS
from resources import map_data,person_data
from desc_print import *

class Verb(object):
    def __init__(self) -> None:
        pass

def go(destination):
    if destination in map_data[GS.curr_room_id]["exits"].keys():
        if map_data[map_data[GS.curr_room_id]["exits"][destination]]["locked"] == 'Yes' and 'key' not in person_data: # this means to check the next rooms locking state.
            print("This is locked, you need find a key first!")
        else:
            GS.curr_room_id = map_data[GS.curr_room_id]["exits"][destination]
            print("You go " + destination + '.')
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
        print("No this item in room, call Chinese Factory now.")

def inventory():
    if len(person_data) == 0:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        print(person_data)

def dorp(item):
    if item in person_data:
        person_data.remove(item)
        map_data[GS.curr_room_id]["items"].append(item)
    else:
        print("No this item in inventory, call Chinese Factory now.")



verb_dict_1 = {
             "look": look,
             "l": look, 
             "inventory": inventory,
             "i": inventory
             }

verb_dict_2 = {
            "go": go, 
            "g": go,
            "get": get,
            "ge": get,
            "dorp" : dorp,
            "d": dorp 
}
