#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import socket
import sys
import os 

server = socket.socket()
server.bind(("localhost",9997))

server.listen()
while True:
    print("等待客户端的连接...")
    conn,addr = server.accept()
    print("新连接:",addr)

    while True:
        data=conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break
        print("收到命令:",data)
        res = os.popen(data.decode()).read()
        print(len(res))
        conn.send(res.encode("utf-8"))

server.close()

