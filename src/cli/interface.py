class Interface:
    def displayMenu(self):
        pass

    def promptSelection(self, msg: str, range: tuple):
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

        while index < range[0] or index > range[1]:
            print("Error: Make sure you have entered a valid value!")
            try:
                index = int(input(msg))
            except ValueError:
                continue

        return index

    def displayAvailableTeams(self, teams: list):
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
            print(f"| {team['id']} | {team['name']} | {team['performance_score']}")

        selected_id = self.promptSelection(
            "Enter the team ID you want: ", (0, len(teams) - 1)
        )
        for team in teams:
            if team["id"] == selected_id:
                return team
        return None

    def displayQuizAnswers(self, answers: list):
        for index, answer in enumerate(answers):
            print(f"{index+1} - {answer}")

        return self.promptSelection(
            "Enter the answer number you think is the correct answer: ",
            (1, len(answers)),
        )
