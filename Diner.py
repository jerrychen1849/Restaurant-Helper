from MenuItem import MenuItem

class Diner(object):
    # class variable for statuses
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, name):
        # name is an input paramter
        self.name = name
        self.order = [] # empty list
        self.status = 0 # starting status for Diner

    # getters for the instance attributes
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.status

    # add one to status attribute
    def updateStatus(self):
        self.status += 1

    # MenuItem object is passed in
    def addToOrder(self, menuItem):
        self.order.append(menuItem) # add to the list of orders using append

    # loop through orders attribute
    def printOrder(self):
        orderLength = len(self.order)
        for x in range(0, orderLength):
            print(self.order[x]) # print out each MenuItem in the list

    def calculateMealCost(self):
        cost = 0
        orderLength = len(self.order)
        for x in range(0, orderLength): # loop thru orders attribute lsit
            price = self.order[x].getPrice() # price is an attribute of the MenuItem object
            cost += price
        return cost

    # string w/ Diner name + status
    def __str__(self):
        info = "\t" + "Diner " + self.name + " is currently " + Diner.STATUSES[self.status]
        return info





