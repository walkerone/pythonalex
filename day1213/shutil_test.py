# -*- coding:utf-8 -*-

import shutil
f1=open("file1.txt")
f2=open("file2.txt","w")
shutil.copyfileobj(f1,f2)  #餐阿叔为文件对象


shutil.copyfile("file1.txt","file3.txt")   #复制文件

shutil.copy("file1.txt","file4,txt")   #权限和用户组都copy


