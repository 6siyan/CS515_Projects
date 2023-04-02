def print_room(room):
    print("> " + room["name"])
    if room["locked"] == "Yes":
        print("Locked")
    print()
    print(room["desc"])
    print()
    if room["items"]:
        #print("Items: " + str(room["items"])[1:-1])
        print("{} {}".format("Items:" , ", ".join(map(str, list(room["exits"].keys())))))

        #print(room["items"])
        print()
    print("{} {}".format("Exits:" , ",".join(map(str, room["items"]))))
    #print("Exits: " + str(list(room["exits"].keys()))[1:-1])
    print()


