class classmethod(object):
    def __init__(self, f):
        self.f = f
    
    def __get__(self, obj, clss=None):
        if clss is None:
            clss = type(obj)
        def newfunc(*args):
            return self.f(clss, *args)
        return newfunc

class A:
    @classmethod
    def foo(clss):
        print(clss)
    
class B:
    pass

B.foo() # <class '__main__.B'>
