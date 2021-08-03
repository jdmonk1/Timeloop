from item import item
from random import randint
from random import seed

class itemCreator:

    def __init__(self):
        self.combineKey = 0

          # self, pickup1, use1, combine1, combineKey1, eat1, drink1, view1, discard1
    def key(self, name, description, pickup=True, use=True, combine=False, eat=False, drink=False, view=True, discard=True, nutrition=0):
        return item(name, pickup, use, combine, self.getcombineKey(), eat, drink, view, discard, nutrition, description)

    def jerky(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=True, drink=False, view=True, discard=True, nutrition=randint(10, 20)):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def waterBottle(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=True, view=True, discard=True, nutrition=50):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def infoLetter(self, name, description, pickup=True, use=False, combine=True, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=0):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def paperclip(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=True, drink=False, view=True, discard=True, nutrition=-10):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)
    
    def spoolOfThread(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=-0):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)
    
    def cash(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=-0):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def ticket(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=0):
        return  item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def brush(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=0):
        return item(name, pickup, use, combine, combine, eat, drink, view, discard, nutrition, description)

    def phone(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=-0):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)

    def usb(self, name, description, pickup=True, use=False, combine=False, combineKey=-1, eat=False, drink=False, view=True, discard=True, nutrition=-0):
        return item(name, pickup, use, combine, combineKey, eat, drink, view, discard, nutrition, description)
    
    def getcombineKey(self):
        self.combineKey += 1
        return self.combineKey

    
        