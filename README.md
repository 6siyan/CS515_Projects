# Adventure game

This is the first project for CS515 Spring 2023

Name: Siyan Liu 

Mail: sliu112@stevens.edu

GitHub repo: https://github.com/6siyan/CS515_Projects_1/

Project time: 15 hours

Test method: Try to build the Github Action service, but find not much thing to do in pytest. So I manually test it. 

Bugs: not find for now, if you find please submit a issue on GitHub.

Difficult issues: the diffcult thing is the system design part. The code itself is more easy than design.

Extensions:

### A drop verb: 

You can use "drop" to drop something from your inventory. like "drop rose".

### Locked doors: 
There are locked rooms in the game. If you meet "This is locked, you need find a key first!". It means you should find the "pswd" item first. When you have a "pswd" in your inventory. You have access to a locked room.

### Wining and losing conditions: 

There is a "cs 515 project code" item in the game. if you find the "cs 515 project code" you will win. The step limit is 200 steps, if you exceed 200 steps you will lose the game.

    Hint: the "pswd" in tuesday and the "cs 515 project code" in last sunday(AKA. the day before monday).

## How to play
You can invoke this game by running:

python3 adventure.py [map filename] 

### Basic movement:
You can use:

go or g to move to new room. like "go east".

look or l to get this room's information. like "look".

get or ge to get a item in the room. like "get rose".

drop or d to drop a personal item to the room. like "drop key"

inventory or i to check what item in your bag. like "inventory"


