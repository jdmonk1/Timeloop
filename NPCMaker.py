class NPCMaker:

    def __init__(self):
        self.varList = []
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
        self.silentchildrenList = []
        self.silentresList = []
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
        self.varList.append(self.var + str(self.num) + str(self.wide))
        self.varList.append(text)
        return self.var + str(self.num) + str(self.wide) + " = " + self.name + ".dialogueGraph.createNode(\"" + text + "\")"

    def createRes(self,res):
        self.num = self.num + 1
        self.wide += 1
        self.resList.append(self.var + str(self.num) + str(self.wide) + "res")
        self.varList.append(self.var + str(self.num) + str(self.wide) + "res")
        self.varList.append(res)
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

    def custom(self, param, param2):
        self.silentchildrenList.append(param)
        self.silentresList.append(param2)

    def getNode(self):
        intro = []
        res = []
        while True:
            comfirst = "p"
            while comfirst == "p":
                comfirst = input("enter choice")
                if comfirst == "p":
                    self.printOutVarList()
            if comfirst == "c":
                thing = input("enter loop var")
                # self.custom(thing)
                thing2 = input("enter res var")
                self.custom(thing,thing2)
                break
            else:
                intro.append(comfirst)
                comfirst = input("enter response")
                res.append(comfirst)
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

    # def createLoop(self,childrenList,resList, ii):
    #     self.num += 1
    #     self.wide += 1
    #     children = ""
    #     res = ""
    #     for i in childrenList:
    #         children += i + ","
    #     children = children[:-1]
    #     for i in resList:
    #         res += i + ","
    #     res = res[:-1]
    #     return ii + ".children = [" + children + "]\n" + ii + ".res = [" + res + "]\n" + self.name + ".dialogueGraph.addNode(" + ii + ")"

    def create(self,childrenList, resList, ii):
        self.num += 1
        self.wide += 1
        children = ""
        res = ""
        for i in childrenList:
            children += i + ","
        children = children[:-1]
        for i in self.silentchildrenList:
            if len(childrenList) == 0:
                children += i
            else:
                children += "," + i
        self.silentchildrenList = []
        for i in resList:
            res += i + ","
        res = res[:-1]
        for i in self.silentresList:
            if len(resList) == 0:
                res += i
            else:
                res += "," + i
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
        # self.nextnextchildrenList = []
        # self.nextnextresList = []
        counter = -1
        for j in self.nextchildrenList:
            counter2 += 1
            counter = -1
            for i in j:
                counter += 1
                com = input("children for " + i + "?")
                if com == "n":
                    print("...skipping " + i + "...")
                    #continue
                if com != "n":
                    self.outputNode(i)
                    self.create(j, self.nextresList[counter2][counter], i)
                    self.nextnextchildrenList.append(self.childrenList)
                    self.nextnextresList.append(self.resList)
                    self.childrenList = []
                    self.resList = []
        self.nextchildrenList = self.nextnextchildrenList
        self.nextresList = self.nextnextresList
        self.nextnextchildrenList = []
        self.nextnextresList = []

    def program(self):
        self.setup()
        while True:
            self.run()
            print("nnchildrenList = ", self.nextnextchildrenList)
            print("nchildrenList = ", self.nextchildrenList)
            print("childrenList = ", self.childrenList)
            com = input("continue to another Level or done?")
            if com == "n":
                break
            # if com == "c":
            #     self.nextnextchildrenList = []
            #     self.nextnextresList = []

    def printOutput(self):
        for i in self.output:
            print(i)

    def printOutVarList(self):
        if len(self.varList) > 1:
            for i in range(0,len(self.varList),4):
                print(self.varList[i], self.varList[i+1], self.varList[i+2], self.varList[i+3])

def makeNPC():
    runner = NPCMaker()
    runner.program()
    runner.printOutput()

if __name__ == "__main__":
    makeNPC()        
    
