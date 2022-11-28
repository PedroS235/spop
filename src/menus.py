import sys
from menu import Menu
from menu_item import MenuItem
from game import Game
from admin_panel import AdminPanel
from cli.interface import Interface


def game_menu():
    game_main_menu.print_menu()
    selected = Interface().prompt_selection(
        "Please choose one of the available options: ", (1, game_main_menu.nbr_of_menu_items()))
    game_main_menu.select_menu_item(selected)


welcome_menu = Menu("Welcome to SPOP")
item1 = MenuItem("Regular User", game_menu)
item2 = MenuItem("Administrator", lambda: AdminPanel())
item3 = MenuItem("Quit", lambda: sys.exit(0))
welcome_menu.add_menu_items([item1, item2, item3])

# -----------------------

admin_panel_main_menu = Menu("Admin Panel")
item1 = MenuItem("Manage Teams", lambda: None)
item2 = MenuItem("Manage Quizzes", lambda: None)
item3 = MenuItem("Change password", lambda: None)
item4 = MenuItem("Quit", lambda: sys.exit(0))

admin_panel_manage_teams = Menu("Manage Teams")
item1 = MenuItem("Go Back", lambda: None)
item2 = MenuItem("Add a new Team", lambda: None)
item3 = MenuItem("Update a Team", lambda: None)
item4 = MenuItem("Remove a Team", lambda: None)
admin_panel_manage_teams.add_menu_items([item1, item2, item3, item4])

admin_panel_manage_quizzes = Menu("Manage Quizzes")
item1 = MenuItem("Go Back", lambda: None)
item2 = MenuItem("Add a new Quizz", lambda: None)
item3 = MenuItem("Update a Quizz", lambda: None)
item4 = MenuItem("Remove a Quizz", lambda: None)
admin_panel_manage_quizzes.add_menu_items([item1, item2, item3, item4])

game_main_menu = Menu("Main Menu")
item1 = MenuItem("New Game", lambda: Game().new_game())
item2 = MenuItem("Quit", lambda: sys.exit(0))
game_main_menu.add_menu_items([item1, item2])
