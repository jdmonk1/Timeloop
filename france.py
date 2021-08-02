from NPCCreator import NPCCreator
from itemCreator import itemCreator
from ContainerCreator import ContainerCreator
from room import room
from NPC import NPC
from computer import computer


class france:

    def __init__(self, key):
        self.name = "france"
        self.roomList = []
        self.timeCost = 0
        self.ticket = key
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
        containerItemList = []
        containerList = []
        computerList = []
        comp = computer("comp1")
        IC = itemCreator()
        NPCC = NPCCreator()
        CC = ContainerCreator()
        containerItemList.append(IC.letter(name="letter", description="Info"))
        containerItemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        containerItemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        containerList.append(CC.suitcase(name="suitcase", itemList=containerItemList, key=0, description="My old leather suitcase. The lock's been busted for years."))
        NPCList.append(NPCC.James("James"))
        NPCList.append(NPCC.jonathan("Jonathan"))
        NPCList.append(NPCC.Gideon("Gideon"))
        NPCList.append(NPCC.roach(name1="cockroach"))
        computerList.append(comp)
        # itemList.append(IC.key(name="key1", description="An old rusty key. Who knows what it unlocks..."))
        # itemList.append(IC.key(name="kesy2", description="An old rusty key. Who knows what it unlocks..."))
        containerItemList = itemList
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        # containerList.append(CC.safe(name="safe2", itemList=containerItemList, key=2, description="A safe with a keyhole"))
        return room("hotel room", itemList, containerList, NPCList, [], computerList)
    
    def setupPantry(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        containerItemList = []
        containerItemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        CC = ContainerCreator()
        containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        itemList.append(IC.key(name="key", description="An old rusty key. Who knows what it unlocks..."))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        return room("pantry", itemList, containerList, NPCList, [], [])

    def setupHallway(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCC = NPCCreator()
        NPCList.append(NPCC.jonathan("person3"))
        NPCList.append(NPCC.jonathan("person4"))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        # itemList.append(IC.key(name="thing2"))
        return room("Hallway", itemList, [], NPCList, [], [])

    def setuproom1(self):
        NPCList = []
        itemList = []
        IC = itemCreator()
        NPCC = NPCCreator()
        NPCList.append(NPCC.jonathan("person5"))
        NPCList.append(NPCC.jonathan("person6"))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        itemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        return room("Room1", itemList, [], NPCList, [], [])


    