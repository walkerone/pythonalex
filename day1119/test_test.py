<<<<<<< HEAD
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
=======
#! -*- coding:utf-8 -*-
import sys
import time
with open('test.txt', mode='w+', encoding='utf-8') as f:
     f.write("tianjin")
     f.seek(0)
     print(type(f.readline()))
     f.flush()
     f.seek(0)
     print(f.readlines())

for i in range(20):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)
>>>>>>> f079b2bfd736be6bab72318fef3c002f57806160
