# -*- coding:utf-8 -*-
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating %s\n" % (self.name,food))
def talk(self):
    print("what is swiming")
d=Dog("big huang")

choice=input("which methord is useing\n")
if hasattr(d,choice):
    # func=getattr(d,choice)   #假如是方法则调用方法执行
    # func('rice')
    print('存在')
    setone=setattr(d,choice,"xiao qiang") #给属性赋值；也可以赋值不存在的方法
    print(getattr(d,choice))
    delattr(d,choice)#删除之后再调用，报错
    if not hasattr(d,choice):  #判断是否已删除
        print("已经删除成功")
else:
    setattr(d,choice,talk)  #假如方法不存在，则设置新的方法
    getattr(d,choice)(d)
    print("不存在这个方法")