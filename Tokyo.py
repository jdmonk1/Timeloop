from container import container
from NPCCreator import NPCCreator
from itemCreator import itemCreator
from ContainerCreator import ContainerCreator
from room import room
from NPC import NPC
from computer import computer

class Tokyo:

    def __init__(self, key):
        self.name = "Tokyo"
        self.roomList = []
        self.timeCost = 0
        self.ticket = key
        self.initRoom = self.setupHotelRoom()

    def setupLocation(self):
        pass