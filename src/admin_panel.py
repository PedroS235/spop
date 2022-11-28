from utils import load_json, save_json
from os import path


class AdminPanel:
    def __init__(self):
        self.dirname = path.dirname(__file__)
        self.teams = load_json(f"{self.dirname}/assets/teams.json")
        self.tracks = load_json(f"{self.dirname}/assets/tracks.json")
        self.quizzes = load_json(f"{self.dirname}/assets/quizzes.json")

    def add_team(self, team: dict):
        self.teams.append(team)
        save_json(f"{self.dirname}/assets/teams.json", self.teams)

    def update_team(self, id, name, performance_score):
        for team in self.teams:
            if team["id"] == id:
                team["name"] = name
                team["performance_score"] = performance_score
                save_json(f"{self.dirname}/assets/teams.json", self.teams)
                return True

        return False

    def remove_team(self, id):
        for team in self.teams:
            if team["id"] == id:
                self.teams.remove(team)
                break

        save_json(f"{self.dirname}/assets/teams.json", self.teams)

    def add_quiz(self, quiz: dict):
        self.quizzes.append(quiz)
        save_json(f"{self.dirname}/assets/quizs.json", self.quizzes)

    def update_quiz(self, id, question, answers, correct_answer_id):
        for quiz in self.quizzes:
            if quiz["id"] == id:
                quiz["question"] = question
                quiz["answers"] = answers
                quiz["correct_answer_index"] = correct_answer_id
                save_json(f"{self.dirname}/assets/quizzes.json", self.quizzes)
                return True

        return False

    def remove_quiz(self, id):
        for quiz in self.quizzes:
            if quiz["id"] == id:
                self.quizzes.remove(quiz)
                break

        save_json(f"{self.dirname}/assets/quizzes.json", self.quizzes)
