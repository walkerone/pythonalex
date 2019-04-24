# -*- coding:utf-8 -*-
import socket
client=socket.socket()  #声明socket 类型，同时生成sockent连接对象
client.connect(('localhost',6969))
while True:
    msg=input("---->").strip()
    client.send(msg.encode()) #所有数据的传输都是以btye类型进行
    data=client.recv(1024)
    with open("dir.txt",'wb') as f1:
        f1.write(data)
        f1.flush()
    print('recv',data.decode())
client.close()