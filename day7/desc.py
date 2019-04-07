# -*- coding:utf-8 -*-
class walker(object):
    age2="33"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def page(self):
        print("page1")
    @property
    def eat(self):
        print("dddd")
print(walker.__dict__)  #获取类的成员，即：静态字段、方法、
w=walker("zhang","18")
print(w.__dict__)   ## 获取 对象obj1 的成员