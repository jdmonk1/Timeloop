from itemCreator import itemCreator

IC = itemCreator()
key = IC.key("key1")
key2 = IC.key("key2")
backpack = []
backpack.append(key)
backpack.append(key2)
key.printAttributes()
key.printText()
key2.printAttributes()
key2.printText()
key.viewText = "testing"
key.useText = "used " + key.name + " succesfully"
key.printText()
key2.printText()
key.printName()
key2.printName()
if key in backpack:
    print(key.Use())
