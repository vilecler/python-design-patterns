import abc

class AbstractHuman(abc.ABC):
    """
    An abstract class to represent a Human.
    """

    def present(self):
        print(f'I am a {self.__class__.__name__}.')

    @abc.abstractmethod
    def work(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def drink(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass
