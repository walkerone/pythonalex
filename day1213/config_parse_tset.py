# -*- coding:utf-8 -*-
import configparser
config=configparser.ConfigParser()

config["name"]={
    "one":"three",
    "two":"ls"
}
config["age"]={
    "age1":222,
    "age2":3333
}
with open("config_test.ini","w") as configfile:
    config.write(configfile)



config.read("config_test")
print(config.sections())
print(config["name"]["two"])

class Person(object):

    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.__age)
    def __one(self):
        print("hell0")
    def two(self):
        self.__one()
qiang=Person('walekr','99')

qiang.show()
qiang.two() 