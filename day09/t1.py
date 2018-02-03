#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.171.193', username='xiaoyong', password='MCSE+ccna=Mcsd')
stdin, stdout, stderr = ssh.exec_command('ls')

for line in stdout:
    print('...' + line.strip('\n'))

ssh.close()



