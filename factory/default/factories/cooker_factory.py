from humans.cooker import Cooker
from .abstract_factory import AbstractFactory

class CookerFactory(AbstractFactory):

    def create_human(self):
        cooker = Cooker()
        cooker.name = 'Cooker'
        return cooker
