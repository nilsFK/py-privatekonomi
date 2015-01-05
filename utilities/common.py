class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def as_obj(to_obj):
    return Struct(**to_obj)

def singleton(cls):
    obj = cls()
    # Always return the same object
    cls.__new__ = staticmethod(lambda cls: obj)
    # Disable __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls