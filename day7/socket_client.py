# -*- coding:utf-8 -*-
import socket
client=socket.socket()  #声明socket 类型，同时生成sockent连接对象
client.connect(('localhost',6969))
while True:
    cmd=input("---->").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode()) #所有数据的传输都是以btye类型进行
    cmd_res=client.recv(1024)
    with open("dir.txt",'wb') as f1:
        f1.write(cmd_res)
        f1.flush()
    print('recv',cmd_res.decode())
client.close()