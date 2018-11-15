# -*- coding:utf-8 -*-
name=input("name is")
age=input("age is ")
info="name={_name},age={_age}".format(_name=name,_age=age)

info2="name={1},age={0}".format(name,age)
print(info)
print(info2)