from inspect import getmembers, isclass, isabstract
import humans

class HumanFactory:
    """
    Simple Factory to create Human.
    """
    _humans = {} # key: class name; value: class value

    def __init__(self) -> None:
        self.load_humans()

    def load_humans(self) -> None:
        """
        Load all Human classes to memory.
        """
        # Get all classes in the module
        classes = getmembers(
            humans,
            lambda x: not isabstract(x) and isclass(x)
        )

        # Only add classes that are children of abstract class to the set ok classes
        for class_name, _type in classes:
            if isclass(_type) and issubclass(_type, humans.AbstractHuman):
                self._humans.update([[class_name, _type]])

    def create_instance(self, human_name: str) -> humans.AbstractHuman:
        """
        Create a Human class by its name or a NullHuman if not found.
        """
        if human_name not in self._humans:
            return humans.NullHuman(human_name)
        return self._humans[human_name]()
