from NPC import NPC

class NPCCreator:

    def __init__(self):
        pass

    def jonathan(self, name1):
        jonathan = NPC(name1)

        hello = jonathan.dialogueGraph.createNode("hello!")
        hellores = "hello how are you?"
        water = jonathan.dialogueGraph.createNode("can I have some water?")
        waterres = "Yes, yes... here is a water bottle!"
        where = jonathan.dialogueGraph.createNode("were am I")
        whereres = "You are in the hotel"
        time = jonathan.dialogueGraph.createNode("what time is it?")
        timeres = "it is 7:00AM"
        name = jonathan.dialogueGraph.createNode("what is your name")
        nameres = "My name is " + name1
        old = jonathan.dialogueGraph.createNode("how old are you?")
        oldres = "I amd 29 years old"
        bye = jonathan.dialogueGraph.createNode("see you later... Bye")
        byeres = "bye"

        jonathan.dialogueGraph.root.res = [hellores, waterres, whereres, timeres, nameres, oldres, byeres]
        jonathan.dialogueGraph.root.children = [hello, water, where, time, name, old, bye] 
        jonathan.dialogueGraph.addNode(jonathan.dialogueGraph.root)

        hello21 = jonathan.dialogueGraph.createNode("I am fine where can I get some water?")
        hello21res = "Yes, yes... here is a water bottle!"
        hello22 = jonathan.dialogueGraph.createNode("see you later... Bye")
        hello22res = "bye"


        hello.res = [hello21res, hello22res]
        hello.children = [hello21, hello22]
        jonathan.dialogueGraph.addNode(hello21)
        jonathan.dialogueGraph.addNode(hello22)
    
        jonathan.dialogueGraph.addNode(hello)
        jonathan.dialogueGraph.addNode(water)
        jonathan.dialogueGraph.addNode(where)
        jonathan.dialogueGraph.addNode(time)
        jonathan.dialogueGraph.addNode(name)
        jonathan.dialogueGraph.addNode(old)
        jonathan.dialogueGraph.addNode(bye)
        return jonathan
