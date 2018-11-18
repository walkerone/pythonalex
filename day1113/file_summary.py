"""
对文件操作流程

1 打开文件，得到文件句柄并赋值给一个变量
2 通过句柄对文件进行操作
3 关闭文件

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】,若是文件存在，再先清空文件在写进去
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件
r+，可读写文件。【可读；可写；可追加】,  先读然后再追加不然会直接覆盖（用的最多的）
w+，写读:没什么用)也是先把写的内容加到文件后面（会把原来的文件覆盖掉）
a+，同a
rb 二进制读取文件
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
rb
wb
ab

为了避免打开文件后忘记关闭，可以通过管理上下文
在Python 2.7 后，with又支持同时对多个文件的上下文进行管理
with open('log1') as obj1, open('log2') as obj2:
    pass-

常用方法
read() #读取文件所有内容并返回字符串,注意，不一定能全读回来
        Read at most size bytes, returned as bytes不能这样操作，占用内存太大，当文件非常大时，要一行一行的读文件，要用for 循环
with open("format_test.py","r+") as fp:   #要以这种方式读取整个文件，占用内存最少
    for i in fp:
        print(i)

readline() #读取一行
__next__() #读取下一行: fp.__next__()
readlines() #读取所有内容，并返回列表（一行为列表的一个元素值）:Read and return a list of lines from the stream：不能这样操作，占用内存太大
write() #写一行数据以unicode Write the unicode string s to the stream and return the number of characters written.
writelines(list) #写多行，参数为列表，列表中字符串需要换行，不然会写进一行:Write a list of lines to the stream
seek() #句柄指针操作,到达某个位置,用于移动文件读取指针到指定位置
tell() #获取当前句柄指针位置
truncate() #截取文件句柄头到当前位置的字符串，返回None
flush()  #刷新到硬盘
seekable()# Return True if the stream supports random access
writeable() #Return True if the stream supports writing
name  #print(fp.name)返回文件名
"""
a=["asfdasd","asdfasdf","333333333"]
with open("format_test.py","w+") as fp:
    print(fp.read())
    fp.write("asdf\n")
    print(fp.name)