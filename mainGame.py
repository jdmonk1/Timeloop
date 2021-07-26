from france import france
from player import player
from room import room

quit = True
France = france()
France.setupLocation()
Player = player(France.initRoom, France)

def test():
    test

def command():
    command = input("<TimeLoop>")
    if command == "pickup":
        itemin = input("enter item")
        print(Player.Pickup(itemin))
    elif command == "view":
        print(Player.View())
    elif command == "use":
        print(Player.Use())
    elif command == "combine":
        print(Player.Combine())
    elif command == "move":
        roomin = input("enter room")
        Player.move(roomin)
    elif command == "eat":
        print(Player.Eat())
    elif command == "drink":
        print(Player.Drink())
    elif command == "discard":
        print(Player.Discard())
    elif command == "backpack":
        Player.viewBackpack()
    elif command == "room":
        print(Player.currentRoom.description)
    elif command == "rooms":
        Player.printAdjacentRoomList()
    elif command == "quit":
        quit = False
    elif command == "test":
        test()
    else:
        print("unknown command")

while(quit):
    command()
