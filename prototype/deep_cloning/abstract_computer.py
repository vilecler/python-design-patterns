import abc

class AbstractComputer(abc.ABC):
    """
    Define what is a computer.
    """

    @abc.abstractmethod
    def display(self):
        """
        Print elements of the computer.
        """
        