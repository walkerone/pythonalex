# -*- coding:utf-8 -*-
class Dog(object):


    def __init__(self,name):
        self.name = name

    @staticmethod #把eat方法变为静态方法；实际和类没有关系了
    def eat(self):
        print("%s is eating" % self.name)

print("-----------")

d = Dog("ChenRonghua")
d.eat(d)
print('------------\n属性方法')
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food=None
    @property
    def eat(self):
        print(" %s is eating" % self._food)
    @eat.setter
    def eat(self,food):
        print("set eat to eat",food)
        self.__food=food
    @eat.deleter
    def eat(self):
        del self.__food
        print("删除eat成功")
d = Dog("ChenRonghua")
d.eat='小强'


print("------------")

class Flight(object):
    def __init__(self,name):
        self.flight_name=name
    def checking_status(self):
        print("%s flight status"% self.flight_name)
        return 0
    @property
    def status(self):
        status=self.checking_status()
        if status==0:
            print("航班已起飞")
        elif status==1:
            print("航班未起飞")
        else:
            print("later will send message to you")
f=Flight("ca230")
f.status

print("--------------\n下面这个是类方法")
class Dog(object):

    # name="learnfirst"
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" % self.name)
d=Dog("walker")
d.eat()