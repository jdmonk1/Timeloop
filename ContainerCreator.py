from item import item
from container import container
class ContainerCreator:

    def __init__(self):
        self.combineKey = 0
    
    def safe(self, name, itemList, key, description, open=False):
        return container(name, itemList, key, description, open)

    def suitCase(self, name, itemList, key, description, open=False):
        return container(name, itemList, key, description, open)

    def trashCan(self, name, itemList, key, description, open=True):
        return container(name, itemList, key, description, open)
    
    def getCombineKey(self):
        self.combineKey += 1
        return self.combineKey