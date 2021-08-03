from container import container
from NPCCreator import NPCCreator
from itemCreator import itemCreator
from ContainerCreator import ContainerCreator
from room import room
from NPC import NPC
from computer import computer

class London:

    def __init__(self, key):
        self.name = "London"
        self.roomList = []
        self.timeCost = 0
        self.ticket = key
        self.initRoom = self.setupAirport()

    def setupLocation(self):
        airport = self.initRoom
        subwayStation = self.setupSubwayStation()
        governmentBuilding = self.setupGovernmentBuilding()
        printerRoom = self.setupPrinterRoom()
        lobby = self.setupLobby()
        coffeeShop = self.setupCoffeeShop()
        castle = self.setupCastle()
        busStation = self.setupBusStation()
        stonehenge = self.setupStonehenge()
        
        airport.adjacencyList.append(subwayStation.description)
        subwayStation.adjacencyList.append(airport.description)
        subwayStation.adjacencyList.append(governmentBuilding.description)
        subwayStation.adjacencyList.append(coffeeShop.description)
        subwayStation.adjacencyList.append(castle.description)
        subwayStation.adjacencyList.append(busStation.description)
        governmentBuilding.adjacencyList.append(printerRoom.description)
        governmentBuilding.adjacencyList.append(lobby.description)
        printerRoom.adjacencyList.append(governmentBuilding.description)
        lobby.adjacencyList.append(governmentBuilding.description)
        coffeeShop.adjacencyList.append(subwayStation.description)
        castle.adjacencyList.append(subwayStation.description)
        busStation.adjacencyList.append(subwayStation.description)
        busStation.adjacencyList.append(stonehenge.description)
        stonehenge.adjacencyList.append(busStation.description)

        self.roomList.append(airport)
        self.roomList.append(subwayStation)
        self.roomList.append(governmentBuilding)
        self.roomList.append(printerRoom)
        self.roomList.append(lobby)
        self.roomList.append(coffeeShop)
        self.roomList.append(castle)
        self.roomList.append(busStation)
        self.roomList.append(stonehenge)

    def setupAirport(self):
        itemList = []
        itemList.append(itemCreator().usb(name="usb", description="a usb"))
        computerList = []
        computerList.append(computer(name="kiosk"))
        return room("airport", [], [], [], [], computerList)

    def setupSubwayStation(self):
        return room("subway_station", [], [], [], [], [])

    def setupGovernmentBuilding(self):
        return room("government_building", [], [], [], [], [])
    
    def setupPrinterRoom(self):
        return room("printer_room", [], [], [], [], [])

    def setupLobby(self):
        computerList = []
        return room("airport", [], [], [], [], computerList)

    def setupCoffeeShop(self):
        return room("coffee_shop", [], [], [], [], [])

    def setupCastle(self):
        return room("castle", [], [], [], [], [])

    def setupBusStation(self):
        itemList = []
        itemList.append(itemCreator().phone(name="cellphone", description="The phone is dead."))
        return room("bus_station", itemList, [], [], [], [])

    def setupStonehenge(self):
        return room("stonehenge", [], [], [], [], [])