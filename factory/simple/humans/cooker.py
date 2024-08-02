from .abstract_human import AbstractHuman

class Cooker(AbstractHuman):
    """
    A Human that cook dishes.
    """
    
    def work(self):
        print("I ustensils to cook.")

    def eat(self):
        print("I eat everything.")

    def drink(self):
        print("I drink wine.")

    def sleep(self):
        print("I sleep enough.")
