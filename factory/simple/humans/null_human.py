from .abstract_human import AbstractHuman

class NullHuman(AbstractHuman):
    """
    A default Human class.
    """

    def __init__(self, name: str):
        self._name = name

    def work(self):
        print(f"My name is {self._name}. I do not work.")

    def eat(self):
        print("I eat many things.")

    def drink(self):
        print("I drink many things.")

    def sleep(self):
        print("I sleep enough.")
