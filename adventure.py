import sys
import json
from game_state import GS
from description import *
from desc_print import *
from verb import *

if len(sys.argv) < 2:
    print("Please provide a filename")
    sys.exit()

filename = sys.argv[1]

# Open the JSON file
with open(filename) as f:
    # Load the data from the file using the `load()` method
    map_data = json.load(f)
    
#print(WELCOME)




default_room_id = 0
print(default_room_id)
print(map_data[default_room_id])
if map_data[default_room_id]:
    GS.curr_room = map_data[default_room_id]
    GS.personal_item = []
else:
    print("Wrong map data!")

print_room(GS.curr_room)
#go()
# while(1):
#     move = input("What would you like to do?")
#     if move in verb_dict.values:
#         verb_dict[move]


