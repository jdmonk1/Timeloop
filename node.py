class node:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.res = []
        self.decision = []

    def response(self, child):
        counter = 0
        for i in self.children:
            if i == child:
                return self.res[counter]
            counter += 1 
