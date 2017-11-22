#! /usr/bin/env python

import paramiko
import re
import time
import sshtest

def low_alarm():
    s=sshtest.ssh_conn('192.168.8.246',22,'root','root')
    s.send('lsh\n')
    time.sleep(1)
    s.send('show ne alarm\n')
    time.sleep(1)
    output=s.recv(5000)
    time.sleep(1)
    rst=re.findall('Low',output)
    if rst:
        print 'temp low occur'
    else:
        print 'no temp low'
    return rst

def main():
    while 1:
        r=low_alarm()
        if r:
            break
        else:
            time.sleep(10)
    s.close()

if __name__=="__main__":
    main()

