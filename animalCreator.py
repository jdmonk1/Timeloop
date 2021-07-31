from animal import animal

class animalCreator:

    def __init__(self):
        pass

    def roach(self, name, move=False, talk=True, ride=False, eat=False, drink=False, consume=False, attack=False):
        return animal(move,talk,ride,eat,drink,consume,attack,name)

    def ant(self, name, move=False, talk=True, ride=False, eat=False, drink=False, consume=True, attack=True):
        return animal(move,talk,ride,eat,drink,consume,attack,name)
    
    def dog(self, name, move=True, talk=False, ride=False, eat=True, drink=True, consume=True, attack=True):
        return animal(move,talk,ride,eat,drink,consume,attack,name)