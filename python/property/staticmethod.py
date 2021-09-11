class staticmethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

class A:
    @staticmethod
    def foo():
        print("No self")