import os


class Menu:
    def __init__(self, title, items=None):
        self.title = title
        self.menuItems = [] if not items else items

    def addMenuItems(self, items):
        self.menuItems = items

    def addMenuItem(self, item):
        self.menuItems.append(item)

    def selectMenuItem(self, index):
        assert index <= len(self.menuItems) and index >= 1
        self.menuItems[index-1].onClick()

    def nbrOfMenuItems(self):
        return len(self.menuItems)

    def printMenu(self):
        os.system('cls||clear')
        print("-" * (len(self.title) + 4))
        print(f"| {self.title} |")
        print("-" * (len(self.title) + 4))

        for index, item in enumerate(self.menuItems):
            print(f"{index+1} -> {item}")
