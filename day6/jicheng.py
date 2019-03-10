# -*- coding:utf-8 -*-
class People(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
    def eat(self):
        print("%s is eating ....." % self.name)
    def talk(self):
        print("%s is talking...." % self.name)
    def sleep(self):
        print("%s is sleeping ..." % self.name)


class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s"% (self.name,obj.name))
        self.friends.append(obj)
class Man(Relation,People):
    def __init(self,name,age,money):
        super(Man,self).__init__(name,age)
        self.money=money
    def sleep(self):
        People.sleep(self)
        print("man is sleeping")
class Women(Relation,People):
    def get_bith(self):
        print("%s is bornd a baby" % self.name)

m1=Man("xiaowang","99")
w1=Women("XIAOHONG","88")

m1.make_friends(w1)
w1.name="xiugai mignzi"
print(m1.friends[0].name)