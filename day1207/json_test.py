# -*- coding:utf-8 -*-
import  json
#json的四个常用方法的使用
a={"name":True}
b=json.dumps(a)
print(b,"---one")
c=json.loads(b)
print(c,"---two")

with open("f.txt","w+") as f:
    json.dump(c,f)
    f.seek(0)
    print(f.read(),"----three")
    f.seek(0)
    d=json.load(f)
    print(d,"---four")
