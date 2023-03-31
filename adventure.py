from game_state import GS
from resources import map_data,person_data
from description import *
from desc_print import *
from verb import *


default_room_id = 0
GS.curr_room_id = default_room_id
person_items = []

while True:
    print_room(map_data[GS.curr_room_id])
    try:
        move = input("What would you like to do?")
    except EOFError:
        print()
        print("Use 'quit' to exit.")
        continue
    
    if move.lower() == "quit":
        print("Exiting game...")
        exit()
    else:
            move = move.split(' ')
            if len(move) == 1 and move[0] in verb_dict:
                verb_dict[move[0]]() # this's like look()
            elif len(move) == 2 and move[0] in verb_dict:
                if move[0] in verb_dict:
                    verb_dict[move[0]](move[1]) # this's like go('east')
            else:
                print("Plase enter a right verb, You can enter help to get some hint.")
