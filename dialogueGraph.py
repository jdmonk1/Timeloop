from node import node

class dialogueGraph:

    def __init__(self, nodeName):
        self.root = node(nodeName)
        self.currentNode = self.root
        self.nodeList = []

    def createNode(self, name):
        return node(name)
    
    def addNode(self, node):
        self.nodeList.append(node)
    
    def deleteNode(self, node):
        self.nodeList.remove(node)

    def traverseNode(self, node1):
        # print(self.currentNode.response(self.findNode(node1)))
        print(self.currentNode.res[node1-1])
        for i in self.currentNode.decision:
            i()
        self.currentNode = self.currentNode.children[node1-1]
        #print("current node = ", self.currentNode.name)

    def findNode(self, node):
        for i in self.nodeList:
            if node == i.name:
                return i

