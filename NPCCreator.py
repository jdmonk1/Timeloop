from itemCreator import itemCreator
from NPC import NPC
from animalCreator import animalCreator
import timerGlob
from colors import colors
from itemCreator import itemCreator

class NPCCreator:

    def __init__(self):
        self.animalCreator = animalCreator()
        self.NPCList = []

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

    def James(self, name1, itemL):
        James = NPC(name1, itemL)
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

    def Gideon(self, name1, itemL):
        Gideon = NPC(name1, itemL)
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

    def roach(self, name1, itemL):
        ladyanne = self.animalCreator.roach("roach")
        roach = NPC(name1, itemL)
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

    def Doug(self, name1, itemL):
        Doug = NPC(name1, itemList=itemL)
        self.NPCList.append(Doug)
        dumby = self.dumby
        a00 = Doug.dialogueGraph.createNode("I like your dog. Is it a Golden Retriever?")
        a11res = "Yes it is. Actually I was about to go on a walk with my dog."

        a33 = Doug.dialogueGraph.createNode("Hi! how are you. I am in a bit of a pinch. could you spot me 10 dollars?")
        a44res = "Who do you take me for? I am not the bank of Paris? Sorry you will have to find your money elsewhere."

        a66 = Doug.dialogueGraph.createNode("Hello! what time is it?")
        a77res = "It is..."
        a88des = self.timePrintDoug
        Doug.dialogueGraph.root.children = [a00,a33,a66]
        Doug.dialogueGraph.root.res = [a11res,a44res,a77res]
        Doug.dialogueGraph.root.decision = [dumby,dumby,a88des]
        Doug.dialogueGraph.addNode(Doug.dialogueGraph.root)
        a99 = Doug.dialogueGraph.createNode("I was wondering if you have a seen a key lying around? I lost mine that goes to my safe.")
        a1010res = "Yes! I found one lying around but how do I know it is yours?"

        a1212 = Doug.dialogueGraph.createNode("Oh okay! sorry! I will let you go.")
        a1313res = "Thanks... Bye"

        a00.children = [a99,a1212]
        a00.res = [a1010res,a1313res]
        a00.decision = [dumby,dumby]
        Doug.dialogueGraph.addNode(a00)
        a1717 = Doug.dialogueGraph.createNode("wait can you really not help me?")
        a1818res = "Sure can... Bye"

        a2020 = Doug.dialogueGraph.createNode("Oh okay! No problem. Have a nice day!")
        a2121res = "Sure thing... Bye"

        a33.children = [a1717,a2020]
        a33.res = [a1818res,a2121res]
        a33.decision = [dumby,dumby]
        Doug.dialogueGraph.addNode(a33)
        a66.children = [a00,a33,a66]
        a66.res = [a11res,a44res,a77res]
        a66.decision = [dumby,dumby,a88des]
        Doug.dialogueGraph.addNode(a66)
        a2727 = Doug.dialogueGraph.createNode("It is mine here is my room ticket. See! could you give me my key!")
        a2828res = "Okay... but I require a finder's reward... 50 dollars should suffice."

        a99.children = [a2727]
        a99.res = [a2828res,a11res,a44res,a77res]
        a99.decision = []
        Doug.dialogueGraph.addNode(a99)
        a3232 = Doug.dialogueGraph.createNode("Okay here is the 50 dollars... Can I have my key back?")
        a3333res = "Thanks... here it is... Bye."
        a3434des = self.dougGiveKey
        a2727.children = [a3232]
        a2727.res = [a3333res,a11res,a44res,a77res]
        a2727.decision = [a3434des]
        Doug.dialogueGraph.addNode(a2727)

        return Doug

    def janitor(self, name1, itemL):
        janitor = NPC(name1, itemList=itemL)
        self.NPCList.append(janitor)
        dumby = self.dumby

        a00 = janitor.dialogueGraph.createNode("hey! what's up?")
        a11res = "I am doing good... now where did I put that...."

        a33 = janitor.dialogueGraph.createNode("Hi! I am looking for the airport. Do you happen to know where that is?")
        a44res = "Yeah, I know. It is just down the hallway. take the elevator to the lobby and then go out on the portico and take a taxi."

        a66 = janitor.dialogueGraph.createNode("Hello! what time is it?")
        a77res = "It is..."
        a88des = self.timePrintDoug
        janitor.dialogueGraph.root.children = [a00,a33,a66]
        janitor.dialogueGraph.root.res = [a11res,a44res,a77res]
        janitor.dialogueGraph.root.decision = [dumby,dumby,a88des]
        janitor.dialogueGraph.addNode(janitor.dialogueGraph.root)
        a99 = janitor.dialogueGraph.createNode("What are you looking for?")
        a1010res = "I am looking for a spool of thread... Good grief... Were did I put it..."

        a00.children = [a99]
        a00.res = [a1010res]
        a00.decision = [dumby]
        janitor.dialogueGraph.addNode(a00)
        a1414 = janitor.dialogueGraph.createNode("Hey is that it on the ground?")
        a1515res = "No... That is a dust bunny... Thanks for looking though... My boss will have my head if I cannot find it."

        a1717 = janitor.dialogueGraph.createNode("Hey do you think you could spot me some money?")
        a1818res = "No... I am too busy to help right now... You will have to find some one else."

        a99.children = [a1414,a1717]
        a99.res = [a1515res,a1818res]
        a99.decision = [dumby,dumby]
        janitor.dialogueGraph.addNode(a99)
        a2222 = janitor.dialogueGraph.createNode("(give the janitor a spool of thread)")
        a2323res = ""
        a2424des = self.janitorGiveItem
        a1414.children = [a2222]
        a1414.res = [a2323res]
        a1414.decision = [a2424des]
        janitor.dialogueGraph.addNode(a1414)

        return janitor

    def jannet(self, name1, itemL):
        Jannet = NPC(name1, itemList=itemL)
        self.NPCList.append(Jannet)
        dumby = self.dumby

        a00 = Jannet.dialogueGraph.createNode("Hi Jannet how are you today!")
        a11res = "Hi! I was doing good until I droped this mans brush into this pile of goo."

        Jannet.dialogueGraph.root.children = [a00]
        Jannet.dialogueGraph.root.res = [a11res]
        Jannet.dialogueGraph.root.decision = [dumby]
        Jannet.dialogueGraph.addNode(Jannet.dialogueGraph.root)
        a33 = Jannet.dialogueGraph.createNode("You could probably clean it off. He probably wont notice and you could be on your way. Here... I will show you.")
        a44res = "I could loose my job over that... No way I am doing that thank you very much."

        a66 = Jannet.dialogueGraph.createNode("I have got a joke... knock knock...")
        a77res = "who is there... seriously... :("

        a99 = Jannet.dialogueGraph.createNode("What time is it?")
        a1010res = "It is..."
        a1111des = self.timePrintDoug
        a00.children = [a33,a66,a99]
        a00.res = [a44res,a77res,a1010res]
        a00.decision = [dumby,dumby,a1111des]
        Jannet.dialogueGraph.addNode(a00)
        a1414 = Jannet.dialogueGraph.createNode("brush...")
        a1515res = "brush who... oh wait do you have a brush I could have?"

        a66.children = [a1414]
        a66.res = [a1515res]
        a66.decision = [dumby]
        Jannet.dialogueGraph.addNode(a66)
        a1919 = Jannet.dialogueGraph.createNode("(hand a brush to jannet)")
        a2020res = ""
        a2121des = self.jannetGiveItem
        a1414.children = [a1919]
        a1414.res = [a2020res]
        a1414.decision = [a2121des]
        Jannet.dialogueGraph.addNode(a1414)

        return Jannet

    def timePrintDoug(self, item="key"):
        print(timerGlob.my_timer)
        
    def dougGiveKey(self, item="key",costtype="cash", cost=50):    
        for d in self.NPCList:
            if d.name == "Doug":
                d.itemToPlayer(item, costtype, cost)

    def janitorGiveItem(self, item=["$10", "$10", "$5"], costtype="item", cost="spool_of_thread"):
        for j in self.NPCList:
            if j.name == "janitor":
                j.itemToPlayer(item, costtype, cost)

    def jannetGiveItem(self, item=["$10", "$5"], costtype="item", cost="brush"):
        for j in self.NPCList:
            if j.name == "jannet":
                j.itemToPlayer(item, costtype, cost)

    def dumby(self):
        pass