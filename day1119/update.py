#! -*- coding:utf-8 -*-
import  time
with open("file_yuan.py","r",encoding="utf-8") as f1,open("new_file.py","w",encoding="utf-8") as f2:
    for i in f1:
        if i=="So many lovely songs were waiting to be sung\n":
            i="这次是真的了个新的6666666666666666666666666666666666666666666666\n"
        f2.write(i)