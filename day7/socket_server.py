# -*- coding:utf-8 -*-
import  socket
import os
server=socket.socket()  #实例
server.bind(('localhost',6969))  #绑定
server.listen()   #监听
print("开始等电话")

#conn 就是客户端连接过来而在服务器为其生成的一个连接实例

while True:
    conn,addr=server.accept()
    print(conn)
    while True:
        print("等待新的指令")
        data=conn.recv(1024)
        if not data:
            print("client 已断开")
            break
        print(data.decode('utf-8'))
        data=os.popen(data.decode('utf-8'))  #popen执行命令,接收的是字符串，执行结果也是字符串
        cmd_res=data.read()
        print(len(cmd_res))
        if len(cmd_res)==0:
            cmd_res=b"cmd has no output"
        conn.send(cmd_res.encode())
        print("send done")
    # conn.sendall() #相当于for 循环进行send
server.close()


