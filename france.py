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
        for i in range(7):
            containerItemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        for i in range(7):
            containerItemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        containerItemList.append(IC.infoLetter(name="Letter",
                                     description="Hi self. This is kind of weird. Me sending a letter to myself in a timeloop. who would have known that it would have come to this." +
                                                " If you, I mean me in the timeloop, am getting this letter than well... you are in a timeloop and I failed in stoping the collective." +
                                                " Not to worry. Once I discovered that the collective were creating a time loop I wrote this letter to help me in the case that I cannot" + 
                                                " stop them. Please follow these intructions closely and follow them to the letter as it is very important. I tried to send you some items" + 
                                                " that I thought you, I mean I, would need. not sure exactly if they will be in the desired location or not. You might have to go looking" + 
                                                " for them as my understanding of temporal location might not be as good as I thought. You need to collect the 4 clues that I have hidden." +
                                                " I have placed them in the time loop carefully so that in the event I cannot stop the collective I can go and find them and stop the collective." +
                                                " Good luck... oh Yeah remember that time loops play with memory, and time (and who knows all else) and have the potential to cause the individuals" +
                                                " and rooms to 'reset' every 24 hours. Make sure to store items in the temporal zone to avoid temporal disasociation. You should start out in a temporal" +
                                                " Zone. Again I say good luck and may you be sucessful in collecting the clues and shutting down the timeloop in the lab.", combineKey=100))
        containerList.append(CC.suitCase(name="suitCase", itemList=containerItemList, key= -1, description="A random suitcase..."))
        # computerList.append(comp)
        # # itemList.append(IC.key(name="key1", description="An old rusty key. Who knows what it unlocks..."))
        # # itemList.append(IC.key(name="kesy2", description="An old rusty key. Who knows what it unlocks..."))
        # containerItemList = itemList
        # # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        # # containerList.append(CC.safe(name="safe2", itemList=containerItemList, key=2, description="A safe with a keyhole"))
        return room("Hotel", itemList, containerList, NPCList, [], computerList)
    
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


    