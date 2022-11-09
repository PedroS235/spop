from menu import Menu
from menu_item import MenuItem


class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__("Main Menu")
        self.menuitems = [MenuItem("New Game")]
