# Save the Stray

This is the first project for CS515 Spring 2023
Bulid @Siyan Liu

## How to play
You can invoke this game by running:
python3 adventure.py [map filename] //default map filename is default_map

## The flies strctures are like below:
Map:
    Properties:
        name: "name"
        desc: "desc"
        exits: {"Yestorday" : 0, "Tormoorow": 1} # The exits should be another object, mapping exit names to room ids.
        items: ["rose"] # items is a list of strings,
    Functions:
        update_dese
        load_map
        update_map(?)
Player:

Actions:
Verb:

Verb_Help:
Locked_doors:
