from NPCCreator import NPCCreator
from itemCreator import itemCreator
from ContainerCreator import ContainerCreator
from room import room
from NPC import NPC
from computer import computer


class moroco:

    def __init__(self, key):
        self.name = "Moroco"
        self.roomList = []
        self.timeCost = 0
        self.ticket = key
        self.initRoom = self.setupAirport()

    def setupLocation(self):
        airport = self.initRoom
        streets = self.setupStreets()
        hut1 = self.setupHut1()
        hut2 = self.setupHut2()
        market = self.setupMarket()
        booth1 = self.setupBooth1()
        booth2 = self.setupBooth2()
        booth3 = self.setupBooth3()
        governmentBuilding = self.setupGovernmentBuilding()
        lobby = self.setupLobby()
        caves = self.setupCaves()
        fields = self.setupFields()

        airport.adjacencyList.append(streets.description)
        streets.adjacencyList.append(airport.description)
        streets.adjacencyList.append(hut1.description)
        streets.adjacencyList.append(hut2.description)
        streets.adjacencyList.append(market.description)
        streets.adjacencyList.append(governmentBuilding.description)
        streets.adjacencyList.append(lobby.description)
        streets.adjacencyList.append(caves.description)
        streets.adjacencyList.append(fields.description)

        hut1.adjacencyList.append(streets.description)
        hut2.adjacencyList.append(streets.description)
        governmentBuilding.adjacencyList.append(streets.description)
        lobby.adjacencyList.append(streets.description)
        caves.adjacencyList.append(streets.description)
        fields.adjacencyList.append(streets.description)
        market.adjacencyList.append(streets.description)
        market.adjacencyList.append(booth1.description)
        market.adjacencyList.append(booth2.description)
        market.adjacencyList.append(booth3.description)
        booth1.adjacencyList.append(market.description)
        booth2.adjacencyList.append(market.description)
        booth3.adjacencyList.append(market.description)

        self.roomList.append(airport)
        self.roomList.append(streets)
        self.roomList.append(market)
        self.roomList.append(booth1)
        self.roomList.append(booth2)
        self.roomList.append(booth3)
        self.roomList.append(governmentBuilding)
        self.roomList.append(lobby)
        self.roomList.append(caves)
        self.roomList.append(caves)
        self.roomList.append(fields)
        self.roomList.append(hut1)
        self.roomList.append(hut2)


    def setupAirport(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        computerList.append(computer(name="kiosk"))
        return room("airport", itemList, containersList, NPCList, [], computerList)

    def setupStreets(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("streets", itemList, containersList, NPCList, [], computerList)

    def setupHut1(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("hut1", itemList, containersList, NPCList, [], computerList)

    def setupHut2(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("hut2", itemList, containersList, NPCList, [], computerList)

    def setupMarket(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("market", itemList, containersList, NPCList, [], computerList)

    def setupBooth1(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("booth1", itemList, containersList, NPCList, [], computerList)

    def setupBooth2(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        itemList.append(itemCreator().hammerHead(name="rock", description="just a rock"))
        return room("booth2", itemList, containersList, NPCList, [], computerList)

    def setupBooth3(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("booth3", itemList, containersList, NPCList, [], computerList)

    def setupGovernmentBuilding(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("government_building", itemList, containersList, NPCList, [], computerList)

    def setupLobby(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("lobby", itemList, containersList, NPCList, [], computerList)
    
    def setupCaves(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        return room("caves", itemList, containersList, NPCList, [], computerList)
    
    def setupFields(self):
        itemList = []
        containersList = []
        NPCList = []
        computerList = []
        itemList.append(itemCreator().stick(name="stick", description="a stick"))
        return room("fields", itemList, containersList, NPCList, [], computerList)

    