#! -*- coding:utf-8 -*-
list = ["name", "age", "height", "age", "1"]
list.append("333")  # 向列表最后添加
a = list.index("age")  # 饭hi字符的索引
b = list.count("age")  # 返回列表中字符出现的次数
list.remove("age")  # 删除指定字符，若有重合删除索引小的
print(list)
list.insert(2, "second")  # 在列表指定位置插入数据
c = list.sort()  # 将列表排序,若列表中包含int类型则报错，需要改为string类型
list.reverse()  # 该方法没有返回值，但是会对列表的元素进行反向排序。
print(list)
list.pop()  # 默认删除列表最后一个，若是指定索引，则删除所在索引位置的字符串
list.clear()  # 清空列表,该方法没有返回值。
d = ["1", 2, 3, 3]
f = [6, 7, 8, 9]
d.extend(f)  # 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(d)
list.copy()
g = f.copy()  # copy() 则顾名思义，复制一个副本，原值和新复制的变量互不影响,
# 使用=直接赋值，是引用赋值，更改一个，另一个同样会变
f.append("3333")
print(g)
print(f)
