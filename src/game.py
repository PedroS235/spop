"""
Author: Pedro Soares
Date: 14/11/2022
Time: 17:21
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
    Contains the main class for the game logic. For more information
    please refer to the different docstrings.
"""
from os import path, system
from random import randint

from utils import load_json
from cli.interface import Interface


class Game:
    """Game class which contains the logic of the game.

    The game class has 3 different parts. The First part is the new game which
    welcomes the player by giving some insights of the game. The second part,
    consists in the qualifying session, which asks the player 3 quizzes. The last
    part is the race simulation, which simulates the race based on the team
    score perforamance and qualifying position.

    Attributes:
        teams: List containing the available teams information.
        tracks: List containing the available teams information.
        quizzes: List containing the available teams information.
        interface: Contains useful functions to display information to the screen.
        selected_track: Keeps track of the current track.
    """

    def __init__(self):
        dirname = path.dirname(__file__)

        self.teams = load_json(f"{dirname}/assets/teams.json")
        self.tracks = load_json(f"{dirname}/assets/tracks.json")
        self.quizzes = load_json(f"{dirname}/assets/quizzes.json")
        self.interface = Interface()
        self.selected_team = None
        self.current_track = self.tracks[0]

    def new_game(self):
        """
        Function that welcomes the player to the game explaining what he should
        expect from the game. In addition ask the player to choose one team
        and starts the qualifying session.
        """
        system('cls||clear')

        print("****************************")
        print("Welcome to the F1 Quiz game!")
        print("****************************")
        print()
        print("The first phase of the game consists in choosing the team")
        print("you will be playing for. Next, you will start playing the game, ")
        print("which consists of a series of race weekends. Each race weekend")
        print(" itself is composed of a qualifying and a race.")
        print("Once you have finished a race weekend, you will advance to the next")
        print()
        print("----------------------------------------------")
        print()

        print("Now to start with you will choose a team...")
        print()

        self.selected_team = self.interface.display_available_teams(self.teams)

        print(
            f"Congratulations, you are now part of the {self.selected_team['name']} team."
        )
        print("...")
        print(
            f"Welcome to you first race weekend which has place in {self.current_track['name']}"
        )
        print("Let's start with the qualifying and see how well you know Formula 1")
        self.simulate_qualifying()

    def simulate_race(self):
        """
        TODO: Simulate race based on qualifying position and team score
        performance.
        """

    def simulate_qualifying(self):
        """
        Simulates the qualifying by making the player answering 3 quizz questions.
        The the qualifying position will be computed based on his answers
        and the team score performance.
        """
        system("cls||clear")
        print(f"Welcome to the race weekend in {self.current_track['name']}")
        print("You are now in qualifying!")
        print()
        print('''You will need to answer 3 quizzes. The accuracy of your answers
        will decide your qualifying position!''')

        correct_answers = 0

        for i in range(3):
            print("----------")
            print(f"- Quiz {i} -")
            print("----------")
            print()
            quiz = self.quizzes[randint(0, len(self.quizzes) - 1)]
            print(quiz["question"])

            if self.interface.display_quiz_answers(
                    quiz["answers"]) == quiz['correct_answer_index']:
                correct_answers += 1
                print("Correct answer!")
            else:
                print("Wrong answer!")

        accuracy = correct_answers * 100.0 / 3
        position = int(10 - randint(0, 2) -
                       (10 * accuracy/self.selected_team['performance_score']))
        if position == 0:
            position = 1
        elif position < 0 and accuracy != 100:
            position = 10
        elif position < 0:
            position = 1

        print(f"You have qualifed in position {position}.")
