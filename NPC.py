from dialogueGraph import dialogueGraph

class NPC:

    def __init__(self, name, animal=None):
        self.dialogueGraph = dialogueGraph(name)
        self.name = name
        self.animal = animal
    
    def chooseOption(self, choice):
        self.dialogueGraph.traverseNode(choice)

    def getName(self):
        return self.name

    def getChoices(self):
        counter = 1
        for i in self.dialogueGraph.currentNode.children:
            print(str(counter) + ") " + i.name)
            counter = counter + 1

    def reset1(self):
        self.dialogueGraph.currentNode = self.dialogueGraph.root