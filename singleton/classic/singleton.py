class Singleton:
    """
    Class that can have only one instance.
    """

    @staticmethod
    def get_instance() -> "Singleton":
        """
        Get the Instance of a Singleton class.
        """
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
