class item:

    def __init__(self, name, pickup1, use1, combine1, combineKey1, eat1, drink1, view1, discard1):
        self.name = name
        self.pickup = pickup1
        self.use = use1
        self.combine = combine1
        self.combineKey = combineKey1
        self.eat = eat1
        self.drink = drink1
        self.view = view1
        self.discard = discard1
        self.viewText = "Not implemented Yet"
        self.useText = "Not implemented Yet"
        self.combineText = "Not implemented Yet"
        self.eatText = "Not implemented Yet"
        self.drinkText = "Not implemented Yet"
        self.pickupText = "Not implemented Yet"
        self.discardText = "Not implemented Yet"
        self.unsucessfulText = "attempt was unsucessful"
    
    def printName(self):
        print("Name = ", self.name)

    def printAttributes(self):
        print("pickup = ", self.pickup)
        print("use = ", self.use)
        print("combine = ", self.combine)
        print("combineKey = ", self.combineKey)
        print("eat = ", self.eat)
        print("drink = ", self.drink)
        print("view = ", self.view)
        print("discard = ", self.discard)

    def printText(self):
        print("viewText = ", self.viewText)
        print("useText = ", self.useText)
        print("combineText = ", self.combineText)
        print("eatText = ", self.eatText)
        print("drinkText = ", self.drinkText)
        print("pickupText = ", self.pickupText)
        print("discardText = ", self.discardText)

    def Pickup(self):
        return self.pickupText

    def View(self):
        return self.viewText

    def Use(self):
        return self.useText

    def Combine(self):
        return self.combineText    
    
    def Eat(self):
        return self.eatText

    def Drink(self):
        return self.drinkText

    def Discard(self):
        return self.discardText
