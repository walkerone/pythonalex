# -*- coding:utf-8 -*-
"""
用户入口
商品信息存在文件里
已购商品，余额记录

商家入口
可以添加商品，修改商品价格
"""
product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
shopping_list = []
salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("what you want buy")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice > 0 and user_choice < len(product_list):
                p_item = product_list[user_choice]
                if p_item[1] < salary:
                    print("买得起呀")
                    shopping_list=shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                    print("added %s into shopping cart,your current balance is\033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("你的金额只剩\033[31;1m%s\033[0m买不起了" % salary)
            else:
                print("produce \033[31:m code\033[0:m is not here")
        elif user_choice == "q":
            print("--------shppintlist----------")
            print(shopping_list)
            exit()
        else:
            print("valid option")
