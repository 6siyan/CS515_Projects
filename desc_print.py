def print_room(room):
    print(room["name"])
    print()
    print(room["desc"])
    print()
    print(room["exits"])
    print()
    if room["items"]:
        print(room["items"])
        print()
