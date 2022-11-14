"""
Author: Pedro Soares
Date: 14/11/2022
Time: 17:26
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
    Contains the class Menu which composes a menu with different menu items.
DISCLAIMER: This file is not complete!
"""


class Menu:
    def __init__(self, title, items=None):
        self.title = title
        self.menu_items = [] if not items else items

    def add_menu_items(self, items):
        self.menu_items = items

    def add_menu_item(self, item):
        self.menu_items.append(item)

    def print_menu(self):
        print("-" * (len(self.title) + 4))
        print(f"| {self.title} |")
        print("-" * (len(self.title) + 4))

        for index, item in enumerate(self.menu_items):
            print(f"{index+1} -> {item}")
