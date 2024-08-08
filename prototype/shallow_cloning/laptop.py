import copy

from .abstract_computer import AbstractComputer
from .abstract_prototype import AbstractPrototype

class Laptop(AbstractComputer, AbstractPrototype):
    """
    Define what is a laptop.
    """

    def __init__(self, model, processor, screen):
        self.model = model
        self.processor = processor
        self.screen = screen

    def display(self):
        """
        Print current laptop properties.
        """
        print(f"Custom computer: {self.model!r}")
        print(f"\t\tProcessor: {self.processor!r}")
        print(f"\t\tScreen: {self.screen!r}")

    def clone(self):
        """
        Clone current laptop.
        """
        return copy.copy(self)
