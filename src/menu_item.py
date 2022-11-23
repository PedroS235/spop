class MenuItem:
    def __init__(self, text, function):
        self.text = text
        self.onClick = function

    def __str__(self) -> str:
        return self.text
