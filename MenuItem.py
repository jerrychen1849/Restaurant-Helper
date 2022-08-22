class MenuItem(object):
    # "cookie cutter" for object
    def __init__(self, name, itemType, price, description):
        # instance variables as input parameters, set equal to self attributes
        self.name = name
        self.itemType = itemType
        self.price = float(price)
        self.description = description

    # getters
    # retrieve and change value of each instance attribute for each "cookie" from class "cookie cutter"
    def getName(self):
        return self.name

    def getItemType(self):
        return self.itemType

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    # string with instance attributes
    def __str__(self):
        info = self.name + " (" + self.itemType + "): " + "$" + str(self.price)
        info += "\n\t" + self.description
        return info