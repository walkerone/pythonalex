# -*- coding:utf-8 -*-
import time


def cousumer(name):
    print("%s 主备吃包子了" % name)
    while True:
        baozi = yield
        print("%s is 被%s吃包子" % (baozi,name))


c=cousumer("walker")

# def producer():
#     c1=cousumer("one")  #
#     c2=cousumer("two")   #消费者生成完之后为什么执行  __next__方法，如果不执行  __next__，则只是将函数变为了生成器，执行__next__方法会走到baozi=yield，并返回
#     c1.__next__()
#     c2.__next__()
#     print("准备开始吃包子了")
#     for i in range(10):
#         print("做了一个包子")
#         c1.send("韭菜")
#         c2.send("牛肉")
#         print("------------------")
#         time.sleep(1)
# producer()
#abs 取绝对值
print(abs(-10))
# all() 可迭代对象中的元素是否为真，如果为真则返回为true
all([1,-10,0])
# 可迭代对象中的元素只有一个为真，如果为真则返回为true
any("AFASDF")
#ascil 将内存数据对象变成可打印的字符串的形式
a=ascii([1,2,3,"卡萨丁"])
print(type(a))
print(bin(255))#将数字转换成二进制
print(bool(8)) #判断真假
print(callable(5))  #判断是否可以被调用
print(chr(99))  #将数字对应的ascil 得表反应出来和ord() 取反

{}  #这是默认字典
dict()#这也是一个字典
a=dict({"name":"zxhang"})
print(type(a))
print(dir(a))   #dir()  查询有什么方法

# eval()    #将字符串装换为字典
# exec()

b=filter(lambda n:n>5,range(10))  #过滤
for i in b:
    print(i)

m=map(lambda  n:n**n,range(10))  #将后面函数的值传个前面的函数处理返回一个列表，或其它
for i in m:
    print(i)

a=set([11,1,1,1888])
a=frozenset([11,1,1,1888])  #冻结

print(globals())  #返回当前文件的变量的key,value


print(hash("阿斯蒂芬拉斯科技是的发个"))