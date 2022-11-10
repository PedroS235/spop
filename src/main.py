from game import Game


class System:
    def __init__(self):
        self.exit = False
        self.game = Game()
        self.currenMenu = None

    def start(self):
        self.loop()

    def loop(self):
        self.game.newGame()


if __name__ == "__main__":
    system = System()
    system.start()
