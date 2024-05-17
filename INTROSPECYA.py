import inspect
from random import randint
def introspection_info(obj):
    attributes = []
    methods = []
    for atr in dir(obj):

        if callable(getattr(obj, atr)):
            methods.append(atr)
        else:
            attributes.append(atr)
    modul = inspect.getmodule(randint).__name__ if inspect.getmodule(obj) else '__main'
    return  {'type(obj': type(obj).__name__, 'attributes': attributes, 'methods': methods, 'modul': modul}



number_info = introspection_info(42)
print(number_info)
