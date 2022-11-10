from utils import retrieveJsonData
from cli.interface import Interface
import os


class Game:
    def __init__(self):
        dirname = os.path.dirname(__file__)

        self.teams = retrieveJsonData(f"{dirname}/assets/teams.json")
        self.tracks = retrieveJsonData(f"{dirname}/assets/tracks.json")
        self.quizzes = retrieveJsonData(f"{dirname}/assets/quizzes.json")
        self.interface = Interface()
        self.selected_team = None
        self.current_track = self.tracks[0]

    def newGame(self):
        """TODO:
        - [] Ask player to select a team
        - [] Move to first race weekend
        """
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

        self.selected_team = self.interface.displayAvailableTeams(self.teams)

        print(
            f"Congratulations, you are now part of the {self.selected_team['name']} team."
        )
        print("...")
        print(
            f"Welcome to you first race weekend which has place in {self.current_track['name']}"
        )
        print("Let's start with the qualifying and see how well you know Formula 1")

    def simulateRace(self):
        pass

    def simulateQualifying(self):
        pass

    def gameLoop(self):
        while True:
            pass
