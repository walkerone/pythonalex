 #! -*- coding:utf-8 -*-
dict2={"height":100,"colour":"red"}
for i,value in dict2.items():  #items() 方法以列表返回可遍历的(键, 值) 元组数组。
    print(dict2.items())
    print(i,value)

name = {"name": "zhang", "age": 100}
name.clear()  # 用于删除字典内所有元素,该函数没有任何返回值
m=("zhang","qiang")
print(dict.fromkeys(m,"wang"))   # fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
name = {"name": "zhang", "age": 100}
name.pop("name")  #删除指定的值，参数键值

dict2={"height":100}
dict={"colour":"red"}
dict.update(dict2)     #把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
print(dict)

print(dict.get("colour"))  #返回指定键的值，如果值不在字典中返回default值
