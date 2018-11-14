#! -*- coding:utf-8 -*-
#https://www.cnblogs.com/songqingbo/p/5126957.html
str = "self_learn"
print(type(str))
str.title()
print(str.title())  # 大写英文首字母
str.count("e")
print(str.count("e"))  # 返回字母的总数
str = "   base  "
str.isspace()
print(str.isspace())  # 所有字符都是空白，则返回true,在S中至少有一个字符，否则为false

intab = "aeiou"
outtab = "12345"
deltab = "thw"
test = "this is string example....wow!!!"
trans = test.maketrans(intab, outtab)  # 创建字符映射转换表
trans1 = test.maketrans(intab, outtab, deltab)  # deltab 要删除的字符
print(test.translate(trans))  # 打印出映射后的字符
print(test.translate(trans1))

str = "Self_Learn"
print(str.upper())  # 全部转换为大写
print(str.istitle())  # 判断英文首字母是否大写
print(str.endswith("N"))   #是否以指定字符串结尾是，返回True
print(str.capitalize())   #字符串第一个字母大写，其它的小写

str = "  Self_ Learn      "
print(str.lstrip())   #省略左边的空格
print(str.rstrip())   #省略右边的空格
print(str.strip())    # 去掉字符串左右的空格
print(str.find("rn")) #返回被查找字符的索引位置

# print(str.format())
print(str.replace("e","6",1))   #替换
print(str.center(100,"n"))    #设置长度，两边补充指定字符,指定字符是可选
print(str.rsplit("e"))       #返回列表,可以设置分隔符，不设置分隔符，默认以空格作为分隔符


str = "  Sel f_  Learn      "
print(str.split(" "))  #返回字符串以什么分隔符
print(str.ljust(100,"0"))   #设置长度右边补充
print(str.rjust(100,"r"),)  #设置长度左边补充
print(str.zfill(50))        #设置长度，左边默认补充0
str="keyvalue"
print(str.isdecimal())  #只有十进制字符，则返回true，否则为假。
print(str.isdigit())    #如果S中的所有字符都是数字，则为真。在S中至少有一个字符，否则为false。
print("*".join(str))    #以指定字符链接
str="\tab"
print(str.isprintable()) #判断字符串中所有字符是否都属于可见字符
str="dddd23423"
print(str.isalnum())     #检查判断字符串是否包含字母数字字符
print(str.isalpha())     #检测字符串是否只由字母组成
str="d3d3"
print(str.isdigit())      #检测字符串是否只由数字组成
print(str.isidentifier()) #检测字符串是否是字母开头


