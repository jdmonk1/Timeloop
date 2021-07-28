class NPCMaker:

    def __init__(self):
        self.output = []
        self.childrenList = []
        self.resList = []
        self.nextchildrenList = []
        self.nextresList = []
        self.nextnextchildrenList = []
        self.nextnextresList = []
        self.prevchildrenList = []
        self.prevresList = []
        self.prevprevchildrenList = []
        self.prevprevresList = []
        self.name = ""
        self.var = "a"
        self.num = -1
        self.wide = -1

    def createIntro(self):
        return self.name + " = NPC(name1)"

    def createNode(self, text):
        self.num = self.num + 1
        self.wide += 1
        self.childrenList.append(self.var + str(self.num) + str(self.wide))
        return self.var + str(self.num) + str(self.wide) + " = " + self.name + ".dialogueGraph.createNode(\"" + text + "\")"

    def createRes(self,res):
        self.num = self.num + 1
        self.wide += 1
        self.resList.append(self.var + str(self.num) + str(self.wide) + "res")
        return self.var + str(self.num) + str(self.wide) + "res = " + "\"" + res + "\""

    def createRoot(self,childrenList, resList):
        children = ""
        res = ""
        for i in childrenList:
            children += i + ","
        children = children[:-1]
        for i in resList:
            res += i + ","
        res = res[:-1]
        return self.name + ".dialogueGraph.root.children = [" + children + "]\n" + self.name + ".dialogueGraph.root.res = [" + res + "]\n" + self.name + ".dialogueGraph.addNode(" + self.name + ".dialogueGraph.root)"

    def getNode(self):
        intro = []
        res = []
        while True:
            intro.append(input("enter choice"))
            res.append(input("enter response"))
            com = input("another choice?")
            if com == "n":
                break
        return (intro, res)

    def outputNodeRoot(self):
        self.name = input("enter NPC name")
        self.output.append(self.createIntro())
        output = self.getNode()
        for i in range(len(output[0])):
            self.output.append(self.createNode(output[0][i]))
            self.output.append(self.createRes(output[1][i]))
        self.output.append(self.createRoot(self.childrenList, self.resList))

    def outputNode(self, ii):
        self.childrenList = []
        self.resList = []
        output = self.getNode()
        for i in range(len(output[0])):
            self.output.append(self.createNode(output[0][i]))
            self.output.append(self.createRes(output[1][i]))
        self.output.append(self.create(self.childrenList, self.resList, ii))

    def createLoop(self,childrenList,resList, ii):
        self.num += 1
        self.wide += 1
        children = ""
        res = ""
        for i in childrenList:
            children += i + ","
        children = children[:-1]
        for i in resList:
            res += i + ","
        res = res[:-1]
        return ii + ".children = [" + children + "]\n" + ii + ".res = [" + res + "]\n" + self.name + ".dialogueGraph.addNode(" + ii + ")"

    def create(self,childrenList, resList, ii):
        self.num += 1
        self.wide += 1
        children = ""
        res = ""
        for i in childrenList:
            children += i + ","
        children = children[:-1]
        for i in resList:
            res += i + ","
        res = res[:-1]
        return ii + ".children = [" + children + "]\n" + ii + ".res = [" + res + "]\n" + self.name + ".dialogueGraph.addNode(" + ii + ")"

    def setup(self):
        self.outputNodeRoot()
        self.nextchildrenList.append(self.childrenList)
        self.nextresList.append(self.resList)
        self.childrenList = []
        self.resList = []

    def run(self):
        counter2 = -1
        counter = -1
        self.nextnextchildrenList = []
        self.nextnextresList = []
        counter = -1
        for j in self.nextchildrenList:
            counter2 += 1
            counter = -1
            for i in j:
                counter += 1
                com = input("children for " + i + "?")
                if com == "n":
                    print("...skipping " + i + "...")
                    continue
                self.nextnextchildrenList.append(self.childrenList)
                self.nextnextresList.append(self.resList)
                self.childrenList = []
                self.resList = []
                self.outputNode(i)
                self.create(j, self.nextresList[counter2][counter], i)
        self.nextchildrenList = self.nextnextchildrenList
        self.nextresList = self.nextnextresList

    def program(self):
        self.setup()
        while True:
            self.run()
            com = input("continue to another Level or done?")
            if com == "n":
                break

    def printOutput(self):
        for i in self.output:
            print(i)

def makeNPC():
    runner = NPCMaker()
    runner.program()
    runner.printOutput()

if __name__ == "__main__":
    makeNPC()        
    
