# -*- coding:utf-8 -*-
import sys,os
import copy
"""print(sys.argv) #打印环境变量
# print(sys.argv[2])# 取出第几个参数
"""
# cmd_result=os.system("dir")  #执行命令,不保存结果
# cmd_res=os.popen("dir").read() #先read下然后赋值给变量
# print(cmd_res)
#
# name=["walker","zhang",["dog","cat"]]
# namer2=copy.copy(name)  #浅浅的copy只是copy了最外面一层
#copy中的copy和列表中的copy是一样的，深copy是deepcopy


def merchant(name=None,price=None,add_product=None):
    #old ,nes 格式为 "computer 5000" 中间有空格
    with open("product_list.txt","r+") as product_file:
        for   products in product_file.readlines():
            for product in products.split():
                if product[0]==name:
                    product[1]=price

        product_file.seek(0)
        product_file.readlines()
        if add_product:
            product_file.write("\n"+add_product)
        product_file.seek(0)
        return product_file.readlines()

old="'Iphone' 580"
new="Iphone 9999"
merchant(name="Iphone",price=66666, add_product="add_productone")
