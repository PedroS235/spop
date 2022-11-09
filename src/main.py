from cli.Menu import Menu
from cli.MenuItem import MenuItem
from game import Game


class System:
    def __init__(self):
        self.exit = False
        self.game = Game()
        self.currenMenu = None

    def loop(self):
        while not self.exit:
            pass
