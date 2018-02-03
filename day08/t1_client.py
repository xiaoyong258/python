#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import socket
import sys 

client = socket.socket()
client.connect(("localhost",9997))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0: 
        continue
    client.send( msg.encode("utf-8"))
    data = client.recv(1024)
    print("来自服务器:",data)

client.close()

