class A:
    def __call__(self, *args, **kwargs):
        print(f"Called: {args} {kwargs}")
    
a = A()
a(42) # Called: (42,) {}