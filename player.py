from colors import colors
import sys
class player:

    def __init__(self, initRoom, initLocationName):
        self.hunger = 100
        self.thirst = 100
        self.health = 100
        self.backpack = []
        self.currentRoom = initRoom
        self.currentLocationName = initLocationName
        self.dead = False

    def status(self):
        ret = ""
        if self.health > 50:
            ret += colors.GREEN + "health:" + str(self.health) + "\n" + colors.BLACK
        elif self.health <= 50 and self.health > 30:
            ret += colors.YELLOW + "health:" + str(self.health) + "\n" + colors.BLACK
        else:
            ret += colors.RED + "health:" + str(self.health) + "\n" + colors.BLACK
        if self.hunger > 50:
            ret += colors.GREEN + "hunger:" + str(self.hunger) + "\n" + colors.BLACK
        elif self.hunger <= 50 and self.hunger > 30:
            ret += colors.YELLOW + "hunger:" + str(self.hunger) + "\n" + colors.BLACK
        else:
            ret += colors.RED + "hunger:" + str(self.hunger) + "\n" + colors.BLACK
        if self.thirst > 50:
            ret += colors.GREEN + "thirst:" + str(self.thirst) + colors.BLACK
        elif self.thirst <= 50 and self.thirst > 30:
            ret += colors.YELLOW + "thirst:" + str(self.thirst) + colors.BLACK
        else:
            ret += colors.RED + "thirst:" + str(self.thirst) + colors.BLACK
        return ret
    
    def commands(self):
        print("List of possible commands:",
        "\npickup\nstatus\nview\nuse\ncombine\nmove\neat\ndrink\ndiscard\nbackpack\nroom\nrooms\ntalkto\nquit\n?",
        "\nType help <command> to find out what that command does and how to use it.")

    def help(self, cmd):
        if cmd == "pickup":
            print("----------\nuse to pick up an item in the room\nformat: pickup <item>\n----------")
        if cmd == "status":
            print("----------\ndisplays your current health stats\nformat: status\n----------")
        if cmd == "view":
            print("----------\nuse to view an item's description or see what items are in a room\nview an item's description:\n  format: view/v <item>\nview a room:\n  format: view/v\n----------")

    def move(self, room):
        for i in self.currentRoom.adjacencyList:
            if i == room:
                for j in self.currentLocationName.roomList:
                    if j.description == room:
                        self.currentRoom = j
                        print("moved to", j.description)

    def pickup(self, item):
        for j in self.currentRoom.itemsList:
            if j.name == item:
                self.backpack.append(j)
                self.currentRoom.itemsList.remove(j)
                return colors.GREEN + "Added " + j.name + " to backpack!" + colors.BLACK
        for i in self.currentRoom.containersList:
            if i.isOpen:
                for j in i.itemList:
                    if j.name == item:
                        self.backpack.append(j)
                        i.itemList.remove(j)
                        return colors.GREEN + "Added " + j.name + " to backpack!" + colors.BLACK
        return colors.RED + "item not in room" + colors.BLACK
                
    def viewItem(self, item):
        for i in self.currentRoom.itemsList:
            if i.name == item:
                return i.description

    def viewRoom(self):
        for i in self.currentRoom.itemsList:
            print(i.name)
        for i in self.currentRoom.containersList:
            if i.isOpen == 0:
                print(colors.RED + i.name + colors.BLACK)
            else:
                print(colors.GREEN + i.name + colors.BLACK)
                for j in i.itemList:
                    print(colors.GREEN + "  " + j.name + colors.BLACK)

    def use(self, key, container):
        combineKey = self.contains(key, self.backpack)
        if combineKey != -1:
            for i in self.currentRoom.containersList:
                if i.name == container:
                    return (i.open(combineKey))
    
    def useComputer(self, computer):
        while True:
            pass
    
    def contains(self, element, lst):
        for i in lst:
            if element == i.name:
                return i.combineKey
        return -1

    def combine(self):
        pass    
    
    def eat(self, item):
        if self.backpack != []:
            for i in self.backpack:
                if item == i.name:
                    self.hunger = self.hunger + i.nutrition
                    self.backpack.remove(i)
                    if self.hunger > 100:
                        self.hunger = 100
                    return "You have eaten " + i.name + ". It gave you " + str(i.nutrition) + " hunger back."
        

    def drink(self, item):
        if self.backpack != []:
            for i in self.backpack:
                if item == i.name:
                    self.thirst = self.thirst + i.nutrition
                    self.backpack.remove(i)
                    if self.thirst > 100:
                        self.thirst = 100
                    return "You have drunk " + i.name + ". It gave you " + str(i.nutrition) + " thirst back."

    def talk(self, name):
        for i in self.currentRoom.NPCList:
            if i.name == name:
                while True:
                    print("--Choices--")
                    i.getChoices()
                    print("----------")
                    com = input("<response to " + name + ">")
                    # for ele in i.dialogueGraph.nodeList:
                        #print(com, ele.name)
                    # if ele.name == com:
                        #print("got here")
                    com = int(com)
                    if com == 0:
                        i.reset1()
                        break
                    print("--Person1--")
                    i.chooseOption(com)
                    print("-----------")


    def discard(self):
        pass

    def fail(self):
        pass

    def viewBackpack(self):
        print("You have " + str(len(self.backpack)) + " items in your backpack:\n---")
        for i in self.backpack:
            print(i.name)
        print("---")

    def printAdjacentRoomList(self):
        for i in self.currentRoom.adjacencyList:
            print(i)
    
    def hungerTick(self):
        self.hunger = self.hunger - 1
        if self.hunger == 30:
            print(colors.RED + "\nDanger!! You are getting hungry!" + colors.BLACK)
        if self.hunger == 20:
            print(colors.RED + "\nDanger!! You are very hungry!" + colors.BLACK)
        if self.hunger == 10:
            print(colors.RED + "\nDANGER!!! YOU ARE CRITICALLY HUNGRY!! YOU MUST EAT!!" + colors.BLACK)
        if self.hunger == 0:
            print(colors.RED + "\nYou are dead." + colors.BLACK)
            self.health = 0
            self.dead = True

    def thirstTick(self):
        self.thirst = self.thirst - 1
        if self.thirst == 30:
            print(colors.RED + "\nDanger!! You are getting thirsty!" + colors.BLACK)
        if self.thirst == 20:
            print(colors.RED + "\nDanger!! You are very thirsty!" + colors.BLACK)
        if self.thirst == 10:
            print(colors.RED + "\nDANGER!!! YOU ARE CRITICALLY thirsty!! YOU MUST FIND WATER!" + colors.BLACK)
        if self.thirst == 0:
            print(colors.RED + "\nYou are dead." + colors.BLACK)
            self.health = 0
            self.dead = True
        
