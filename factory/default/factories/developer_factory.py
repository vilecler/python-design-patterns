from humans.developer import Developer
from .abstract_factory import AbstractFactory

class DeveloperFactory(AbstractFactory):

    def create_human(self):
        developer = Developer()
        developer.name = 'Developer'
        return developer
