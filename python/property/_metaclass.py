class Foo:
    pass

class Meta(type):
    def __call__(self, *args, **kwargs):
        return Foo()

class A(metaclass=Meta):
    pass

assert type(A) is Meta

a = A()
assert isinstance(a, Foo)
