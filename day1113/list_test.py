#! -*- coding:utf-8 -*-
"""
len() ,len(list)方法返回列表元素个数,list -- 要计算元素个数的列表，返回值，返回列表元素个数
元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
list( seq ) 方法用于将元组或字符串转换为列表,返回值，返回列表
#可以直接del list[2] 删除列表中的元素
#列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表
列表可以嵌套列表
序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推
"""
list = ["name", "age", "height", "age", "1"]
list.append("333")  # 向列表最后添加，该方法无返回值，但是会修改原来的列表
a = list.index("age")  # 该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
b = list.count("age")  # 返回列表中字符出现的次数，返回值：返回元素在列表中出现的次数
list.remove("age")  # 删除指定字符，若有重合删除索引小的，该方法没有返回值但是会移除两种中的某个值的第一个匹配项
print(list)
list.insert(2, "second")  # 在列表指定位置插入数据，该方法没有返回值，但会在列表指定位置插入对象
c = list.sort()  # 将列表排序,若列表中包含int类型则报错，需要改为string类型
list.reverse()  # 该方法没有返回值，但是会对列表的元素进行反向排序。
print(list)
list.pop()  # 默认删除列表最后一个，若是指定索引，则删除所在索引位置的字符串
list.clear()  # 清空列表,该方法没有返回值。
d = ["1", 2, 3, 3]
f = [6, 7, 8, 9]
d.extend(f)  # 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），该方法没有返回值，但会在已存在的列表中添加新的列表内容
print(d)
list.copy()
g = f.copy()  # copy() 则顾名思义，复制一个副本，原值和新复制的变量互不影响,
# 使用=直接赋值，是引用赋值，更改一个，另一个同样会变
f.append("3333")
print(g)
print(f)
