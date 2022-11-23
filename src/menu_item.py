"""
Author: Pedro Soares
Date: 14/11/2022
Time: 17:27
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
    Contains the class MenuItem which corresponds to an item of a menu.

DISCLAIMER: This file is not complete!
"""


class MenuItem:
    def __init__(self, text, function):
        self.text = text
        self.onClick = function

    def __str__(self) -> str:
        return self.text
