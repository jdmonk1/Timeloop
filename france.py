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
        halway = self.setupHallway()
        hotel = self.initRoom
        room1 = self.setuproom1()
        halway.adjacencyList.append(room1.description)
        halway.adjacencyList.append(hotel.description)
        hotel.adjacencyList.append(halway.description)
        room1.adjacencyList.append(halway.description)
        self.roomList.append(halway)
        self.roomList.append(hotel)
        self.roomList.append(room1)


    def setupHotelRoom(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person1"))
        NPCList.append(NPC("person2"))
        itemList.append(IC.key(name="TestKey"))
        itemList.append(IC.key(name="OtherTestKey"))
        return room("Hotel", itemList, NPCList, [])

    def setupHallway(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person3"))
        NPCList.append(NPC("person4"))
        itemList.append(IC.key(name="thing1"))
        itemList.append(IC.key(name="thing2"))
        return room("Halway", itemList, NPCList, [])

    def setuproom1(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCList.append(NPC("person5"))
        NPCList.append(NPC("person6"))
        itemList.append(IC.key(name="thing3"))
        itemList.append(IC.key(name="thing4"))
        return room("Room1", itemList, NPCList, [])


    