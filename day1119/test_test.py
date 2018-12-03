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