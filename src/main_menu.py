from menu import Menu
from menu_item import MenuItem
from game import Game
from admin_panel import AdminPanel

welcome_menu = Menu("Welcome to SPOP")
item1 = MenuItem("Regular User", lambda: Game().newGame())
item2 = MenuItem("Administrator", lambda: AdminPanel())
welcome_menu.addMenuItems([item1, item2])
