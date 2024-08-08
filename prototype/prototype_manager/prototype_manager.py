from .abstract_prototype import AbstractPrototype

class PrototypeManager(dict):
    """
    Helps to manage Prototype when there is a lot
    """
    def __setitem__(self, key, prototype):
        if issubclass(prototype, AbstractPrototype):
            dict.__setitem__(self, key, prototype)
