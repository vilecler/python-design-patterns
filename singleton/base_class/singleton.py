class Singleton:
    """
    Class that can have only one instance.
    """
    _instances= {}

    def __new__(cls, *args, **kwargs) -> "Singleton":
        """
        Get the Instance of a Singleton class.
        """
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
