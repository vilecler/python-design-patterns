class Singleton(type):
    """
    Class that can have only one instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs) -> "Singleton":
        """
        Get the Instance of a Singleton class.
        """        
        if cls not in cls._instances:
            instance = super().__call__(args, kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyObject(metaclass=Singleton):
    """
    Just an example of metaclass usage.
    """
