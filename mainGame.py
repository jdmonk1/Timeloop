from france import france
from moroco import moroco
from player import player
#from test import test
import threading
from time import *
from room import room
import sys
from colors import colors
from os import system, name
import random

class Game:

    def __init__(self):
        #self.test = test()
        self.key = 0
        self.key2 = 3
        self.key3 = 7
        self.listofKeys = []
        self.Moroco = moroco(self.createLocationKey())
        self.Moroco.setupLocation()
        self.France = france(self.createLocationKey())
        self.France.setupLocation()
        self.locationList = []
        self.locationList.append(self.France)
        self.locationList.append(self.Moroco)
        self.Player = player(self.France.initRoom, self.France)
        self.my_timer = 5000000
        self.countdown_thread = threading.Thread(target=self.timer)
        self.quit = False

    def begin(self):
        system('cls')
        self.countdown_thread.start()
        self.command()

    def setSeed():
        num = random.randint(0,1000)
        random.seed(num)

    def createLocationKey(self):
        while True:
            num = random.randint(0,9)
            self.key += num
            self.key2 += num
            self.key3 += num
            key = (self.key * 10000) + (self.key2 * 100) + self.key3
            if key not in self.listofKeys:
                self.listofKeys.append((self.key * 10000) + (self.key2 * 100) + self.key3)
                return key

    def timer(self):
        hungerTicker = 0
        thirstTicker = 0
        for x in range(5000000):
            self.my_timer -= 1
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            sleep(.1)
            if self.quit:
                break
            hungerTicker += 1
            thirstTicker += 1
            if hungerTicker >= 10:
                self.Player.hungerTick()
                hungerTicker = 0
            if thirstTicker >= 10:
                self.Player.thirstTick()
                thirstTicker = 0
        if not self.quit:
            print("\n24 hours have passed. You wake up back in your bed in France.\nPress Enter to continue")
            self.my_timer = 5
            self.timer()

    def command(self):
        while not self.quit:
            cmd = ""
            if self.Player.dead:
                while not self.quit:
                    cmd = input(colors.BLUE + "Type \"quit\" to exit the game: " + colors.BLACK)
                    if cmd == "quit":
                        self.quit = True
                        break
            else:
                #inthing = colors.BLUE + "<TimeLoop>" + colors.BLACK
                #cmd = self.test.in1(inthing)
                cmd = input(colors.BLUE + "<TimeLoop>" + colors.BLACK)
                # print(colors.BLUE + "", end="")
                cmd = cmd.split(" ")
                if cmd[0] == "pickup" and len(cmd) == 2:
                    print(self.Player.pickup(cmd[1]))
                elif cmd == ["status"]:
                    print(self.Player.status())
                elif (cmd[0] == "view" or cmd[0] == "v") and len(cmd) == 2:
                    print(self.Player.view(cmd[1]))
                elif cmd == ["view"] or cmd == ["v"]:
                    self.Player.viewRoom()
                elif (cmd[0] == "use" and cmd[1] == "computer") and len(cmd) == 3:
                    result1 = self.Player.useComputer(self.Player, self.locationList, cmd[2])
                    if result1 != None:
                        pass
                    else:
                        print("computer not in the room")
                elif cmd[0] == "use" and len(cmd) == 3:
                    print(self.Player.use(cmd[1], cmd[2]))
                elif cmd[0] == "use" and len(cmd) == 2:
                    print(self.Player.use(self.Player.playerKey, cmd[1]))
                elif cmd[0] == "combine" and len(cmd) == 3:
                    print(self.Player.combine())
                elif (cmd[0] == "move" or cmd[0] == "m") and len(cmd) == 2:
                    self.Player.move(cmd[1])
                elif cmd[0] == "eat" and len(cmd) == 2:
                    print(self.Player.eat(cmd[1]))
                elif cmd[0] == "drink" and len(cmd) == 2:
                    print(self.Player.drink(cmd[1]))
                elif cmd[0] == "discard" and len(cmd) == 2:
                    self.Player.discard(cmd[1])
                elif cmd[0] == "backpack" or cmd[0] == "bp" and len(cmd) == 1:
                    self.Player.viewBackpack()
                elif cmd == ["room"]:
                    print(self.Player.currentRoom.description)
                elif cmd == ["rooms"]:
                    self.Player.printAdjacentRoomList()
                elif (cmd[0] == "talkto" or cmd[0] == "t") and len(cmd) == 2:
                    self.Player.talk(cmd[1])
                elif cmd[0] == "quit":
                    self.quit = True
                elif cmd[0] == "help" and len(cmd) == 2:
                    self.Player.help(cmd[1])
                elif cmd == ["test"]:
                    self.test.in1("")
                elif cmd == ["?"]:
                    self.Player.commands()
                else:
                    print("unknown command")
        print(colors.BLUE + "Game is terminated" + colors.BLACK)
        self.countdown_thread.join()

