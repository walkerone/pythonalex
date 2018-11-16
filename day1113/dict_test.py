 #! -*- coding:utf-8 -*-
"""
键必须是唯一的，但值则不必
len(dict) 计算字典元素个数，即键的总数
str(dict) 输出字典，以可打印的字符串表示
setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
popitem() 方法随机返回并删除字典中的一对键和值
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典

"""
dict2={"height":100,"colour":"red"}
for i,value in dict2.items():  #items() 方法以列表返回可遍历的(键, 值) 元组数组。
    print(dict2.items())
    print(i,value)
m=("zhang","qiang")
print(dict.fromkeys(m,"wang"))   # fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
print(dict2.get("6666","这个是默认值"))  #返回指定键的值，如果值不在字典中返回default值
key=dict2.keys()#Python3 字典 keys() 方法返回一个迭代器，可以使用 list() 来转换为列表:字典 values() 方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。

print(list(key))

name = {"name": "zhang", "age": 100}
name.clear()  # 用于删除字典内所有元素,该函数没有任何返回值

name = {"name": "zhang", "age": 100}
name.pop("name")  #删除指定的值，参数键值

dict2={"height":100}
dict={"colour":"red"}
dict.update(dict2)     #把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
print(dict)