# -*- coding:utf-8 -*-

class MyType(type):
    def __init__(self, *args, **kwargs):
        print("Mytype __init__", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ", obj, *args, **kwargs)
        # print(self)
        self.__init__(obj, *args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__", *args, **kwargs)
        return type.__new__(cls, *args, **kwargs)


class Foo(object):
    metaclass=MyType

    def __init__(self, name):
        self.name = name
        print(self.name)

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__", cls, *args, **kwargs)
        return object.__new__(cls)  # 继承父类的的  __new__方法并返回


f = Foo("walker")  # __new__方法时再类之前执行的 ；类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__
print("f", f)
