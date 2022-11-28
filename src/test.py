from admin_panel import AdminPanel
import json

p = AdminPanel()
print(json.dumps(p.teams, indent=2))

p.add_team({"id": 10, "name": "my team", "performance_score": 33})
print(json.dumps(p.teams, indent=2))

p.update_team(10, "Hello world", 10)
print(json.dumps(p.teams, indent=2))

p.remove_team(10)
print(json.dumps(p.teams, indent=2))

p.add_quiz({"id": 3, "question": "How are you?", "answers": [
           "213", "34213"], "correct_answer_index": 1})
print(json.dumps(p.quizzes, indent=2))

p.update_quiz(3, "Yeah boy", ["ok", "Not ok"], 0)
print(json.dumps(p.quizzes, indent=2))

p.remove_quiz(3)
print(json.dumps(p.quizzes, indent=2))
