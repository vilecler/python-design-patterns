from .abstract_human import AbstractHuman

class Painter(AbstractHuman):
    """
    A Humain who creates paintings.
    """

    def work(self):
        print("I use a pencil to paint.")

    def eat(self):
        print("I only eat vegetables.")

    def drink(self):
        print("I only drink water.")

    def sleep(self):
        print("I do sleep a lot.")
