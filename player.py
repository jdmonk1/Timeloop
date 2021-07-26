class player:

    def __init__(self, initRoom, initLocationName):
        self.hunger = 100
        self.thirst = 100
        self.health = 100
        self.backpack = []
        self.currentRoom = initRoom
        self.currentLocationName = initLocationName

    def move(self, room):
        for i in self.currentRoom.adjacencyList:
            if i == room:
                for j in self.currentLocationName.roomList:
                    if j.description == room:
                        self.currentRoom = j
                        print("moved to ", j.description)

    def Pickup(self, item):
        if self.backpack != []:
            for i in self.backpack:
                if item == i.name:
                    return "item already in backpack"
                else:
                    for j in self.currentRoom.itemsList:
                        if j.name == item:
                            self.backpack.append(j)
                            return "Added " + j.name + " to backpack!"
                    return "item not in room"
        else:
            for j in self.currentRoom.itemsList:
                if j.name == item:
                    self.backpack.append(j)
                    return "Added " + j.name + " to backpack!"
            return "item not in room"
                
    def View(self):
        pass

    def Use(self):
        pass

    def Combine(self):
        pass    
    
    def Eat(self, nutrition):
        self.hunger = self.hunger + nutrition

    def Drink(self):
        pass

    def Discard(self):
        pass

    def fail(self):
        pass

    def viewBackpack(self):
        print("---")
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
        
