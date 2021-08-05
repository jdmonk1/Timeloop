from NPC import NPC
from animalCreator import animalCreator

class NPCCreator:

    def __init__(self):
        self.animalCreator = animalCreator()

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

    def Gideon(self, name1):
        Gideon = NPC(name1)
        a00 = Gideon.dialogueGraph.createNode("Hallo!!!")
        a11res = "Who are you?"
        a22 = Gideon.dialogueGraph.createNode("Hi")
        a33res = "You stink!"
        Gideon.dialogueGraph.root.children = [a00,a22]
        Gideon.dialogueGraph.root.res = [a11res,a33res]
        Gideon.dialogueGraph.addNode(Gideon.dialogueGraph.root)
        a44 = Gideon.dialogueGraph.createNode("Nunya")
        a55res = "Fine if you are so grumpy go away"
        a66 = Gideon.dialogueGraph.createNode("Bobbert Joe")
        a77res = "You must have gotten bullied as a kid. Here... Here is a free piece of jerky!"
        a00.children = [a44,a66]
        a00.res = [a55res,a77res]
        Gideon.dialogueGraph.addNode(a00)
        a1010 = Gideon.dialogueGraph.createNode("Excuse me?")
        a1111res = "You stink!"
        a1212 = Gideon.dialogueGraph.createNode("I am hungry!")
        a1313res = "Hi hungry. I am Gideon."
        a1414 = Gideon.dialogueGraph.createNode("I know... my eyes are very reflective.")
        a1515res = "That is rude... :("
        a22.children = [a1010,a1212,a1414]
        a22.res = [a1111res,a1313res,a1515res]
        Gideon.dialogueGraph.addNode(a22)
        a1818 = Gideon.dialogueGraph.createNode("Your momma's refrigerator stinks.")
        a1919res = "unfortunatly I have to agree."
        a2020 = Gideon.dialogueGraph.createNode("chicken wink")
        a2121res = "shut up!"
        a1010.children = [a1818,a2020]
        a1010.res = [a1919res,a2121res]
        Gideon.dialogueGraph.addNode(a1010)
        a2424 = Gideon.dialogueGraph.createNode("What are you a middle schooler...?")
        a2525res = "Born and raised."
        a2626 = Gideon.dialogueGraph.createNode("Haa Haa... Very funny. Do you have food?")
        a2727res = "In the pantry dumb dumb."
        a1212.children = [a2424,a2626]
        a1212.res = [a2525res,a2727res]
        Gideon.dialogueGraph.addNode(a1212)
        a3030 = Gideon.dialogueGraph.createNode("I am sorry... but... Have you taken a shower recently?")
        a3131res = "What is a shower?"
        a3232 = Gideon.dialogueGraph.createNode("I am sorry... but... Can you lead me to some food?")
        a3333res = "In the pantry... WHY do you think it is called a PANTRY!!"
        a1414.children = [a3030,a3232]
        a1414.res = [a3131res,a3333res]
        Gideon.dialogueGraph.addNode(a1414)
        a1818.children = [a00,a22]
        a1818.res = [a11res,a33res]
        Gideon.dialogueGraph.addNode(a1818)
        return Gideon

    def roach(self, name1):
        ladyanne = self.animalCreator.roach("roach")
        roach = NPC(name1)
        roach.animal = ladyanne
        a00 = roach.dialogueGraph.createNode("Hallo!!!")
        a11res = "Who are you?"

        a33 = roach.dialogueGraph.createNode("Hi")
        a44res = "You stink!"

        roach.dialogueGraph.root.children = [a00,a33]
        roach.dialogueGraph.root.res = [a11res,a44res]
        roach.dialogueGraph.root.descision = []
        roach.dialogueGraph.addNode(roach.dialogueGraph.root)
        a66 = roach.dialogueGraph.createNode("Nunya")
        a77res = "Fine if you are so grumpy go away"

        a99 = roach.dialogueGraph.createNode("Bobbert Joe")
        a1010res = "You must have gotten bullied as a kid. Here... Here is a free piece of jerky!"
        a1111des = roach.animal.testPrint
        a00.children = [a66,a99]
        a00.res = [a77res,a1010res]
        a00.decision = [a1111des]
        roach.dialogueGraph.addNode(a00)
        return roach

    def Doug(self, name1):
        Doug = NPC(name1)
        ladyanne = self.animalCreator.roach("roach")
        Doug.animal = ladyanne
        a00 = Doug.dialogueGraph.createNode("HI!")
        a11res = "Hello."

        Doug.dialogueGraph.root.children = [a00]
        Doug.dialogueGraph.root.res = [a11res]
        Doug.dialogueGraph.root.decision = []
        Doug.dialogueGraph.addNode(Doug.dialogueGraph.root)
        a33 = Doug.dialogueGraph.createNode("what time is it?")
        a44res = "It is..."
        a55des = Doug.animal.testPrint
        a00.children = [a33]
        a00.res = [a44res]
        a00.decision = [a55des]
        Doug.dialogueGraph.addNode(a00)
        return Doug



