class cached_property(object):
    """Non-Data Descriptor"""
    def __init__(self, func):
      self.func = func

    def __get__(self, obj, cls):
        value = self.func(obj)
        obj.__dict__[self.func.__name__] = value
        return value
