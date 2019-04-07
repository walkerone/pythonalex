# -*- coding:utf-8 -*-
data={"name":"walker","age":33}
try:
    data["weight"]
except (KeyError,IndexError) as e: #这样一次只能捕获一个错误；如果对两种错误的处理方式一样，可以用这种方式进行处理
    print("字典不存在",e)
print("----------")
list1=["sadfasd","sadfsadf",333]
# list1[5]
try:
    list1[5]
except IndexError as e:
    print(e)
print("------------")
m=6666
try:
    data["weight"]
    print("字典不存在",e)
    print(m[9])
except IndexError as e:
    print(e)
except Exception as e:  #抓住所有的错误;不建议一开始就是用使用
    print("未知错误")
else:
    print("一切正常")
finally:
    print("finally 是有错没错都执行")

print("-------\n自定义异常")
class mysqlerror(Exception):
    def __init__(self,msg):
        self.msg="23333333"
    def __str__(self):
        return "asdf"
try:
    raise mysqlerror("数据库连不上出错了吧哈哈")  #raise触发自己编写的异常；自定义异常时不要覆盖已有的异常
except mysqlerror as e:
    print(e)


