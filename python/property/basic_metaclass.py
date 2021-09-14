from typing import OrderedDict


class Meta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return OrderedDict()
    
    def __new__(cls, name, bases, attrs, **kwargs):
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)