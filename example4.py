class MyClass:
    def func(self, *args):
        if len(args) == 1:
            print(1+2)
        elif len(args) == 2:
            print(2-1)


obj = MyClass()

obj.func(1)
obj.func(1, 2)
