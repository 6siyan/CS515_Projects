def print_room(room):
    print("> " + room["name"])
    if room["locked"] == "Yes":
        print("Locked")
    print()
    print(room["desc"])
    print()
    print("Exits: ")
    print(room["exits"])
    print()
    if room["items"]:
        print("Items: ")
        print(room["items"])
        print()

