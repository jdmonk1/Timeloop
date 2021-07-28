from NPC import NPC

class NPCCreator:

    def __init__(self):
        pass

    def jonathan(self, name1):
        jonathan = NPC(name1)

        hello = jonathan.dialogueGraph.createNode("Excuse me?")
        hellores = "Yes?"
        water = jonathan.dialogueGraph.createNode("can I have some water?")
        waterres = "Yes, yes... here is a water bottle!"
        where = jonathan.dialogueGraph.createNode("where am I")
        whereres = "You are in the hotel"
        time = jonathan.dialogueGraph.createNode("what time is it?")
        timeres = "it is 7:00AM"
        name = jonathan.dialogueGraph.createNode("what is your name")
        nameres = "My name is " + name1
        old = jonathan.dialogueGraph.createNode("how old are you?")
        oldres = "I am 29 years old"
        bye = jonathan.dialogueGraph.createNode("Thank you, goodbye")
        byeres = "bye"

        jonathan.dialogueGraph.root.children = [hello]
        jonathan.dialogueGraph.root.res = [hellores]

        jonathan.dialogueGraph.root.res = [hellores, waterres, whereres, timeres, nameres, oldres, byeres]
        # jonathan.dialogueGraph.root.children = [hello, water, where, time, name, old, bye] 
        jonathan.dialogueGraph.addNode(jonathan.dialogueGraph.root)

        hello21 = jonathan.dialogueGraph.createNode("I really need some water. Do you have any to spare?")
        hello21.children = [where, time, name, old, bye]
        hello21.res = [whereres, timeres, nameres, oldres, byeres]
        hello21res = "Yeah, sure... here you are."
        hello22 = jonathan.dialogueGraph.createNode("Never mind")
        hello22res = "Uhh... okay"


        hello.res = [hello21res, hello22res]
        hello.children = [hello21, hello22]
        jonathan.dialogueGraph.addNode(hello21)
        jonathan.dialogueGraph.addNode(hello22)
        water.children = [where, time, name, old, bye]
        where.children = [where, time, name, old, bye]
        time.children = [where, time, name, old, bye]
        name.children = [where, time, name, old, bye]
        old.children = [where, time, name, old, bye]
        bye.children = [where, time, name, old, bye]
        water.res = [whereres, timeres, nameres, oldres, byeres]
        where.res = [whereres, timeres, nameres, oldres, byeres]
        time.res = [whereres, timeres, nameres, oldres, byeres]
        name.res = [whereres, timeres, nameres, oldres, byeres]
        old.res = [whereres, timeres, nameres, oldres, byeres]
        bye.res = [whereres, timeres, nameres, oldres, byeres]

    
        jonathan.dialogueGraph.addNode(hello)
        jonathan.dialogueGraph.addNode(water)
        jonathan.dialogueGraph.addNode(where)
        jonathan.dialogueGraph.addNode(time)
        jonathan.dialogueGraph.addNode(name)
        jonathan.dialogueGraph.addNode(old)
        jonathan.dialogueGraph.addNode(bye)
        return jonathan

    def James(self, name1):
        James = NPC(name1)
        a00 = James.dialogueGraph.createNode("Hello!")
        a11res = "hi... who are you?"
        a22 = James.dialogueGraph.createNode("give me what I want")
        a33res = "NEVER!!"
        James.dialogueGraph.root.children = [a00,a22]
        James.dialogueGraph.root.res = [a11res,a33res]
        James.dialogueGraph.addNode(James.dialogueGraph.root)
        a44 = James.dialogueGraph.createNode("I am James, and you are...?")
        a55res = "I am also James... what a coincidence!"
        a00.children = [a44]
        a00.res = [a55res]
        James.dialogueGraph.addNode(a00)
        return James
