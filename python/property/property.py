class property(object):
    def __init__(self, fget=None, fset=None, fdel=None):
      self.fget = fget
      self.fset = fset
      self.fdel = fdel

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)
    
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


class A:
    @property
    def foo(self):
        return self.bar
    
    @foo.setter
    def foo(self, value):
        self.bar = value


a = A()
a.foo = 42
assert a.foo == 42
