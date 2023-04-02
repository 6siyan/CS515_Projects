# Adventture game engine

This is the first project for CS515 Spring 2023

Name: Siyan Liu 

Mail: sliu112@stevens.edu

GitHub repo: 

Project time: 10 hours

Test method: manual test. Try to build the Github Action service, but find not much thing to do in pytest.

Bugs: not find for now, if you find please submit a issue on GitHub.

Difficult issues: the diffcult thing is the system design part. The code itself is more easy than design.

Extensions:

    A drop verb: You can use "drop" to drop something from your inventory.

    Locked doors: There are locked rooms in the game. If you meet "This is locked, you need find a key first!". It means you should find the "key" item first. When you have a key in your inventory. You have access to a locked room.

    Wining and losing conditions: There is a "crown" in the game. if you find the crown you will win. The step limit is 200 steps, if you exceed 200 steps you will lose the game.

## How to play
You can invoke this game by running:

python3 adventure.py [map filename] 

### Basic movement:
You can use:

go or g to move to new room. like "go east".

look or l to get this room's information. like look

get or ge to get a item in the room. like "get rose".

drop or d to drop a personal item to the room. like "drop key"

inventory or i to check what item in your bag. like "inventory"


