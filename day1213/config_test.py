# -*- coding:utf-8 -*-
import  configparser

config=configparser.ConfigParser()

print(config.sections())
#写入配置文件
config["card"]={
    "card1":"Yinlian",
    "card2":"saoma"
}
config["picture"]={'Name': 'Zara', 'Age': 7, 'Class': 'First'}

with open("config.ini","w",encoding="GBK") as configfile:
    config.write(configfile)    #将内容写入到文件


config.read("config.ini")
#在读取文件之前需要先  read  一下
print(config.sections())
print(config["card"]["card2"])

config["card"]["card2"]="这个是我修改后的"
with open("config.ini","w") as configfile:
    config.write(configfile)

for i,j in config["card"].items():
    print(i,j)

options=config.options("card")
print(options)    #返回字典中的key

item_list=config.items("card")
print(item_list)  #以元组的形式返回列表，返回sections中的值

val=config.get("card","card2")  #获取section中指定key对应的value
print(val)
# va2=config.getint()


config.add_section("add_section")     #新增section并写入到文件
config.write(open("config.ini","w"))
import  time
time.sleep(2)

# config.remove_section("add_section")
# config.write(open("config.ini","w"))

if not config.has_section("add_section"):
    print("ssss")
    config.add_section("add_section")  # 新增section并写入到文件
    config.write(open("config.ini", "w"))
else:
    print("add_section 已经存在了")

config.set("card","card2","哈哈，为啥那么难呢")     #  修改与新增
config.set("card","card_add","哈哈，为啥那么难呢")
config.write(open("config.ini","w"))



