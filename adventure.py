from game_state import GS
from resources import map_data,person_data
from description import *
from desc_print import *
from verb import *

winning = 1
steps = 100
default_room_id = 1
GS.curr_room_id = default_room_id
person_items = []

try:
    map_data[GS.curr_room_id]
except:
    print("No vaild room here, please check the map data")
    exit()
print_room(map_data[GS.curr_room_id])
while steps and winning:
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
            move = move.split(' ', 1)
            if len(move) == 1 and move[0] in verb_dict_1:
                verb_dict_1[move[0]]() # this's like look()
            elif len(move) == 2 and move[0] in verb_dict_2:
                if move[0] in verb_dict_2:
                    verb_dict_2[move[0]](move[1]) # this's like go('east')
            else:
                print("Plase enter a right verb, You can enter help to get some hint.")
    if "corwn" in person_data:
        winning = 0
        break
    steps -= 1
    print(f"you have {steps} steps left!")

if winning == 0:
    print("You are win!")
if steps == 0:
    print("Game over, you are out of steps!")