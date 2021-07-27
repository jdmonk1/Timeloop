from dialogueGraph import dialogueGraph

class NPC:

    def __init__(self, name):
        self.dialogueGraph = dialogueGraph(name)
        self.name = name
    
    def chooseOption(self, choice):
        self.dialogueGraph.traverseNode(choice)

    def getName(self):
        return self.name

    def getChoices(self):
        for i in self.dialogueGraph.currentNode.children:
            print(i.name)

    def reset1(self):
        self.dialogueGraph.currentNode = self.dialogueGraph.root