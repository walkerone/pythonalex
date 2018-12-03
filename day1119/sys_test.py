# -*- coding:utf-8 -*-
# import
f=open("haproxy","r")
f_nes=open("haproxy_new","w")
b=f.readlines()
option=("1、请输入搜索的地址：","2、请输入增加的内容：","3、请输入删除的内容：")
for i in option:
    print(i)
choice=input("请选择操作方式:序列号》》")
if choice==1:
    data=input("请输入搜索地址：")
    address="backend %s\n" %data
    if address in b:
        index_add=b.index(address)
        print(b[index_add],b[index_add+1])
    if address not in b:
        print("你查找的内容不存在")