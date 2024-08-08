import abc

class AbstractPrototype(abc.ABC):
    """
    Define what is a prototype.
    """

    @abc.abstractmethod
    def clone(self):
        """
        Clone the prototype to a new object.
        """
