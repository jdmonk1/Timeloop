from itemCreator import itemCreator
from room import room
from NPC import NPC


class france:

    def __init__(self):
        self.name = "france"
        self.roomList = []
        self.timeCost = 0
        self.initRoom = self.setupHotelRoom()

    def setupLocation(self):
        hallway = self.setupHallway()
        hotel = self.initRoom
        room1 = self.setuproom1()
        pantry = self.setupPantry()
        hallway.adjacencyList.append(room1.description)
        hallway.adjacencyList.append(hotel.description)
        hotel.adjacencyList.append(hallway.description)
        hotel.adjacencyList.append(pantry.description)
        room1.adjacencyList.append(hallway.description)
        pantry.adjacencyList.append(hotel.description)
        self.roomList.append(hallway)
        self.roomList.append(hotel)
        self.roomList.append(room1)
        self.roomList.append(pantry)


    def setupHotelRoom(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person1"))
        NPCList.append(NPC("person2"))
        itemList.append(IC.key(name="key1", description="An old rusty key. Who knows what it unlocks..."))
        itemList.append(IC.key(name="key2", description="An old rusty key. Who knows what it unlocks..."))
        return room("Hotel", itemList, NPCList, [])
    
    def setupPantry(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        return room("Pantry", itemList, NPCList, [])

    def setupHallway(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person3"))
        NPCList.append(NPC("person4"))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        # itemList.append(IC.key(name="thing2"))
        return room("Hallway", itemList, NPCList, [])

    def setuproom1(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person5"))
        NPCList.append(NPC("person6"))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        return room("Room1", itemList, NPCList, [])


    