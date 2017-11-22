#!/usr/bin/env python

import paramiko
import re
import time

def ssh_conn(hostname, port, username, password):
    scon=paramiko.SSHClient()
    scon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    scon.connect(hostname=hostname, port=port, username=username, password=password)
    chan=scon.invoke_shell()
    return chan

def main():

    hostname='192.168.8.246'
    port=22
    username='root'
    password='root'
    s=ssh_conn(hostname, port, username, password)
    coun=s.send('lsh\n')
    time.sleep(1)
    if coun:
	rst=s.recv(5000)
    coun=s.send('show version\n')
    time.sleep(1)
    if coun:
	rst=s.recv(5000)
    output=re.findall('V[0-9]\.[0-9]\.[0-9]{3}', rst)
    print output

if __name__=="__main__":
    main()


