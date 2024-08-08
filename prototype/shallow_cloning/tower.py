import copy

from .abstract_computer import AbstractComputer
from .abstract_prototype import AbstractPrototype

class Tower(AbstractComputer, AbstractPrototype):
    """
    Define what is a tower.
    """

    def __init__(self, model, processor, size):
        self.model = model
        self.processor = processor
        self.size = size

    def display(self):
        """
        Print current tower properties.
        """
        print(f"Custom computer: {self.model!r}")
        print(f"\t\tProcessor: {self.processor!r}")
        print(f"\t\tSize: {self.size!r}")

    def clone(self):
        """
        Clone current tower.
        """
        return copy.copy(self)
