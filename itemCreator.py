from item import item

class itemCreator:

    def __init__(self):
        self.combineKey = 0

          # self, pickup1, use1, combine1, combineKey1, eat1, drink1, view1, discard1
    def key(self, name, pickup=True, use=True, combine=False, eat=False, drink=False, view=True, discard=True):
        return item(name ,pickup, use, combine, self.getcombineKey(), eat, drink, view, discard)

    def getcombineKey(self):
        self.combineKey += 1
        return self.combineKey

    
        