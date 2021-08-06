from itemCreator import itemCreator
from dialogueGraph import dialogueGraph
from colors import colors
from itemCreator import itemCreator
#import timerGlob

class NPC:

    def __init__(self, name, itemList, animal=None):
        self.dialogueGraph = dialogueGraph(name)
        self.name = name
        self.animal = animal
        self.itemList = itemList
        self.itemForPlayer = []
        self.cost = None
        self.backpack = None
        self.currentRoom = None
        self.IC = itemCreator()
    
    def findItem(self, name):
        for i in self.backpack:
            if i.name == name:
                return i

    def chooseOption(self, choice, backpack, currentRoom):
        self.backpack = backpack
        self.currentRoom = currentRoom
        self.dialogueGraph.traverseNode(choice)
        return self.backpack

    def getName(self):
        return self.name

    def getChoices(self):
        counter = 1
        for i in self.dialogueGraph.currentNode.children:
            print(str(counter) + ") " + i.name)
            counter = counter + 1

    def reset1(self):
        self.dialogueGraph.currentNode = self.dialogueGraph.root

    def retChoices(self):
        return self.dialogueGraph.currentNode.children

    def itemToPlayer(self, name, costtype, cost):
        if costtype == "cash":
            cash = 0
            fives = 0
            tens = 0
            for x in self.backpack:
                if x.name == "$5":
                    cash += 5
                    fives += 1
                if x.name == "$10":
                    cash += 10
                    tens += 1
            #print(cash)
            #print(tens)
            #print(fives)
            if cash >= cost:
                while cost >= 0:
                    if tens >= 1 and cost - 10 > 0:
                        self.backpack.remove(self.findItem("$10"))
                        tens -= 1
                        cost -= 10
                    elif tens >= 1 and cost - 5 > 0:
                        self.backpack.remove(self.findItem("$10"))
                        self.backpack.append(self.IC.cash(name="$5", description="5 bucks"))
                        tens -= 1
                        fives += 1
                        cost -= 5
                    elif tens == 0 and fives >= 1 and cost - 5 >= 0:
                        self.backpack.remove(self.findItem("$5"))
                        fives -= 1
                        cost -= 5
                    elif tens == 0 and fives == 0 and cost > 0:
                        print(colors.RED + "I don't have the right cash!" + colors.BLACK)
                    else:
                        for i in self.itemList:
                            if i.name == name:
                                #print("here")
                                self.itemList.remove(i)
                                #print("here2")
                                self.itemForPlayer.append(i)
                                #print("here3")
                        print("you gave " + str(cash) + " to " + self.name)
                        return
            else:
                print(colors.RED + "I don't have the right cash!" + colors.BLACK)
                return

        if costtype == "item":
            pass

    def itemFromPlayer(self, item):
        for i in item:
            self.itemList.append(i)
    