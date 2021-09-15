
class IntField:
    def __set_name__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        assert isinstance(value, int)
        instance.__dict__[self._name] = value
    
class FieldMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        for k, v in attrs.items():
            if isinstance(v, IntField):
                v.__set_name__(k)
        return super().__new__(cls, name, bases, attrs)
