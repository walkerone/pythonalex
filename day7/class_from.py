# -*- coding:utf-8 -*-
# class Foo(object):
#
#
#     def __init__(self,name):
#         self.name = name
#
#
# f = Foo("alex")
# print(type(f))
# print(type(Foo))
print("---------------")
def func(self):
    print("hello learnfirst")
    print('my name is\n',self.name)
def __init__(self,name):
    self.name=name

Foo=type("Foo",(object,),{"talk":func,"__init__":__init__})  #里面的空括号代表继承谁,
# 加入构造函数时必须为__init__  的key不能修改，因为默认回去查找__init__方法
print(type(Foo))
f=Foo("walker")
f.talk()
print(type(f))