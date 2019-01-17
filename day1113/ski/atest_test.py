# -*- coding:utf-8 -*-
import time
import sys

from ..  import  day1113 as bao

bao.mc()

# def timer(func):
#     def deco():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         all_time=stop_time-start_time
#         print("run_time",all_time)
#     return deco
#
#
# @timer #test1=timer(test1)
# def atest1():
#     time.sleep(3)
#     print("test1",time.time())

# for i in range(30):
#     sys.stdout.write("$")
#     time.sleep(0.2)
#     sys.stdout.flush()
#
def timer(func):   #被装饰函数有参数
    def deco(name):
        start_time=time.time()
        func(name)
        stop_time=time.time()
        all_time=stop_time-start_time
        print(all_time)
    return deco
@timer
def atest(name):
    print (name)
    time.sleep(0.1)
    print ("\n这个是test")
atest("walkerone")


#装饰器有参数
def timers(size):
    print (size)
    def timer(func):   #被装饰函数有参数
        def deco(name):
            start_time=time.time()
            func(name)
            stop_time=time.time()
            all_time=stop_time-start_time
            print (all_time)
        return deco
    return timer
@timers(100)
def atest(name):
    print (name)
    time.sleep(0.1)
    print ("\n这个是test")
atest("walker1206")



#列表生成式
a=[0,1,2,3,4,5]
b=[]
for index,i in enumerate(a):
    a[index]+1
print(a)

c=[]
for i in a:
    c.append(i+1)
print(c)

a=[i+1 for i in range(5)]
print(a)

a = map(lambda x:x+1, [1, 2, 3, 4, 5, 6])
for i in a:
    print(i)
b=[1,2,3,4,5,6]
a=(x**x for x in range(10))

for i in a:
    print(i)


print("--------")
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

data=fib(5)
while True:
    try:
        print(data.__next__())
    except StopIteration as e :
        print(e.value)
        break


#_*_coding:utf-8_*_
__author__ = 'Alex Li'

# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了2个包子!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")

# 通过生成器实现协程并行运算

from collections import Iterable
a=[1,2,3,4,5,6]
print(isinstance(a,Iterable))
print("33333333333333333")


