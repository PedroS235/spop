from game import Game
from cli.interface import Interface
from main_menu import welcome_menu


class System:
    def __init__(self):
        self.exit = False
        self.interface = Interface()
        self.game = Game()
        self.currentMenu = None

    def start(self):
        welcome_menu.printMenu()
        selection = self.interface.promptSelection(
            "Please choose one of the available options: ", (1, welcome_menu.nbrOfMenuItems()))
        welcome_menu.selectMenuItem(selection)
        # self.loop()


if __name__ == "__main__":
    system = System()
    system.start()
