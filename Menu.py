from MenuItem import MenuItem

class Menu(object):
    # class variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, fileName):
        # instance attribute
        self.menuItemDictionary = {"Drink":[],
                              "Appetizer":[],
                              "Entree":[],
                              "Dessert":[]}

        # open file to fill out dictionary
        fileIn = open("menu.csv", "r")

        for line in fileIn:
            line = line.strip() # strip and split to clean up list
            dataList = line.split(",")
            menu = MenuItem(dataList[0], dataList[1], dataList[2], dataList[3]) # object getting to get MenuItem object type and index dictionary
            self.menuItemDictionary[dataList[1]].append(menu) # append to add object to list

        fileIn.close()

    # type of MenuItem object and index of that object in list are parameters passed into function
    def getMenuItem(self, menuItemType, i):
        return self.menuItemDictionary[menuItemType][i] # second index to get object from correct spot in list

    # input parameter
    # return number of objects in list
    def getMenuItemsByType(self, menuItemType):
        menuList = self.menuItemDictionary[menuItemType]
        lenList = len(menuList)
        return lenList

    def printMenuItemsByType(self, menuItemType):
        print("\n-----" + menuItemType + "s" +"-----") # print the type heading (sample output)
        menuList = self.menuItemDictionary[menuItemType] # index menuItemType in dictionary to create menuItemList
        lenMenuList = len(menuList) # len of list
        for x in range(0, lenMenuList): # loop through correct list and print out each object
            print(str(x) + ")" , menuList[x])

