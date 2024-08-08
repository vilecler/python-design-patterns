class Human:

    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.is_male = None
        self.is_female = None

    def set_first_name(self, first_name: str) -> "Human":
        self.first_name = first_name
        return self

    def set_last_name(self, last_name: str) -> "Human":
        self.last_name = last_name
        return self

    def set_male(self) -> "Human":
        self.is_male = True
        return self

    def set_female(self) -> "Human":
        self.is_female = True
        return self
