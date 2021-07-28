from france import france
from player import player
from room import room


France = france()
France.setupLocation()
Player = player(France.initRoom, France)

def test():
    test

def command():
    quit = True
    cmd = ""
    cmd = input("<TimeLoop>")
    cmd = cmd.split(" ")
    # print(cmd)
    if cmd[0] == "pickup" and len(cmd) == 2:
        print(Player.pickup(cmd[1]))
    elif cmd == ["status"]:
        print(Player.status())
    elif (cmd[0] == "view" or cmd[0] == "v") and len(cmd) == 2:
        print(Player.viewItem(cmd[1]))
    elif cmd == ["view"] or cmd == ["v"]:
        Player.viewRoom()
    elif cmd[0] == "use" and len(cmd) == 3:
        print(Player.use(cmd[1], cmd[2]))
    elif cmd[0] == "combine" and len(cmd) == 3:
        print(Player.combine())
    elif (cmd[0] == "move" or cmd[0] == "m") and len(cmd) == 2:
        Player.move(cmd[1])
    elif cmd[0] == "eat" and len(cmd) == 2:
        print(Player.eat(cmd[1]))
    elif cmd[0] == "drink" and len(cmd) == 2:
        print(Player.drink(cmd[1]))
    elif cmd[0] == "discard" and len(cmd) == 2:
        print(Player.discard())
    elif cmd[0] == "backpack" or cmd[0] == "bp" and len(cmd) == 1:
        Player.viewBackpack()
    elif cmd == ["room"]:
        print(Player.currentRoom.description)
    elif cmd == ["rooms"]:
        Player.printAdjacentRoomList()
    elif (cmd[0] == "talkto" or cmd[0] == "t") and len(cmd) == 2:
        Player.talk(cmd[1])
    elif cmd[0] == "quit":
        quit = False
    elif cmd[0] == "help" and len(cmd) == 2:
        Player.help(cmd[1])
    elif cmd == ["?"]:
        Player.commands()
    else:
        print("unknown command")
    
    if quit:
        command()

# while(quit):
#     command()
command()
