def print_room(room):
    print("> " + room["name"])
    if "locked" in room and room["locked"] == "Yes":
        print("Locked")
    print()
    print(room["desc"])
    print()
    if "items" in room and room["items"]:
        print("{} {}".format("Items:" , ",".join(map(str, room["items"]))))
        print()
    print("{} {}".format("Exits:" , ", ".join(map(str, list(room["exits"].keys())))))
    print()


