class player:

    def __init__(self, initRoom, initLocationName):
        self.hunger = 70
        self.thirst = 40
        self.health = 100
        self.backpack = []
        self.currentRoom = initRoom
        self.currentLocationName = initLocationName

    def status(self):
        return "health:" + str(self.health) + "\nhunger:" + str(self.hunger) + "\nthirst:" + str(self.thirst)

    def move(self, room):
        for i in self.currentRoom.adjacencyList:
            if i == room:
                for j in self.currentLocationName.roomList:
                    if j.description == room:
                        self.currentRoom = j
                        print("moved to ", j.description)

    def pickup(self, item):
        if self.backpack != []:
            for j in self.currentRoom.itemsList:
                if j.name == item:
                    self.backpack.append(j)
                    self.currentRoom.itemsList.remove(j)
                    return "Added " + j.name + " to backpack!"
            return "item not in room"
        else:
            for j in self.currentRoom.itemsList:
                if j.name == item:
                    self.backpack.append(j)
                    self.currentRoom.itemsList.remove(j)
                    return "Added " + j.name + " to backpack!"
            return "item not in room"
                
    def viewItem(self, item):
        for i in self.currentRoom.itemsList:
            if i.name == item:
                return i.description

    def viewRoom(self):
        for i in self.currentRoom.itemsList:
            print(i.name)

    def use(self):
        pass

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
            print("Danger!! You are getting hungry!")
        if self.hunger == 20:
            print("Danger!! You are very hungry!")
        if self.hunger == 10:
            print("DANGER!!! YOU ARE CRITICALLY HUNGRY!!")
        if self.hunger == 0:
            print("You are dead.")
            self.health = 0

    def thirstTick(self):
        self.thirst = self.thirst - 1
        if self.hunger == 30:
            print("Danger!! You are getting hungry!")
        if self.hunger == 20:
            print("Danger!! You are very hungry!")
        if self.hunger == 10:
            print("DANGER!!! YOU ARE CRITICALLY HUNGRY!!")
        if self.hunger == 0:
            print("You are dead.")
            self.health = 0
        
