import abc

class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_human(self):
        pass
