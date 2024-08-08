from .human import Human

class God:
    """
    Director class.
    """

    @staticmethod
    def create_adam() -> Human:
        return Human().set_first_name('Adam').set_male()

    @staticmethod
    def create_eve() -> Human:
        return Human().set_first_name('Eve').set_female()
