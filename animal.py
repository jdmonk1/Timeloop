from NPC import NPC

class animal:

    def __init__(self, move, talk, ride, eat, drink, consume, attack, name):
        self.name = name
        self.move = move
        self.talk = talk
        self.ride = ride
        self.eat = eat
        self.drink = drink
        self.consume = consume
        self.attack = attack
        self.NPC = NPC(self.name)

    def talk(self):
        while True:
            pass


    
