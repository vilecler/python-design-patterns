class MonoState:
    _state = {}

    def __new__(cls,  *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls._state
        return self

class MyObject(MonoState):
    """
    Just an example of MonoState usage.
    """
