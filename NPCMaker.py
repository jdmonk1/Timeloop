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
        self.desList = []
        self.silentdesList = []
        self.nextdesList = []
        self.nextnextdesList = []
        self.des = []
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

    def createDes(self,des):
        self.num = self.num + 1
        self.wide += 1
        if des != "":
            self.desList.append(self.var + str(self.num) + str(self.wide) + "des")
            self.varList.append(self.var + str(self.num) + str(self.wide) + "des")
            self.varList.append(des)
            return self.var + str(self.num) + str(self.wide) + "des = " + des
        else:
            self.desList.append("")
            self.varList.append(self.var + str(self.num) + str(self.wide) + "des")
            self.varList.append(des)
            return ""

    def createRoot(self,childrenList, resList, desList):
        children = ""
        res = ""
        des = ""
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
        for i in desList:
            des += i + ","
        des = des[:-1]
        for i in self.silentdesList:
            if len(desList) == 0:
                des += i
            else:
                des += "," + i
        self.silentdesList = []
        return self.name + ".dialogueGraph.root.children = [" + children + "]\n" + self.name + ".dialogueGraph.root.res = [" + res + "]\n" + self.name + ".dialogueGraph.root.decision = [" + des + "]\n" + self.name + ".dialogueGraph.addNode(" + self.name + ".dialogueGraph.root)"

    def custom(self, param, param2, param3):
        self.silentchildrenList.append(param)
        self.silentresList.append(param2)
        self.silentdesList.append(param3)
        self.varList.append(param)
        self.varList.append(param2)
        self.varList.append(param3)

    def getNode(self):
        intro = []
        res = []
        des = []
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
                thing3 = input("enter des var or nothing")
                if thing3 == "":
                    thing4 = ""
                else:
                    thing4 = thing3
                self.custom(thing,thing2,thing4)
                break
            else:
                intro.append(comfirst)
                comfirst = input("enter response")
                res.append(comfirst)
                comfirst = input("enter decision or nothing")
                # if comfirst == "":
                #     thing4 = ""
                # else:
                #     thing4 = comfirst
                des.append(comfirst)
            com = input("another choice?")
            if com == "n":
                break
        return [intro, res, des]

    def outputNodeRoot(self):
        self.name = input("enter NPC name")
        self.output.append(self.createIntro())
        output = self.getNode()
        for i in range(len(output[0])):
            self.output.append(self.createNode(output[0][i]))
            self.output.append(self.createRes(output[1][i]))
            #print(output[2])
            self.output.append(self.createDes(output[2][i]))
        self.output.append(self.createRoot(self.childrenList, self.resList, self.desList))

    def outputNode(self, ii):
        self.childrenList = []
        self.resList = []
        output = self.getNode()
        for i in range(len(output[0])):
            self.output.append(self.createNode(output[0][i]))
            self.output.append(self.createRes(output[1][i]))
            self.output.append(self.createDes(output[2][i]))
        self.output.append(self.create(self.childrenList, self.resList, self.desList, ii))

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

    def create(self,childrenList, resList, desList, ii):
        self.num += 1
        self.wide += 1
        children = ""
        res = ""
        des = ""
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
        for i in desList:
            des += i + ","
        des = des[:-1]
        for i in self.silentdesList:
            if len(desList) == 0:
                des += i
            else:
                des += "," + i
        self.silentdesList = []
        return ii + ".children = [" + children + "]\n" + ii + ".res = [" + res + "]\n" + ii + ".decision = [" + des + "]\n" + self.name + ".dialogueGraph.addNode(" + ii + ")"

    def setup(self):
        self.outputNodeRoot()
        self.nextchildrenList.append(self.childrenList)
        self.nextresList.append(self.resList)
        self.nextdesList.append(self.desList)
        self.childrenList = []
        self.resList = []
        self.desList = []

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
                    self.create(j, self.nextresList[counter2][counter], self.nextdesList[counter2][counter], i)
                    self.nextnextchildrenList.append(self.childrenList)
                    self.nextnextresList.append(self.resList)
                    self.nextnextdesList.append(self.desList)
                    self.desList = []
                    self.childrenList = []
                    self.resList = []
        self.nextchildrenList = self.nextnextchildrenList
        self.nextresList = self.nextnextresList
        self.nextdesList = self.nextnextdesList
        self.nextnextdesList = []
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
    
