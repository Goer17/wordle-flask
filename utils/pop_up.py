class PopUp:
    def __init__(self, info: str, ) -> None:
        self.info = info

class ShortInfo(PopUp):
    def __init__(self, info: str) -> None:
        super().__init__(info)

class Wind(PopUp):
    def __init__(self, info: str, close_text: str) -> None:
        super().__init__(info)
        self.close_text = close_text