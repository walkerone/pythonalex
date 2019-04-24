# -*- coding:utf-8 -*-
import  socket
import os
server=socket.socket()
server.bind(('localhost',6969))
server.listen()
print("开始等电话")
conn,addr=server.accept()  #等电话
#conn 就是客户端连接过来而在服务器为其生成的一个连接实例
print(conn,addr)
while True:
    data=conn.recv(1024)
    if not data:
        print("client have lost")
        break
    print(data.decode('utf-8'))
    data=os.popen(data.decode('utf-8'))  #popen执行命令
    res=data.read()
    conn.send(res.encode())
    conn.sendall() #相当于for 循环进行send
server.close()


