from colors import colors
class container:

    def __init__(self, name, itemList, key, description, open):
        self.name = name
        self.itemList = itemList
        self.key = key
        self.description = description
        self.isOpen = open

    def open(self, key):
        if self.key == key:
            self.isOpen = True
            return colors.GREEN + str(self.name) + " has been opened!!" + colors.BLACK
        else:
            return colors.RED + str(self.name) + " was not opened. The key doesn't fit." + colors.BLACK

    
