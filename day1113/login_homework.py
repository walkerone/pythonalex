# -*- coding:utf-8 -*-
"""
while 循环最多输入三次账号名称和密码，
先判断输入的name是否在lockfile,若是被锁定直接退出，with可以同时打开多个文件
若是不在loclfile,再判断name是否在loginfile，若是则输入密码尝试登录三次，若是正确，则提示欢迎语：
若是输入三次密码且一直未正确，则直接写入lockfile
"""
count = 0

while count < 3:
    flag = False
    account_input = input("input your account:")
    password_input = input("input the account\'s password")
    with open("login_name", "r") as accounts_file, open("lock_account", "r+") as lock_account:
        print(lock_account.read())
        lock_account_name = lock_account.read()
        print(lock_account.tell())
        print(lock_account_name)
        for account_input1 in lock_account_name.split():
            print(lock_account_name.split())
            if account_input1.strip()==account_input:
                flag=True
                break
        accounts = accounts_file.readlines()
        for account in accounts:
            name, password = account.split()
            name = name.strip()
            password = password.strip()
            if name == account_input and password == password_input:
                print("welcome to my family")
                flag=True
                break
    count += 1
    if flag:
        break
else:
    with open("lock_account","a+") as lock_account:
        lock_account.write("\n"+account_input)

