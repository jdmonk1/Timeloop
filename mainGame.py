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
    query = input("<TimeLoop>")
    if query == "pickup":
        itemin = input("enter item")
        print(Player.Pickup(itemin))
    elif query == "view":
        print(Player.View())
    elif query == "use":
        print(Player.Use())
    elif query == "combine":
        print(Player.Combine())
    elif query == "move":
        roomin = input("enter room")
        Player.move(roomin)
    elif query == "eat":
        print(Player.Eat())
    elif query == "drink":
        print(Player.Drink())
    elif query == "discard":
        print(Player.Discard())
    elif query == "backpack":
        Player.viewBackpack()
    elif query == "room":
        print(Player.currentRoom.description)
    elif query == "rooms":
        Player.printAdjacentRoomList()
    elif query == "quit":
        quit = False
    elif query == "test":
        test()
    else:
        print("unknown command")
    
    if quit:
        command()

# while(quit):
#     command()
command()
