"""
Author: Pedro Soares
Date: 13/11/2022
Time: 17:00
Version: 0.1
Product Name: SPOP - F1 CLI Game

Description:
    SPOP is a simple game that combines both Formula 1 and a quiz gameself.
    A Formula 1 championship is composed of a series of race weekends,
    where each race weekend is composed of a practice session, a qualifying
    session and a race. For this game, only the qualifying and race sessions are
    considered and thus a race weekend is composed of a qualifying and a race.
    In order to simulate the qualifying, the game presents a quiz based on
    Formula 1, which based on the answers will determine in what position the
    user will end up. The position is also based on a team performance score,
    which tries to replicate the performance of the real teams.
    As for the race, this will be entirely simulated based on the qualifying
    position and the team performance score.
    The main objective of this SPOP, is to entertain the users.

File Description:
    This file is the main entry point to the system. Furthermore, it also
    contains the main class for the system functions.
    For more information please refer to the different docstrings.
"""
from game import Game
from cli.interface import Interface
from menus import welcome_menu


class System:
    """System class which contains any related methods to the system.
    """

    def __init__(self):
        self.exit = False
        self.interface = Interface()
        self.game = Game()
        self.currentMenu = None

    def start(self):
        welcome_menu.print_menu()
        selection = self.interface.prompt_selection(
            "Please choose one of the available options: ", (1, welcome_menu.nbr_of_menu_items()))
        welcome_menu.select_menu_item(selection)
        # self.loop()


if __name__ == "__main__":
    system = System()
    system.start()
