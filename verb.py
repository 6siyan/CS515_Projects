from game_state import GS
from resources import map_data,person_data
from desc_print import *

class Verb(object):
    def __init__(self) -> None:
        pass

def go(destination = None):
    if destination == None:
        print("Sorry, you need to 'go' somewhere.")
    elif destination in map_data[GS.curr_room_id]["exits"].keys():
        if "locked" in map_data[map_data[GS.curr_room_id]["exits"][destination]] and map_data[map_data[GS.curr_room_id]["exits"][destination]]["locked"] == 'yes' and 'key' not in person_data: # this means to check the next rooms locking state.
            print("This is locked, you need find a key first!")
        else:
            GS.curr_room_id = map_data[GS.curr_room_id]["exits"][destination]
            print("You go " + destination + '.')
            print()
            print_room(map_data[GS.curr_room_id])
    else:
        print(f"There's no way to go {destination}.")


def look():
    print_room(map_data[GS.curr_room_id])

def get(item = None):
    if item == None:
        print("Sorry, you need to 'get' something.")
    elif item in map_data[GS.curr_room_id]["items"]: #need do a repeat check here.
        # and not in person_data
        map_data[GS.curr_room_id]["items"].remove(item)
        person_data.append(item)
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} anywhere.")

def inventory():
    if len(person_data) == 0:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        print("\n".join(map(str, person_data)))
        #print(str(person_data)[1:-1])

def drop(item = None):
    if item == None:
        print("Sorry, you need to 'drop' something.")
    elif item in person_data:
        person_data.remove(item)
        map_data[GS.curr_room_id]["items"].append(item)
        print(f"You drop off the {item}.")
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
            "drop" : drop,
            "d": drop 
}
