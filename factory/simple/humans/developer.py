from .abstract_human import AbstractHuman

class Developer(AbstractHuman):
    """
    A Human who codes programs.
    """

    def work(self):
        print("I use a computer to work.")

    def eat(self):
        print("I only eat chips.")

    def drink(self):
        print("I only drink sodas.")

    def sleep(self):
        print("I do not sleep a lot.")
