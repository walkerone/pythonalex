# -*- coding:utf-8 -*-
import time

def timer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        all_time=stop_time-start_time
        print("run_time",all_time)
    return deco
@timer #test1=timer(test1)
def test1():
    time.sleep(3)
    print("test1",time.time())
test1()
