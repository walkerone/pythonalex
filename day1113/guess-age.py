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
        count += 1
else:
    print("have try three times")
