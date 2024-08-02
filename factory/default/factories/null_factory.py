from humans.null_human import NullHuman
from .abstract_factory import AbstractFactory

class NullFactory(AbstractFactory):

    def create_human(self):
        null_human = NullHuman('Unknown')
        null_human.name = 'Unknown'
        return null_human
