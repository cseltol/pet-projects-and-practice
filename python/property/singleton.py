class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print(f"args {args}, kwargs {kwargs} ")
        if Singleton._instance is None:
            Singleton._instance = super().__new__(cls)
        return Singleton._instance
    
    def __init__(self, value):
        self.value = value
    

a = Singleton(42)
b = Singleton(92)

assert a is b
assert a.value == 42
