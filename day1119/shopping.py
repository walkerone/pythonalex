#! -*- coding:utf-8 -*-
# https://www.cnblogs.com/zpzcy/p/7668765.html
"""
需求:
启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额
"""
product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
# product_list.a
salary = input("what is your salary")
shopping = []
# shopping_number = input("the number of whtat you want buy")
# print(type(product_list[int(shopping_number)]))
# print(product_list[int(shopping_number)][0])
# shopping_market = shopping.append(product_list[int(shopping_number)][0])
if salary.isdigit():
    salary = int(salary)  # 控制台输入的都是字符串
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        use_choice = input("选择要买商品的number")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and use_choice > 0:
               p_item=product_list[user_choice]
