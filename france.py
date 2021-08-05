from container import container
from NPCCreator import NPCCreator
from itemCreator import itemCreator
from ContainerCreator import ContainerCreator
from room import room
from NPC import NPC
from computer import computer


class france:

    def __init__(self, key):
        self.name = "France"
        self.roomList = []
        self.timeCost = 0
        self.ticket = key
        self.dougKey = 500
        self.initRoom = self.setupHotelRoom()

    def setupLocation(self):
        hallway = self.setupHallway()
        hotel = self.initRoom
        room1 = self.setuproom1()
        room2 = self.setuproom2()
        room3 = self.setuproom3()
        pantry = self.setupPantry()
        room4 = self.setuproom4()
        room5 = self.setuproom5()
        elevator = self.setupelevator()
        lobby = self.setupLobby()
        portico = self.setupProtico()
        taxi = self.setupTaxi()
        airport = self.setupAirport()

        hallway.adjacencyList.append(room1.description)
        hallway.adjacencyList.append(hotel.description)
        hallway.adjacencyList.append(room2.description)
        hotel.adjacencyList.append(hallway.description)
        hotel.adjacencyList.append(pantry.description)
        room1.adjacencyList.append(hallway.description)
        pantry.adjacencyList.append(hotel.description)
        room2.adjacencyList.append(hallway.description)
        hallway.adjacencyList.append(room3.description)
        room3.adjacencyList.append(hallway.description)
        hallway.adjacencyList.append(room5.description)
        room5.adjacencyList.append(hallway.description)
        hallway.adjacencyList.append(room4.description)
        room4.adjacencyList.append(hallway.description)
        elevator.adjacencyList.append(hallway.description)
        hallway.adjacencyList.append(elevator.description)
        elevator.adjacencyList.append(lobby.description)
        lobby.adjacencyList.append(elevator.description)
        lobby.adjacencyList.append(portico.description)
        portico.adjacencyList.append(lobby.description)
        portico.adjacencyList.append(taxi.description)
        airport.adjacencyList.append(taxi.description)
        taxi.adjacencyList.append(airport.description)
        taxi.adjacencyList.append(portico.description)
        hotel.adjacencyList.append(taxi.description)
        self.roomList.append(hallway)
        self.roomList.append(hotel)
        self.roomList.append(room1)
        self.roomList.append(pantry)
        self.roomList.append(room2)
        self.roomList.append(room3)
        self.roomList.append(room5)
        self.roomList.append(room4)
        self.roomList.append(elevator)
        self.roomList.append(lobby)
        self.roomList.append(portico)
        self.roomList.append(taxi)
        self.roomList.append(airport)

    def setupHotelRoom(self):
        NPCList = []
        itemList = []
        containerItemList = []
        containerList = []
        computerList = []
        comp = computer("laptop")
        IC = itemCreator()
        NPCC = NPCCreator()
        CC = ContainerCreator()
        itemList.append(IC.cash(name="$5", description="5 bucks"))
        itemList.append(IC.cash(name="$5", description="5 bucks"))
        itemList.append(IC.cash(name="$5", description="5 bucks"))
        itemList.append(IC.cash(name="$5", description="5 bucks"))
        itemList.append(IC.cash(name="$10", description="5 bucks"))
        itemList.append(IC.cash(name="$10", description="5 bucks"))
        itemList.append(IC.cash(name="$10", description="5 bucks"))

        for i in range(7):
            containerItemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
        for i in range(7):
            containerItemList.append(IC.waterBottle(name="water_bottle", description="A plastic bottle of water."))
        containerItemList.append(IC.infoLetter(name="Letter",
                                     description="Hi self,\n\n\tThis is kind of weird. Me sending a letter to myself in a timeloop. who would have known that it would have come to this." +
                                                " If you (or rather me in the timeloop) am getting this letter, then well... you (I) are (am) in a timeloop and I failed in stoping the collective." +
                                                " Not to worry. Once I discovered that the collective were creating a time loop I wrote this letter to help me in the case that I cannot" + 
                                                " stop them. Please follow these intructions closely and follow them to the letter as it is very important. I tried to send you some items" + 
                                                " that I thought you, I mean I, would need. not sure exactly if they will be in the desired location or not. You might have to go looking" + 
                                                " for them as my understanding of temporal location might not be as good as I thought. You need to collect the 4 clues that I have hidden." +
                                                " I have placed them in the time loop carefully so that in the event I cannot stop the collective I can go and find them and stop the collective." +
                                                " Good luck... oh Yeah remember that time loops play with memory, and time (and who knows all else) and have the potential to cause the individuals" +
                                                " and rooms to 'reset' every 24 hours. Make sure to store items in the temporal zone to avoid temporal disasociation. You should start out in a temporal" +
                                                " Zone. Again I say good luck and may you be sucessful in collecting the clues and shutting down the timeloop in the lab.\n\nAll the best,\nMe", combineKey=100))
        containerList.append(CC.suitCase(name="suitCase", itemList=containerItemList, key= -1, description="My old leather suitcase. I think I still remember the combination..."))
        return room("hotel_room", itemList, containerList, NPCList, [], computerList)
    
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
        NPCList.append(NPCC.Doug("Doug"))
        NPCList.append(NPCC.jonathan("person4"))
        itemList.append(IC.jerky(name="jerky", description="A piece of dried jerky."))
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
    
    def setuproom2(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        containerItemList.append(IC.jerky(name="jerky", description="A dried-up piece of jerky. Who know's how long it's been in the trash can... gross."))
        containerItemList.append(IC.infoLetter(name="letter", description="Lab Info"))
        containerItemList.append(IC.paperclip(name="paper_clip", description="An aluminum paperclip. It's bent out of shape and is probably useless."))
        containerItemList.append(IC.spoolOfThread(name="spool_of_thread", description="The thread looks completely unused, but it's pretty bad quality. It could be used to tie something in a pinch, but it wouldn't hold for long."))
        containerItemList.append(IC.cash(name="$10", description="10 bucks"))
        containerList.append(CC.trashCan(name="trash_can", itemList=containerItemList, key=0, description="A plastic trash bin... not much to write home about."))
        return room("Room2", itemList, containerList, [], [], [])

    def setuproom3(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        itemList.append(IC.cash(name="$5", description="5 bucks"))
        containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("room3", itemList, containerList, [], [], [])

    def setuproom4(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        itemList.append(IC.brush(name="brush", description="A simple, red hairbrush."))
        containerItemList.append(IC.cash(name="$5", description="5 bucks"))
        containerList.append(CC.trashCan(name="trash_can", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("room4", itemList, containerList, [], [], [])

    def setuproom5(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("room5", itemList, containerList, [], [], [])    

    def setupelevator(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("elevator", itemList, containerList, [], [], []) 

    def setupLobby(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("lobby", itemList, containerList, [], [], []) 
    
    def setupProtico(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("hotel_portico", itemList, containerList, [], [], []) 

    def setupTaxi(self):
        NPCList = []
        itemList = []
        containerList = []
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("taxi", itemList, containerList, [], [], []) 

    def setupAirport(self):
        NPCList = []
        itemList = []
        containerList = []
        computerList = []
        computerList.append(computer(name="Kiosk"))
        IC = itemCreator()
        CC = ContainerCreator()
        containerItemList = []
        # itemList.append(IC.cash(name="$5", description="5 bucks"))
        # containerItemList.append(IC.ticket(name="plane_ticket", description="A plane ticket"))
        # containerList.append(CC.safe(name="safe", itemList=containerItemList, key=1, description="A safe with a keyhole"))
        return room("airport", itemList, containerList, [], [], computerList) 
    