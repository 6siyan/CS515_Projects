from game_state import GS
from resources import map_data,person_data
from desc_print import *
from verb import *

# Game states are here.
winning = 1
steps = 20000
default_room_id = 0
GS.curr_room_id = default_room_id

try:
    map_data[GS.curr_room_id]
except:
    print("No vaild room here, please check the map data")
    exit()
print_room(map_data[GS.curr_room_id])
while steps and winning:
    try:
        move = input("What would you like to do? ")
    except EOFError:
        print()
        print("Use 'quit' to exit.")
        continue

    if move.lower() == "quit":
        print("Goodbye!")
        exit()
    else:
            move = move.lower().split(' ', 1)
            if len(move) == 1: 
                if move[0] in verb_dict_1:
                    verb_dict_1[move[0]]() # this's like look()
                elif move[0] in verb_dict_2:
                    verb_dict_2[move[0]]()
                else:
                    print("Plase enter a right verb.")
            elif len(move) == 2 and move[0] in verb_dict_2:
                if move[0] in verb_dict_2:
                    verb_dict_2[move[0]](move[1]) # this's like go('east')
                else:
                    print("Plase enter a right verb.")
            else:
                print("Plase enter a right verb.")

    if "corwn" in person_data:
        winning = 0
        break
    steps -= 1
    #print(f"you have {steps} steps left!")

if winning == 0:
    print("You are win!")
if steps == 0:
    print("Game over, you are out of steps!")