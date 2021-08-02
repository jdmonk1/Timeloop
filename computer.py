class computer:

    def __init__(self, name):
        self.listLocations = []
        self.name = name

    def bookAFlight(self, Player, flight, key):
        for i in self.listLocations:
            if flight == i.name and key == str(i.ticket):
                Player.currentLocationName = i
                Player.currentRoom = i.initRoom
                return Player

    def listLocationsOut(self):
        for i in self.listLocations:
            print(i.name)

    def updateCurrentLocations(self, locationList):
        self.listLocations = locationList
