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
    Contains the main class for the interface utilities functions. For more
    information please refer to the different docstrings.
"""


class Interface:
    """Interface class which contains useful methods to display information.

        This class contains 2 methods to display text to the screen. The first one 
        is to display the available teams and ask the player to choose one. The
        second one is to display a quiz answer and ask the player to choose one.
    """

    def prompt_selection(self, msg: str, selection_range: tuple):
        """
        This method prompts a message with the intent of retrieving an index.
        In case the user enters an invalid range, it will re-prompt until it
        gets a successfull answer.

        Args:
            msg: message to be askedself.
            range: The range that should e expected

        Returns:
            The selected index.

        """

        try:
            index = int(input(msg))
        except ValueError:
            index = -1

        while index < selection_range[0] or index > selection_range[1]:
            print("Error: Make sure you have entered a valid value!")
            try:
                index = int(input(msg))
            except ValueError:
                continue

        return index

    def display_available_teams(self, teams: list):
        """
        This method prints the available teams in the terminal
        and prompts the user to choose one of the teams.

        Args:
            teams: list of the available teams, where a team is a dictionary
            with the form {id, name, performance_score}.

        returns:
            The selected team
        """

        print(f"There are {len(teams)} available teams for you to choose:")
        print("| ID | Name | Performance score |")
        for team in teams:
            print(
                f"| {team['id']+1} | {team['name']} | {team['performance_score']}")

        selected_id = self.prompt_selection(
            "Enter the team ID you want: ", (1, len(teams))
        )
        for team in teams:
            if team["id"] == selected_id-1:
                return team
        return None

    def display_quiz_answers(self, answers: list):
        """
        This method prints a quiz possible answers and prompts the user to
        choose one of the possible answers.

        Args:
            answers: List of the answers to be displayed.

        returns:
            The selected answer index.
        """

        for index, answer in enumerate(answers):
            print(f"{index+1} - {answer}")

        return self.prompt_selection(
            "Enter the answer number you think is the correct answer: ",
            (1, len(answers)),
        )
