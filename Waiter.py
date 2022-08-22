from Menu import Menu
from Diner import Diner

class Waiter(object):

    # Menu object is passed in
    def __init__(self, menu):
        self.menu = menu # menu instance attribute equals object
        self.diners = [] # set diner attribute to empty list

    def addDiner(self, diner):
        self.diners.append(diner) # append object to list of diners

    def getNumDiners(self):
        numDiners = len(self.diners) # return length of diners attribute
        return numDiners

    def printDinerStatuses(self):
        for statuses in Diner.STATUSES: # loop through statues in our list from Diner
            print("Diners who are " + statuses + ": ")
            for diner in self.diners: # nested for loop
                dinerStatus = diner.getStatus() # get statuses
                if statuses == Diner.STATUSES[dinerStatus]: # status is current status in list of statuses
                    name = diner.getName()  # get name
                    print("\tDiner " + name + "is currently " + statuses) # print status heading

    def takeOrders(self): # take orders of Diners that Waiter is responsible for
        for diner in self.diners:
            if diner.getStatus() == 1: # if diner is ready to order
                for x in range(0,4): # loop thru menu types
                    self.menu.printMenuItemsByType(Menu.MENU_ITEM_TYPES[x]) # print current menu type
                    menuLength = self.menu.getMenuItemsByType(Menu.MENU_ITEM_TYPES[x])
                    choice = 1000000
                    while choice not in range(menuLength-1, -1, -1):
                        choice = int(input("> ")) # take in user's menu choice within range
                    menuItem = self.menu.getMenuItem(Menu.MENU_ITEM_TYPES[x], choice) # get the correct item from list
                    diner.addToOrder(menuItem) # add item to order
                print(diner.name + " ordered:") # print diner's order
                diner.printOrder()

    def ringUpDiners(self):
        for diner in self.diners: # for each diner in waiter's list
            if diner.getStatus() == 3: # ready to pay
                cost = diner.calculateMealCost() # calculte cost of meal
                print("\n" + diner.name + ", your meal cost is $" + str(cost))

    def removeDoneDiners(self):
        for diner in self.diners: # loop backwards
            if diner.getStatus() == 4: # if diner is ready to leave
                print("\n" + diner.name + ", " + "thank you for dining with us! Come again soon!")
                self.diners.remove(diner) # delete diner at index

    def advanceDiners(self):
        self.printDinerStatuses() # diner statuses printed
        self.takeOrders() # take orders
        self.ringUpDiners() # ring up diners
        self.removeDoneDiners() # remove finished diners
        for diner in self.diners: # for each diner in list, update status of diner
            diner.updateStatus()