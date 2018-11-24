# -*- coding:utf-8 -*-
import sys,os
import copy
"""print(sys.argv) #打印环境变量
# print(sys.argv[2])# 取出第几个参数
"""
# cmd_result=os.system("dir")  #执行命令,不保存结果
cmd_res=os.popen("dir").read() #先read下然后赋值给变量
print(cmd_res)

name=["walker","zhang",["dog","cat"]]
namer2=copy.copy(name)  #浅浅的copy只是copy了最外面一层
#copy中的copy和列表中的copy是一样的，深copy是deepcopy


print(name)
print(namer2)
name[0]="walker123"
name[2][0]="Dog"
print(name)
print(namer2)
列表浅copy的三种方式
p1=copy.copy(name)
p1=name.copy()
p1=name[:]