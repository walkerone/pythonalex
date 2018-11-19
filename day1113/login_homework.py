# -*- coding:utf-8 -*-
"""
1 先判断输入的name是否在lockfile,若是被锁定直接退出，with可以同时打开多个文件
2 若是不在loclfile,再判断name是否在loginfile，若是则输入密码尝试登录三次，若是正确，则提示欢迎语：
若是输入三次密码且一直未正确，则直接写入锁定文件
"""
count = 0
while count <3:

    with open("login_name","r") as file:
        name=file.readline()
        password=file.readline()
        cofirm_name = input("your name:")
        confim_password = input("your password:")
        count+=1
        if cofirm_name == name:
            if confim_password == password:
                print("welcome to my family")
                break
            else:
                print("cofirm_password is wrong")
        else:
            with open("lock_file","a") as lock_account:
                lock_account.write(cofirm_name)
            print("valid name")
else:
    print("you have try three times")
