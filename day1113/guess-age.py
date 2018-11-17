# -*- coding:utf-8 -*-
age_of_old = 56
count = 0
while count < 3:
    age = input("guess_age")
    if not age.isdigit():
        print("请输入整数")
    else:
        age = int(age)
        if age_of_old < age:
            print("think bigger")
        elif age_of_old > age:
            print("think smaller")
        elif age_of_old == age:
            print("right")
            break
        count += 1
        if count==3:
            continue_confirm=input("do you want have a try:")
            if continue_confirm!="n":
                count=0
else:
   print("have try three times,do you want to try again")


