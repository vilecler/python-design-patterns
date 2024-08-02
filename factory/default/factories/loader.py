from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abstract_factory import AbstractFactory

def load_factory(factory_name: str) -> AbstractFactory:
    """
    Load a Factory by its name or NullFactory if not found.
    """
    try:
        factory_module = import_module(f'.{factory_name}', 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')

    classes = getmembers(
        factory_module,
        lambda x: not isabstract(x) and isclass(x)
    )

    for _, _class in classes:
        if issubclass(_class, AbstractFactory):
            return _class()
