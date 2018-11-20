# -*- coding:utf-8 -*-
import sys,os
"""print(sys.argv) #打印环境变量
# print(sys.argv[2])# 取出第几个参数
"""
# cmd_result=os.system("dir")  #执行命令,不保存结果
cmd_res=os.popen("dir").read() #先read下然后赋值给变量
cmd_res.read()
