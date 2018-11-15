# -*- coding:utf-8 -*-
age_of_old = 56
count=0
while True:
    age = int(input("guess_age"))
    if age_of_old < age:
        print("think bigger")
    elif age_of_old > age:
        print("think smaller")
    elif age_of_old == age:
        print("right")
        break
    count+=1
else: